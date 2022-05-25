import django_filters 
from django_filters import DateFilter
from .models import Account, Transaction


class Accountfilter(django_filters.FilterSet): 
    class Meta:
        model = Account
        fields = ['owner', 'type', 'created']
    
    def filter_by_type(self, queryset, name, value): 
        expresssion = 'created' if value =='ascending' else '-created'
        return queryset.order_by(expresssion)
    def filter_by_owner(self, queryset, name, value): 
        expresssion = 'created' if value =='ascending' else '-created'
        return queryset.order_by(expresssion)


class Transactionfilter(django_filters.FilterSet): 
    class Meta:
        model = Transaction
        fields = ['account', 'type', 'date']
    
    def filter_by_type(self, queryset, name, value): 
        expresssion = 'date' if value =='ascending' else '-date'
        return queryset.order_by(expresssion)
    def filter_by_account(self, queryset, name, value): 
        expresssion = 'date' if value =='ascending' else '-date'
        return queryset.order_by(expresssion)
