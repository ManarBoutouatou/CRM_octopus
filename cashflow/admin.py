from django.contrib import admin
from cashflow.models import Transaction, Account
# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'receiver','other', 'type', 'project', 'amount']
class AccountAdmin(admin.ModelAdmin):
    list_display = [ 'type']

admin.site.register(Transaction, TransactionAdmin) 
admin.site.register(Account, AccountAdmin) 
