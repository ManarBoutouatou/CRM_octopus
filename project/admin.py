from django.contrib import admin
from project.models import Project, Transaction
from import_export.admin import ImportExportModelAdmin  

# Register your models here.
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'project','other', 'tr_type', 'amount', 'date']
admin.site.register(Transaction, TransactionAdmin) 

@admin.register(Project)
class ProjectImportExport(ImportExportModelAdmin) : 
    pass  


# admin.site.register(Project) 