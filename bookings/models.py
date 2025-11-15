from django.db import models
from django.contrib.auth.models import User
class Bookings(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'PENDING'),
        ('CONFIRMED', 'CONFIRMED'),
        ('CANCELLED', 'CANCELLED'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    court = models.ForeignKey(
        'courts.Court',
        db_column='CourtId',
        on_delete=models.DO_NOTHING,
        related_name='bookings'
    )
    start_time = models.DateTimeField(db_column='StartTime')
    end_time   = models.DateTimeField(db_column='EndTime')
    hours = models.DecimalField(db_column='Hours', max_digits=4, decimal_places=2)
    price_per_hour_snapshot = models.DecimalField(db_column='PricePerHourSnapshot', max_digits=12, decimal_places=0)
    total_amount = models.DecimalField(db_column='TotalAmount', max_digits=12, decimal_places=0)
    status = models.CharField(db_column='Status', max_length=10, choices=STATUS_CHOICES, default='PENDING')
    note = models.CharField(db_column='Note', max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)

    class Meta:
        verbose_name = "Quản lý đặt lịch"
        verbose_name_plural = "Quản lý đặt lịch"
        managed = True
        db_table = 'Bookings'
        indexes = [
            models.Index(fields=['court', 'start_time'], name='idx_booking_court_time'),
            models.Index(fields=['user', 'start_time'],  name='idx_booking_user_time'),
        ]