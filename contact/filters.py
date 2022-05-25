import django_filters 
from django_filters import DateFilter
from .models import Company, Employee, Lead


class CompanyFilter(django_filters.FilterSet): 
    PROJECT_TYPE_CHOICES = (
    ('EC', 'e-commerce'),
    ('WS', 'web site'),
    ('WA', 'web app'),
    )
    class Meta:
        model = Company
        fields = ['name', 'project_type', 'collab_start']
    
    def filter_by_project_type(self, queryset, name, value): 
        expresssion = 'active' if value =='ascending' else '-active'
        return queryset.order_by(expresssion)


class Employeefilter(django_filters.FilterSet): 
    PROJECT_TYPE_CHOICES = (
    ('EC', 'e-commerce'),
    ('WS', 'web site'),
    ('WA', 'web app'),
    )
    class Meta:
        model = Employee
        fields = ['name', 'project_type', 'collab_start']
    
    def filter_by_project_type(self, queryset, name, value): 
        expresssion = 'active' if value =='ascending' else '-active'
        return queryset.order_by(expresssion)
    
class Leadfilter(django_filters.FilterSet): 
    
    STATUS_TYPE_CHOICES= (
        ('I', 'inrested'),
        ('CA', 'call again'),
        ('NI', 'not intrested'),    
    ) 
    class Meta:
        model = Lead
        fields = '__all__'
    
