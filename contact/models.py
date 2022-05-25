from email.policy import default
from re import T
from django.db import models
from django.urls import reverse 
from tinymce import models as tinymce_models


# Create your models here.

# contact 
COMPANY_TYPE_CHOICES = (
    ('CL', 'client'),
    ('F', 'fournisseur'),
    ('P', 'partenaire'),
    ('CN', 'concurrent'),

)
PROJECT_TYPE_CHOICES = (
    ('EC', 'e-commerce'),
    ('WS', 'web site'),
    ('WA', 'web app'),
)

class Company(models.Model):
    name                = models.CharField(max_length=250)
    industry            = models.CharField(max_length=100, blank=True, null=True)
    annual_revenue      = models.DecimalField(max_digits=20 , decimal_places=0, blank=True, null=True)
    email               = models.EmailField(max_length=254,  blank=True, null=True)
    mobile              = models.CharField(max_length=13,  blank=True, null=True)
    website             = models.URLField(max_length=250, blank=True, null=True)
    adress              = models.CharField(max_length=250,  blank=True, null=True)
    rc_code             = models.CharField( max_length=150, null=True, blank=True)
    art_code            = models.CharField(max_length=150, null=True, blank=True)
    nif_code            = models.CharField( max_length=150, null=True, blank=True)
    nis_code            = models.CharField( max_length=150, null=True, blank=True)
    responsible_person  = models.CharField(max_length=100,  blank=True, null=True)
    source              = models.CharField(max_length=250, blank=True, null=True)
    company_type        = models.CharField(choices=COMPANY_TYPE_CHOICES, max_length=2, blank=True, null=True)
    project_type        = models.CharField(choices=PROJECT_TYPE_CHOICES, max_length=2, blank=True, null=True)
    logo                = models.ImageField(upload_to='companies/', null=True, blank=True)  
    collab_start        = models.DateField(blank=True, null=True)
    created             = models.DateField(auto_now=True)
    updated             = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("contact:companydetail", kwargs={"pk": self.pk})

   
DECISION_TYPE_CHOICES= (
    ('1', '*'),
    ('2', '**'),
    ('3', '***'),
    ('4', '****'),
    ('5', '*****'),
)


class Employee(models.Model):
    name         = models.CharField(max_length=254)
    company      = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE) 
    decision     = models.CharField(choices=DECISION_TYPE_CHOICES, max_length=2, blank=True, null=True)
    mobile       = models.CharField(max_length=13, blank=True, null=True)
    email        = models.EmailField(max_length=254, blank=True, null=True) 
    address      = models.CharField(max_length=250, blank=True, null=True)
    source       = models.CharField( max_length=250, blank=True, null=True)
    project_type = models.CharField(choices=PROJECT_TYPE_CHOICES, max_length=2, blank=True, null=True)
    collab_start = models.DateField(blank=True, null=True)
    created      = models.DateField(auto_now=True)
    updated      = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("contact:clientdetail", kwargs={"pk": self.pk})

STATUS_TYPE_CHOICES= (
    ('I', 'inrested'),
    ('CA', 'call again'),
    ('NI', 'not intrested'), 
) 


class Lead(models.Model):
    company      = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True)
    source       = models.CharField( max_length=250, blank=True, null=True)
    project_type = models.CharField(choices=PROJECT_TYPE_CHOICES, max_length=2, blank=True, null=True)
    status       = models.CharField(choices=STATUS_TYPE_CHOICES, max_length=2, blank=True, null=True)
    note         = tinymce_models.HTMLField( blank=True, null=True)
    created      = models.DateField(auto_now=True)
    updated      = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.company)
    def get_absolute_url(self):
        return reverse("contact:leaddetail", kwargs={"pk": self.pk})
    
   

    
