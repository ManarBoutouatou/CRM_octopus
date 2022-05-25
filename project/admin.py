from django.contrib import admin
from project.models import Project
from import_export.admin import ImportExportModelAdmin  

# Register your models here.


@admin.register(Project)
class ProjectImportExport(ImportExportModelAdmin) : 
    pass  


# admin.site.register(Project) 