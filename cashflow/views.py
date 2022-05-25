from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from django.urls.base import reverse_lazy

from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView, 
    FormView
)
from django.views.generic.edit import CreateView
from pprint import pprint
from contact.models import Company, Employee
from cashflow.models import Transaction, Account
from project.models import Project
from .filters import Accountfilter, Transactionfilter
from .forms import AddAccountForm, AddTransactionForm
# Create your views here.

#cashflow
class CashflowListView(ListView): 
    template_name= "cashflow_list.html"
    model = Transaction 
    def get_context_data(self, **kwargs):
        context = super(CashflowListView, self).get_context_data(**kwargs)
        # context["transactions"] =Transaction.objects.all().order_by('date')
        filters=Transactionfilter(self.request.GET, queryset=Transaction.objects.all())
        context["transactions"] = filters.qs
        context["total_payment"] =Transaction.payments.get_total_payment()
        context["total_charges"] =Transaction.payments.get_total_charges()
        context["total_creance"] =Transaction.payments.get_total_creance()
        context["total_salaire"] =Transaction.payments.get_total_salaire()    
        context["total_allouer"] =Transaction.payments.get_total_allouer()  
        return context
    
class CashflowAccountListView(ListView): 
    template_name= "account_list.html"
    model = Account 
    def get_context_data(self, **kwargs):
        context = super(CashflowAccountListView, self).get_context_data(**kwargs)
        context["account_count"] =Account.objects.all().count()
        # context["projects"] = Project.objects.filter(project_name__id=owner).distinct()
        # context["projects"] = Project.objects.filter('project_name')
        context["projects"] = Project.objects.all()
        filters=Accountfilter(self.request.GET, queryset=Account.objects.all())
        context["accounts"] = filters.qs
        return context

class AccountDetailView(DetailView):
    model = Account
    template_name= "cashflowaccount-detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account_id = self.get_object().id
        context["accounts"] =Account.objects.all()
        context["transactions"] =Transaction.objects.all()   
        context["account_payment"] =Transaction.payments.get_account_payment(account_id)
        context["account_charges"] =Transaction.payments.get_account_charges(account_id)
        context["account_creance"] =Transaction.payments.get_account_creance(account_id)
        context["account_salaire"] =Transaction.payments.get_account_salaire(account_id) 
        context["account_allouer"] =Transaction.payments.get_account_allouer(account_id)        
        context['payments'] = Transaction.objects.filter(account=account_id)     
        return context
        
class AddAccountView(CreateView):
    template_name= "add-accounts.html"
    form_class= AddAccountForm
    model = Account
    success_url = reverse_lazy('cashflow:accountlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(AddAccountView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        return context
   
class AddTransactionView(CreateView):
    template_name= "add-transaction.html"
    form_class= AddTransactionForm
    model = Transaction
    success_url = reverse_lazy('cashflow:cashflowlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(AddAccountView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        return context