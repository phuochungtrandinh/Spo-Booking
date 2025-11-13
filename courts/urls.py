# courts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_courts, name='list_courts'),
    path('add/', views.add_court, name='add_court'),
    path('edit/<int:pk>/', views.edit_court, name='edit_court'),
    path('delete/<int:pk>/', views.delete_court, name='delete_court'),
]
