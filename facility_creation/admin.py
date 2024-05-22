from django.contrib import admin
from . import models
import data_wizard
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(models.Region)
class RegionAdmin(ImportExportModelAdmin):
    list_display = ('region_name', 'id', 'region_code', 'date_created', 'created_by')
    search_fields = ['region_name', 'region_code', 'date_created']  # Adjusted search fields for Region

@admin.register(models.District)
class DistrictAdmin(ImportExportModelAdmin):
    list_display = ('district_name', 'district_region', 'id', 'district_code', 'date_created')
    search_fields = ['district_region__region_name', 'district_name', 'district_code', 'date_created']  # Added search fields for District
    
@admin.register(models.Facility)
class FacilityAdmin(ImportExportModelAdmin):
    list_display = ('facility_name', 'facility_region', 'facility_district', 'id', 'facility_code', 'date_created')
    search_fields = ['facility_region__region_name', 'facility_name', 'facility_code', 'date_created']  # Added search fields for District
