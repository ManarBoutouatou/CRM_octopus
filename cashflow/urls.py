from django.urls import path
from . import views 
from cashflow.views import (
   CashflowAccountListView, 
   AccountDetailView, 
   AddAccountView, 
   CashflowListView,
)
from django.contrib.auth.decorators import login_required, permission_required
app_name= 'cashflow'
urlpatterns = [  
   #cashflow
   
   path('accountlist', login_required(CashflowAccountListView.as_view()), name='accountlist'),
   path('accounttdetail/<int:pk>/', login_required(AccountDetailView.as_view()), name="accounttdetail"),
   path('addaccounts', login_required(AddAccountView.as_view()), name="addaccounts"),

   path('cashflowlist', login_required(CashflowListView.as_view()), name='cashflowlist'),

]




