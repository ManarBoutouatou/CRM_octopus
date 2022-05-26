from django import forms
from django.forms import ModelForm, widgets
from django.contrib.admin.widgets import AdminDateWidget
from .models import  Account

class AddAccountForm(ModelForm) :
    class Meta: 
        model = Account
        fields = '__all__' 
    
