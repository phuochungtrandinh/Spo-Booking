from django.contrib import admin
from .models import Courts
# Register your models here.
class CourtsAdmin(admin.ModelAdmin):
    class Meta:
        model = Courts

admin.site.register(Courts, CourtsAdmin)
