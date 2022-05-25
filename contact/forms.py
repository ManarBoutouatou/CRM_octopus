from django import forms
from django.forms import ModelForm
from .models import Company, Employee, Lead


class AddCompanyForm(ModelForm) :
    class Meta: 
        model = Company 
        fields = '__all__' 
        
class AddClientForm(ModelForm) :
    class Meta: 
        model = Employee 
        fields = '__all__' 


class AddLeadForm(ModelForm) :
    class Meta: 
        model = Lead
        fields = '__all__' 


class AddLeadsForm(ModelForm) :
    class Meta: 
        model = Lead
        fields =  ('status',)