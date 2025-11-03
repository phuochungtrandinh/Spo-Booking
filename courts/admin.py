from django.contrib import admin
from .models import Court
# Register your models here.
class CourtsAdmin(admin.ModelAdmin):
    class Meta:
        model = Court

from django.contrib import admin
from .models import Court

@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_hour', 'status')
