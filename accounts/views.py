from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email', '')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # 1. Kiểm tra mật khẩu trùng nhau
        if password != password2:
            messages.error(request, 'Mật khẩu không khớp.')
            return redirect('accounts:register')

        # 2. Kiểm tra username đã tồn tại chưa
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Tên đăng nhập đã tồn tại.')
            return redirect('accounts:register')

        # 3. Tạo user mới
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        # 4. Gán user vào group "Customer" (nếu chưa có thì tự tạo)
        group, created = Group.objects.get_or_create(name='Customer')
        user.groups.add(group)

        messages.success(request, 'Tạo tài khoản thành công, vui lòng đăng nhập.')
        return redirect('accounts:login')

    # GET: hiển thị form đăng ký
    return render(request, 'accounts/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # email/phone/username
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng.')

    # GET hoặc lỗi: hiển thị lại form đăng nhập
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'Đăng xuất thành công.')
    return redirect('accounts:login')