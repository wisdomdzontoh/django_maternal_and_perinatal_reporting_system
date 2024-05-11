from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'region_name', 'region_code', 'date_created')
    search_fields = ['region_name', 'region_code', 'date_created']  # Adjusted search fields for Region

@admin.register(models.District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'district_region', 'district_name', 'district_code', 'date_created')
    search_fields = ['district_region__region_name', 'district_name', 'district_code', 'date_created']  # Added search fields for District
    
@admin.register(models.Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'facility_region', 'facility_district', 'facility_name', 'facility_code', 'date_created')
    search_fields = ['facility_region__district_name', 'facility_name', 'facility_code', 'date_created']  # Added search fields for District
