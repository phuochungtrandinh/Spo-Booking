# booking/views.py
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from datetime import datetime
from decimal import Decimal
from django.contrib import messages

from .models import Bookings
from courts.models import Court

from accounts.models import Users
from django.shortcuts import render


@login_required
def customer_booking(request):
    courts = Court.objects.all()

    if request.method == 'POST':
        court_id = request.POST.get('court')
        date_str = request.POST.get('date')
        start_time_str = request.POST.get('start_time')
        end_time_str = request.POST.get('end_time')
        note = request.POST.get('note', '')

        # Gộp ngày + giờ thành datetime đầy đủ
        start_datetime = datetime.strptime(f"{date_str} {start_time_str}", "%Y-%m-%d %H:%M")
        end_datetime = datetime.strptime(f"{date_str} {end_time_str}", "%Y-%m-%d %H:%M")

        court = Court.objects.get(id=court_id)

        # Tính số giờ đặt
        total_hours = (end_datetime - start_datetime).seconds / 3600

        # Tính tiền (dựa trên giá sân hiện tại)
        price_per_hour = court.price_per_hour  # cần có field này trong bảng Courts
        total_amount = Decimal(total_hours) * Decimal(price_per_hour)


        booking = Bookings.objects.create(
            user=request.user,
            court=court,
            start_time=start_datetime,
            end_time=end_datetime,
            hours=Decimal(total_hours),
            price_per_hour_snapshot=Decimal(price_per_hour),
            total_amount=Decimal(total_amount),
            note=note,
            status='PENDING'
        )

        messages.success(request, "✅ Đặt lịch thành công! Vui lòng chờ xác nhận từ quản trị viên.")
        return redirect('customer_booking')

    context = {'courts': courts}
    return render(request, 'bookings/customer_booking.html', context)