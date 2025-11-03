from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from datetime import datetime, timedelta

from bookings.models import Bookings


@login_required
def payment_qr(request, booking_id):
    booking = get_object_or_404(Bookings, id=booking_id)

    context = {
        'booking': booking,
        'total_amount': booking.total_amount,
    }
    return render(request, 'payments/payment_qr.html', context)


def payment_qr_preview(request):
    # Dữ liệu mẫu để xem giao diện khi chưa có booking thực tế
    class DummyBooking:
        id = 9999
        start_time = datetime.now()
        end_time = datetime.now() + timedelta(hours=2)

    context = {
        'booking': DummyBooking(),
        'total_amount': Decimal('150000'),
    }
    return render(request, 'payments/payment_qr.html', context)
