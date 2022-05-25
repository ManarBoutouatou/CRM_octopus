from django.db import models
from contact.models import Company, Employee
from tinymce import models as tinymce_models

# Create your models here.


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
    ('CO', 'confirm'),
    ('CP', 'completed'),
    ('PE', 'pending'),
) 
class Project (models.Model): 
    name                    = models.CharField(max_length=254, blank=True)
    company                 = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE) 
    manager                 = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE) 
    started_date            = models.DateField(blank=True, null=True) 
    deadline                = models.DateField(blank=True, null=True) 
    project_type            = models.CharField(choices=PROJECT_TYPE_CHOICES, max_length=2, blank=True, null=True)
    contract                = models.CharField(choices=CONTRACT_TYPE_CHOICES, max_length=2, blank=True, null=True)
    contract_expiration     = models.DateField(blank=True, null=True) 
    cost                    = models.DecimalField(max_digits=20 , decimal_places=0, blank=True, null=True)
    status                  = models.CharField(choices=STATUS_TYPE_CHOICES, max_length=2, blank=True, null=True)
    description             = tinymce_models.HTMLField( blank=True, null=True)
    def __str__(self):
        return self.name
  


