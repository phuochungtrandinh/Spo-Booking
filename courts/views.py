# courts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Court
from django.contrib import messages

def list_courts(request):
    courts = Court.objects.all()
    return render(request, 'courts/list_courts.html', {'courts': courts})

def add_court(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        status = request.POST.get('status')
        Court.objects.create(name=name, price_per_hour=price, status=status)
        messages.success(request, 'Thêm sân thành công!')
        return redirect('list_courts')
    return render(request, 'courts/add_court.html')

def edit_court(request, pk):
    court = get_object_or_404(Court, pk=pk)
    if request.method == 'POST':
        court.name = request.POST.get('name')
        court.price_per_hour = request.POST.get('price')
        court.status = request.POST.get('status')
        court.save()
        messages.success(request, 'Cập nhật sân thành công!')
        return redirect('list_courts')
    return render(request, 'courts/edit_court.html', {'court': court})

def delete_court(request, pk):
    court = get_object_or_404(Court, pk=pk)
    court.delete()
    messages.success(request, 'Xóa sân thành công!')
    return redirect('list_courts')
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')  # hoặc trang chủ nếu bạn chưa có trang đăng nhập

