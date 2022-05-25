from django.contrib import admin
from .models import Company, Employee, Lead  
from import_export.admin import ImportExportModelAdmin  
# Register your models here. 

@admin.register(Company)
class CompanyImportExport(ImportExportModelAdmin) : 
    pass 

@admin.register(Employee)
class EmployeeImportExport(ImportExportModelAdmin) : 
    pass 

@admin.register(Lead)
class LeadImportExport(ImportExportModelAdmin) : 
    pass 
# admin.site.register(Company) 
# admin.site.register(Employee) 
# admin.site.register(Lead) 
