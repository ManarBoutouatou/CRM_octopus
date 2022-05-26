from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, request
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
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from contact.models import Company, Employee
from .models import Transaction, Project
from .forms import AddProjectForm, AddTransactionForm
from .filters import ProjectFilter

import logging
from pprint import pprint

# Create your views here.
class RedirectPermissionRequiredMixin(PermissionRequiredMixin,):
    login_url = reverse_lazy('core:index')
    def handle_no_permission(self):
        return redirect(self.get_login_url())

class CashflowListView(ListView): 
    template_name= "cashflow_list.html"
    model = Transaction 
    def get_context_data(self, **kwargs):
        context = super(CashflowListView, self).get_context_data(**kwargs)
        # context["transactions"] =Transaction.objects.all().order_by('date')
        # filters=Transactionfilter(self.request.GET, queryset=Transaction.objects.all())
        # context["transactions"] = filters.qs
        context["total_payment"] =Transaction.payments.get_total_payment()
        context["total_charges"] =Transaction.payments.get_total_charges()
        context["total_creance"] =Transaction.payments.get_total_creance()
        context["total_salaire"] =Transaction.payments.get_total_salaire()    
        context["total_allouer"] =Transaction.payments.get_total_allouer()  
        return context
#project    
class ProjectListView(RedirectPermissionRequiredMixin,ListView): 
    template_name= "project_list.html"
    model = Project 
    permission_required= 'project.view_project'
    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        # context["projects"] =Project.objects.all().order_by('active')
        context["project_count"] =Project.objects.all().count()
        filters=ProjectFilter(self.request.GET, queryset=Project.objects.all())
        context["projects"] = filters.qs
        return context
    
class ProjectDetailView(RedirectPermissionRequiredMixin,DetailView):
    model = Project
    template_name= "project_detail.html"
    permission_required= 'project.view_project'
  
        
class AddProjectView(RedirectPermissionRequiredMixin,SuccessMessageMixin, CreateView):
    template_name= "project_add.html"
    form_class= AddProjectForm
    model = Project
    success_message = "Project added successfully."
    permission_required= 'project.add_project'
    success_url = reverse_lazy('project:projectlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(AddProjectView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        context["employees"] = Employee.objects.all()
        return context
   
 
class ProjectUpdateView(RedirectPermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    model = Project
    form_class= AddProjectForm
    template_name = 'project_edit.html' 
    success_message = "Project updated successfully."
    permission_required= 'project.change_project'
    success_url = reverse_lazy('project:projectlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(ProjectUpdateView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        context["employees"] = Employee.objects.all()
        return context
   

class ProjectDeleteView(RedirectPermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    model = Project
    template_name= "project_delete.html"
    success_message = "Product deleted successfully."
    permission_required= 'project.delete_project'
    success_url = reverse_lazy('project:projectlist')


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