from django import forms
from django.forms import ModelForm, widgets
from django.contrib.admin.widgets import AdminDateWidget
from .models import Project, Transaction

class AddProjectForm(ModelForm) :
    class Meta: 
        model = Project
        fields = '__all__' 
     
class AddTransactionForm(ModelForm) :
    class Meta: 
        model = Transaction
        fields = '__all__' 