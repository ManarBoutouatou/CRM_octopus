from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.db.models import Sum
# from dateutil.relativedelta import relativedelta
# from contact.models import Company 

from datetime import date, timedelta
ACCOUNT_TYPE= (
    ('IN', 'In'),
    ('OU', 'Out'),   
) 
class Account (models.Model): 
    # owner        = models.ManyToManyField(Project, related_name="project_name" )
    name                    = models.CharField(max_length=254)
    # campany     = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="accounts") 
    acc_type     = models.CharField(choices=ACCOUNT_TYPE, max_length=2, null=True)
    actif       = models.BooleanField()
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.name)



