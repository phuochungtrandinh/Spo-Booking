from django.contrib import admin
from .models import Users
# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    class Meta:
        model = Users

admin.site.register(Users, UsersAdmin)
