from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST.get('email', '')

        if password != password2:
            messages.error(request, "Mật khẩu không khớp.")
            return redirect('accounts:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Tên đăng nhập đã tồn tại.")
            return redirect('accounts:register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Gán user vào nhóm Customer
        group, created = Group.objects.get_or_create(name='Customer')
        user.groups.add(group)

        messages.success(request, "Tạo tài khoản thành công, vui lòng đăng nhập.")
        return redirect('accounts:login')

    return render(request, 'accounts/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:  # nếu là admin
                return redirect('list_courts')  # chuyển đến trang quản lý sân
            else:
                return redirect('home_page')  # chuyển đến trang khách hàng
        else:
            messages.error(request, 'Sai tài khoản hoặc mật khẩu')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, "Đăng xuất thành công.")
    return redirect('accounts:login')


@login_required
def dashboard_view(request):
    if request.user.is_staff or request.user.is_superuser:
        return redirect('/admin/')
    return render(request, 'accounts/customer_dashboard.html', {'user': request.user})
