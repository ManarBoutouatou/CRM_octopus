from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from django.urls.base import reverse_lazy
from .models import Company, Employee, Lead 
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from .forms import Company, AddCompanyForm, Employee, AddClientForm, Lead, AddLeadForm, AddLeadsForm
from .filters import CompanyFilter, Employeefilter, Leadfilter 
from pprint import pprint
from django.shortcuts import get_object_or_404
from project.models import Project 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib import messages
import logging
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
#COMPANY
class RedirectPermissionRequiredMixin(PermissionRequiredMixin,):
    login_url = reverse_lazy('core:index')
    def handle_no_permission(self):
        return redirect(self.get_login_url())

class CompanyListView(RedirectPermissionRequiredMixin, ListView): 
    template_name= "company_list.html"
    model = Company 
    permission_required= 'contact.view_company'
    
    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        # context["companies"] =Company.objects.all().order_by('collab_start')
        context["company_count"] =Company.objects.all().count()
        filters=CompanyFilter(self.request.GET, queryset=Company.objects.all().order_by('collab_start'))
        context["companies"] = filters.qs
        return context

class AddCompanyView(RedirectPermissionRequiredMixin,SuccessMessageMixin, CreateView):
    template_name= "company_add.html"
    form_class= AddCompanyForm
    model = Company 
    permission_required= 'contact.add_company'
    success_message = "Company added successfully."
    success_url = reverse_lazy('contact:companylist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
class CompanyUpdateView(RedirectPermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    model = Company
    form_class= AddCompanyForm
    template_name = 'company_edit.html' 
    permission_required= 'contact.change_company'
    success_message = "Company updated successfully."
    success_url = reverse_lazy('contact:companylist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
class CompanyDetailView(RedirectPermissionRequiredMixin, DetailView):
    model = Company
    template_name= "company_detail.html"
    permission_required= 'contact.view_company'
    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        company_id = self.get_object().id
        context["projects"] = Project.objects.all()
        context["company_projects"] = Project.objects.filter(company=company_id)
        context["employees"] = Employee.objects.all()
        context["company_employees"] = Employee.objects.filter(company=company_id)
        return context 
class CompanyDeleteView(RedirectPermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Company
    template_name= "company_delete.html"
    permission_required= 'company.delete_company'
    success_message = "Company deleted successfully."
    success_url = reverse_lazy('contact:companylist')
#CLIENT 
class ClientListView(RedirectPermissionRequiredMixin, ListView): 
    template_name= "client_list.html"
    model = Employee 
    permission_required= 'contact.view_employee'
    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        # context["employees"] =Employee.objects.all().order_by('collab_start')
        context["client_count"] =Employee.objects.all().count()
        filters=Employeefilter(self.request.GET, queryset=Employee.objects.all().order_by('collab_start'))
        context["employees"] = filters.qs
        return context
  
  
class  AddClientView(RedirectPermissionRequiredMixin, SuccessMessageMixin, CreateView):
    template_name= "client_add.html"
    form_class= AddClientForm
    model = Employee
    success_message = "Client added successfully."
    permission_required= 'contact.add_employee'
    success_url = reverse_lazy('contact:clientlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(AddClientView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        return context 

class ClientUpdateView(RedirectPermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Employee
    form_class= AddClientForm
    template_name = 'client_edit.html' 
    permission_required= 'contact.change_employee'
    success_message = "Client updated successfully."
    success_url = reverse_lazy('contact:clientlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(ClientUpdateView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        return context
class ClientDetailView(RedirectPermissionRequiredMixin, DetailView):
    model = Employee
    template_name= "client_detail.html"
    permission_required= 'contact.view_employee'
    def get_context_data(self, **kwargs):
        context = super(ClientDetailView, self).get_context_data(**kwargs)
        employee_id = self.get_object().id
        context["projects"] = Project.objects.all()
        context["client_projects"] = Project.objects.filter(manager=employee_id)
        return context

class ClientDeleteView(RedirectPermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Employee
    template_name= "client_delete.html"
    permission_required= 'client.delete_company'
    success_message = "Client deleted successfully."
    success_url = reverse_lazy('contact:clientlist')

#LEADS
class LeadListView(RedirectPermissionRequiredMixin,ListView): 
    template_name= "lead_list.html"
    model = Lead 
    permission_required= 'contact.view_lead'
    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        context["lead_count"] =Lead.objects.all().count()
        filters=Leadfilter(self.request.GET, queryset=Lead.objects.all().order_by('created'))
        context["leads"] = filters.qs
        return context

class LeadDetailView(RedirectPermissionRequiredMixin, DetailView):
    model = Lead
    template_name= "lead_detail.html"
    permission_required= 'contact.view_lead'

class  AddLeadView(RedirectPermissionRequiredMixin, SuccessMessageMixin, CreateView):
    template_name= "lead_add.html"
    form_class= AddLeadForm
    model = Lead
    success_message = "Lead added successfully."
    permission_required= 'contact.add_lead'
    success_url = reverse_lazy('contact:leadlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(AddLeadView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        return context

class LeadUpdateView(RedirectPermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name= "lead_edit.html"
    form_class= AddLeadForm
    model = Lead
    success_message = "Lead updated successfully."
    permission_required= 'contact.change_lead'
    success_url = reverse_lazy('contact:leadlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(LeadUpdateView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        return context
class LeadsUpdateView(RedirectPermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name= "lead_edit.html"
    form_class= AddLeadsForm
    model = Lead
    success_message = "Lead updated successfully."
    permission_required= 'contact.change_lead'
    success_url = reverse_lazy('core:index')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    


class LeadDeleteView(RedirectPermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Lead
    template_name= "lead_delete.html"
    permission_required= 'lead.delete_company'
    success_message = "Lead deleted successfully."
    success_url = reverse_lazy('contact:leadlist')


    

