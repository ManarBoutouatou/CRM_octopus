from django.urls import path
from . import views 
from cashflow.views import CashflowListView, CashflowAccountListView, AccountDetailView, AddAccountView, AddTransactionView
from django.contrib.auth.decorators import login_required, permission_required
app_name= 'cashflow'
urlpatterns = [  
   #cashflow
   path('cashflowlist', login_required(CashflowListView.as_view()), name='cashflowlist'),
   
   path('accountlist', login_required(CashflowAccountListView.as_view()), name='accountlist'),
   path('accounttdetail/<int:pk>/', login_required(AccountDetailView.as_view()), name="accounttdetail"),
   path('addaccounts', login_required(AddAccountView.as_view()), name="addaccounts"),
   path('addtransaction', login_required(AddTransactionView.as_view()), name="addtransaction"),
]




