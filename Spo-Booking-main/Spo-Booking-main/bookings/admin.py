from django.contrib import admin
from .models import Bookings

# Register your models here.
class BookingsAdmin(admin.ModelAdmin):
    class Meta:
        model = Bookings

admin.site.register(Bookings, BookingsAdmin)
