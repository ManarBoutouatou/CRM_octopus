from django.contrib import admin
from cashflow.models import  Account
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = [ 'name','acc_type', ]


admin.site.register(Account, AccountAdmin) 
