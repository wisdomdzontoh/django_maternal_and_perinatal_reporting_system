from django.contrib import admin
from maternal_entry.models import MaternalEntry
from import_export.admin import ImportExportModelAdmin



# Register your models here.
admin.site.register(MaternalEntry, ImportExportModelAdmin)