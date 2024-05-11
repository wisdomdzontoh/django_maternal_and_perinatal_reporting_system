from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Region(models.Model):
    region_name = models.CharField(max_length=100)
    region_code = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f"{self.region_name} ({self.region_code})"
    
    
class District(models.Model):
    district_region = models.ForeignKey(Region, on_delete=models.PROTECT)
    district_name = models.CharField(max_length=100)
    district_code = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.district_name} ({self.district_code})"
    
class Facility(models.Model):
    facility_region = models.ForeignKey(Region, on_delete=models.PROTECT)
    facility_district = models.ForeignKey(District, on_delete=models.PROTECT)
    facility_name = models.CharField(max_length=100)
    facility_code = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.facility_name}"
