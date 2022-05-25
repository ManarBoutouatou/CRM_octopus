from django.urls import path
from . import views 
from .views import  CompanyListView, AddCompanyView, CompanyUpdateView, CompanyDetailView, CompanyDeleteView
from .views import  ClientListView, AddClientView, ClientUpdateView, ClientDetailView, ClientDeleteView
from .views import  LeadListView, AddLeadView, LeadUpdateView, LeadDetailView, LeadDeleteView, LeadsUpdateView
from django.contrib.auth.decorators import login_required, permission_required
app_name= 'contact'

urlpatterns = [
  
   #company
  
   path('companylist', login_required(CompanyListView.as_view()), name='companylist'),
   path('addcompany', login_required(AddCompanyView.as_view()), name="addcompany"),
   path('editcompany/<int:pk>/', login_required(CompanyUpdateView.as_view()), name="editcompany"),
   path('companydetail/<int:pk>/', login_required(CompanyDetailView.as_view()), name="companydetail"),
   path('companydelete/<int:pk>/', login_required(CompanyDeleteView.as_view()), name="companydelete"),
  
  #CLIENT
   path('clientlist', login_required(ClientListView.as_view()), name='clientlist'),
   path('addclient', login_required(AddClientView.as_view()), name="addclient"),
   path('editclient/<int:pk>/', login_required(ClientUpdateView.as_view()), name="editclient"),
   path('clientdetail/<int:pk>/', login_required(ClientDetailView.as_view()), name="clientdetail"),
   path('clientdelete/<int:pk>/', login_required(ClientDeleteView.as_view()), name="clientdelete"),

   #LEADS
   path('leadlist', login_required(LeadListView.as_view()), name='leadlist'),
   path('addlead',  login_required(AddLeadView.as_view()), name="addlead"),
   path('editlead/<int:pk>/', login_required(LeadUpdateView.as_view()), name="editlead"),
   path('editleads/<int:pk>/', login_required(LeadsUpdateView.as_view()), name="editleads"),
   path('leaddetail/<int:pk>/', login_required(LeadDetailView.as_view()), name="leaddetail"),
   path('leaddelete/<int:pk>/', login_required(LeadDeleteView.as_view()), name="leaddelete"),
 

]




