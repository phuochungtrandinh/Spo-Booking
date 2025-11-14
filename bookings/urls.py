
from django.urls import path
from . import views

app_name = 'bookings'
urlpatterns = [
    path('customer/', views.customer_booking, name='customer_booking'),
    ]


