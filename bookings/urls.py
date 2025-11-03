
from django.urls import path
from . import views

app_name = 'bookings'
urlpatterns = [
    path('admin/', views.admin_booking_list, name='admin_booking_list'),
    path('customer/', views.customer_booking, name='customer_booking'),
]
