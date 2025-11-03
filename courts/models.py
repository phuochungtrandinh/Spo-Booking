# courts/models.py
from django.db import models

class Court(models.Model):
    STATUS_CHOICES = [
        ('active', 'Đang hoạt động'),
        ('inactive', 'Tạm dừng'),
    ]

    name = models.CharField(max_length=100, verbose_name="Tên sân")
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Giá theo giờ")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', verbose_name="Tình trạng")

    def __str__(self):
        return self.name
