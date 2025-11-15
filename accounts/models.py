from django.db import models

class Users(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)
    password = models.CharField(db_column='Password', max_length=255)
    full_name = models.CharField(db_column='FullName', max_length=255, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=255, unique=True, blank=True, null=True)
    phone = models.CharField(db_column='Phone', max_length=20, unique=True, blank=True, null=True)
    role = models.CharField(db_column='Role', max_length=10, default='User')
    is_active = models.BooleanField(db_column='IsActive', default=True)
    is_deleted = models.BooleanField(db_column='IsDeleted', default=False)
    created_at = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)
    updated_at = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)

    class Meta:
        verbose_name = "Quản lý khách hàng"
        verbose_name_plural = "Quản lý khách hàng"
        managed = True
        db_table = 'Accounts'

    def __str__(self):
        return self.full_name or self.email or self.phone or f'User #{self.id}'

