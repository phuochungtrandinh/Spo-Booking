from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('qr/<int:booking_id>/', views.payment_qr, name='payment_qr'),
    path('qr/demo/', views.payment_qr_preview, name='payment_qr_preview'),
]


