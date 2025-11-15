from django.db import models

class Payments(models.Model):
    STATUS_CHOICES = (('PENDING','PENDING'), ('VERIFIED','VERIFIED'), ('REJECTED','REJECTED'))

    booking = models.OneToOneField(
        'bookings.Bookings',
        db_column='BookingId',
        on_delete=models.CASCADE,
        related_name='payment'
    )
    amount = models.DecimalField(db_column='Amount', max_digits=12, decimal_places=0)
    reference = models.CharField(db_column='Reference', max_length=200)
    transfer_screenshot = models.CharField(db_column='TransferScreenshot', max_length=512, blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=10, choices=STATUS_CHOICES, default='PENDING')
    verified_by = models.ForeignKey(
        'accounts.Users',
        db_column='VerifiedBy',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='verified_payments'
    )
    verified_at = models.DateTimeField(db_column='VerifiedAt', blank=True, null=True)
    created_at = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)

    class Meta:
        verbose_name = "Quản lý thanh toán"
        verbose_name_plural = "Quản lý thanh toán"
        managed = True
        db_table = 'Payments'
        indexes = [
            models.Index(fields=['reference'], name='idx_payment_reference'),
            models.Index(fields=['status'],    name='idx_payment_status'),
        ]