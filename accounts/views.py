from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from bookings.models import Bookings
from django.db.models import Q

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
def profile_view(request):
    user = request.user

    # Lay lich su dat san
    bookings = Bookings.objects.filter(user=user).select_related('court').order_by('-start_time')

    # Xu ly cap nhat thong tin
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'update_info':
            email = request.POST.get('email', '').strip()
            phone = request.POST.get('phone', '').strip()
            full_name = request.POST.get('full_name', '').strip()

            # Kiem tra email trung
            if email and User.objects.filter(email=email).exclude(id=user.id).exists():
                messages.error(request, 'Email da duoc su dung boi tai khoan khac.')
            else:
                user.email = email
                user.first_name = full_name
                user.save()
                messages.success(request, 'Cap nhat thong tin thanh cong.')
                return redirect('accounts:profile')

        elif action == 'change_password':
            old_password = request.POST.get('old_password', '')
            new_password = request.POST.get('new_password', '')
            confirm_password = request.POST.get('confirm_password', '')

            if not user.check_password(old_password):
                messages.error(request, 'Mat khau cu khong dung.')
            elif new_password != confirm_password:
                messages.error(request, 'Mat khau moi khong khop.')
            elif len(new_password) < 6:
                messages.error(request, 'Mat khau phai co it nhat 6 ky tu.')
            else:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Doi mat khau thanh cong.')
                return redirect('accounts:profile')

    context = {
        'user': user,
        'bookings': bookings,
    }
    return render(request, 'accounts/profile.html', context)
