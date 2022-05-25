from django.contrib import admin
from meetings.models import Event
from import_export.admin import ImportExportModelAdmin  


# Register your models here.




admin.site.register(Event) 