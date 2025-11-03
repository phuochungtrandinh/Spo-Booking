from django.shortcuts import render

def home_page(request):
    """
    Trang chủ public: hiển thị hero, nút Đăng nhập/Đăng ký.
    """
    return render(request, 'home/home.html')



