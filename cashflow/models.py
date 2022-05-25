from django.db import models
from project.models import Project
import uuid
from datetime import date, timedelta
# from dateutil.relativedelta import relativedelta
from django.urls import reverse
from django.utils.translation import gettext as _
from contact.models import Company, Employee 
from project.models import Project
from django.db.models import Sum
# Create your models here.
TRANSACTION_STATE= (
    ('IN', 'In'),
    ('OU', 'Out'),   
) 
TRANSACTION_TYPE_CHOICES= (
    ('PA', 'paiement'),
    ('SA', 'salaire '),
    ('CR', 'creance'),
    ('CH', 'charges'),   
    ('AL', 'allouer'),  
) 
class TransactionManager(models.Manager):
    def get_total_payment(self):
        return Transaction.objects.filter(type="PA").aggregate(Sum('amount'))
    def get_total_salaire(self):
        return Transaction.objects.filter(type="SA").aggregate(Sum('amount'))
    def get_total_creance(self):
        return Transaction.objects.filter(type="CR").aggregate(Sum('amount'))
    def get_total_charges(self):
        return Transaction.objects.filter(type="CH").aggregate(Sum('amount'))
    def get_total_allouer(self):
        return Transaction.objects.filter(type="AL").aggregate(Sum('amount'))
    def get_account_payment(self, account_id):
        return Transaction.objects.filter(type="PA", account_id = account_id).aggregate(Sum('amount'))
    def get_account_salaire(self, account_id):
        return Transaction.objects.filter(type="SA", account_id = account_id).aggregate(Sum('amount'))
    def get_account_creance(self, account_id):
        return Transaction.objects.filter(type="CR", account_id = account_id).aggregate(Sum('amount'))
    def get_account_charges(self, account_id):
        return Transaction.objects.filter(type="CH", account_id = account_id).aggregate(Sum('amount'))
    def get_account_allouer(self, account_id):
        return Transaction.objects.filter(type="AL", account_id = account_id).aggregate(Sum('amount'))

class Account (models.Model): 
    owner        = models.ManyToManyField(Project, related_name="project_name" )
    type         = models.CharField(choices=TRANSACTION_STATE, max_length=2, blank=True, null=True)
    created      = models.DateField(auto_now=True)
    updated      = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.owner)

class Transaction(models.Model): 
    account      = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE, related_name="sender") 
    receiver     = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE, related_name="receiver")
    project      = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE) 
    type         = models.CharField(choices=TRANSACTION_TYPE_CHOICES, max_length=2, blank=True, null=True)
    other        = models.CharField(max_length=254, blank=True, null=True)
    amount       = models.DecimalField(max_digits=20 , decimal_places=0, blank=True, null=True)
    date         = models.DateField(blank=True, null=True)
    note         = models.CharField(max_length=254, blank=True, null=True)
    created      = models.DateField(auto_now=True)
    updated      = models.DateField(auto_now_add=True)
    objects      = models.Manager()
    payments     = TransactionManager()
    def __str__(self):
        return str(self.project)

