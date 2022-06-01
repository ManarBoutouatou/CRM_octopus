from django.db import models

from tinymce import models as tinymce_models
from cashflow.models import Account
from contact.models import Employee, Company
from config import settings
from django.db.models import Sum
# Create your models here.

user = settings.AUTH_USER_MODEL
PROJECT_TYPE_CHOICES = (
    ('EC', 'e-commerce'),
    ('WS', 'web site'),
    ('WA', 'web app'),
)

CONTRACT_TYPE_CHOICES = (
    ('H', 'hosting'),
    ('A', 'annual'),
    ('S', 'semi-annual'),
    ('Q', 'quarterly'),
    ('AD', 'adverisement'),
)

STATUS_TYPE_CHOICES= (
    ('CF', 'Confirm'),
    ('CP', 'Completed'),
    ('PE', 'Pending'),
    ('CA', 'Cancelled'),
) 

# Create your models here.

TRANSACTION_TYPE_CHOICES= (
    ('PA', 'paiement'),
    ('SA', 'salaire '),
    ('CR', 'creance'),
    ('CH', 'charges'),   
    ('AL', 'allouer'),  
) 

class TransactionManager(models.Manager):
    def get_total(self):
        return Transaction.objects.all().aggregate(Sum('amount'))
    def get_total_payment(self):
        return Transaction.objects.filter(tr_type="PA").aggregate(Sum('amount'))
    def get_total_salaire(self):
        return Transaction.objects.filter(tr_type="SA").aggregate(Sum('amount'))
    def get_total_creance(self):
        return Transaction.objects.filter(tr_type="CR").aggregate(Sum('amount'))
    def get_total_charges(self):
        return Transaction.objects.filter(tr_type="CH").aggregate(Sum('amount'))
    def get_total_allouer(self):
        return Transaction.objects.filter(tr_type="AL").aggregate(Sum('amount'))
    def get_account_payment(self, account_id):
        return Transaction.objects.filter(tr_type="PA", account_id = account_id).aggregate(Sum('amount'))
    def get_account_salaire(self, account_id):
        return Transaction.objects.filter(tr_type="SA", account_id = account_id).aggregate(Sum('amount'))
    def get_account_creance(self, account_id):
        return Transaction.objects.filter(tr_type="CR", account_id = account_id).aggregate(Sum('amount'))
    def get_account_charges(self, account_id):
        return Transaction.objects.filter(tr_type="CH", account_id = account_id).aggregate(Sum('amount'))
    def get_account_allouer(self, account_id):
        return Transaction.objects.filter(tr_type="AL", account_id = account_id).aggregate(Sum('amount'))


# def get_projects_total_cost(self):
#         return Project.objects.all().aggregate(Sum('cost'))



class Project (models.Model): 
    name                    = models.CharField(max_length=254)
    company                 = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="client", related_name="projects") 
    # account   = models.ForeignKey(Account,on_delete=models.CASCADE, related_name="projects") 
    manager                 = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE) #####?????? 
    cost                    = models.DecimalField(max_digits=20 , decimal_places=0, default=0)
    started_date            = models.DateField(blank=True, null=True) 
    deadline                = models.DateField(blank=True, null=True) 
    project_type            = models.CharField(choices=PROJECT_TYPE_CHOICES, max_length=2, blank=True, null=True)
    contract                = models.CharField(choices=CONTRACT_TYPE_CHOICES, max_length=2, blank=True, null=True)
    contract_expiration     = models.DateField(blank=True, null=True) 
    status                  = models.CharField(choices=STATUS_TYPE_CHOICES, max_length=2, blank=True, null=True)
    description             = tinymce_models.HTMLField( blank=True, null=True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    @property
    def get_status_class(self):
        if self.status == "CF":
            return "badge-success"
        elif self.status == "CP":
            return "badge-info"
        elif self.status == "PE":
            return "badge-warning"
        else:
            return "badge-danger"
    
    def get_project_dettes(self):
        cost = self.cost
        transactions = self.transactions.aggregate(Sum('amount'))
        reste = self.cost - transactions['amount__sum']
        print('amount all trans', reste)
        return int(reste)
    
   
  

        # return Project.objects.all().aggregate(Sum('cost'))

class Transaction(models.Model): 
    # receiver     = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE, related_name="receiver")

    account     = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE) 
    project     = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE, related_name="transactions") 
    tr_type     = models.CharField(choices=TRANSACTION_TYPE_CHOICES, max_length=2, null=True, blank=True,)
    other       = models.CharField(max_length=254, blank=True, null=True)
    made_by     = models.ForeignKey(user, blank=True, null=True, on_delete=models.CASCADE, related_name="made_transactions") 
    amount      = models.DecimalField(max_digits=20 , decimal_places=0, blank=True, null=True)
    date        = models.DateField(blank=True, null=True)
    note        = models.CharField(max_length=254, blank=True, null=True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    objects     = models.Manager()
    payments    = TransactionManager()

    def __str__(self):
        return f"{self.project} - {self.tr_type}"


# class Task(models.Model):
#     project     = models.ForeignKey(Project,on_delete=models.CASCADE, related_name="tasks") 
#     manager     = models.ForeignKey(user,on_delete=models.SET_NULL, related_name="supervised_tasks", blank=True, null =True) 
#     status      = models.CharField(choices=STATUS_TYPE_CHOICES, max_length=2, blank=True, null=True)
#     description = tinymce_models.HTMLField( blank=True, null=True)

#     responsible = models.ForeignKey(user,on_delete=models.SET_NULL, related_name="attributed_tasks", blank=True, null =True) 
#     actif       = models.BooleanField()
#     created     = models.DateTimeField(auto_now_add=True)
#     updated     = models.DateTimeField(auto_now=True)
#     deadline    = models.DateField(blank=True, null=True) 
#     started_date= models.DateField(blank=True, null=True) 
