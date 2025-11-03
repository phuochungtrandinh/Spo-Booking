from django.db import models

class Courts(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=120)
    address = models.CharField(db_column='Address', max_length=255)
    description = models.TextField(db_column='Description', blank=True, null=True)
    image_url = models.CharField(db_column='ImageUrl', max_length=512, blank=True, null=True)
    is_active = models.BooleanField(db_column='IsActive', default=True)
    price_per_hour = models.DecimalField(db_column='PricePerHour', max_digits=12, decimal_places=0)
    created_at = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)
    updated_at = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Courts'
        verbose_name_plural = 'Courts'

    def __str__(self):
        return self.name

class Courtphotos(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)
    court = models.ForeignKey(Courts, db_column='CourtId', on_delete=models.CASCADE, related_name='photos')
    image_url = models.CharField(db_column='ImageUrl', max_length=512)
    caption = models.CharField(db_column='Caption', max_length=255, blank=True, null=True)
    sort_order = models.IntegerField(db_column='SortOrder', default=0)
    created_at = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)
    updated_at = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CourtPhotos'
        unique_together = (('court', 'sort_order'),)

    def __str__(self):
        return f'{self.court.name} - photo #{self.id}'

class Courtclosures(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)
    court = models.ForeignKey(Courts, db_column='CourtId', on_delete=models.CASCADE, related_name='closures')
    start_time = models.DateTimeField(db_column='StartTime')
    end_time = models.DateTimeField(db_column='EndTime')
    reason = models.CharField(db_column='Reason', max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CourtClosures'

    def __str__(self):
        return f'Closure {self.court.name} {self.start_time}–{self.end_time}'