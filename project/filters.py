import django_filters 
from django_filters import DateFilter
from .models import Project

class ProjectFilter(django_filters.FilterSet) :
    class Meta: 
        model = Project
        fields = ['name', 'project_type']
    
    def filter_by_project_type(self, queryset, name, value): 
        expresssion = 'active' if value =='ascending' else '-active'
        return queryset.order_by(expresssion)

# class Transactionfilter(django_filters.FilterSet): 
#     class Meta:
#         model = Transaction
#         fields = ['account', 'type', 'date']

#     def filter_by_type(self, queryset, name, value): 
#         expresssion = 'date' if value =='ascending' else '-date'
#         return queryset.order_by(expresssion)
#     def filter_by_account(self, queryset, name, value): 
#         expresssion = 'date' if value =='ascending' else '-date'
#         return queryset.order_by(expresssion)
