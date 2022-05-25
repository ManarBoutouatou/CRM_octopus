import django_filters 
from django_filters import DateFilter
from .models import Event


class Eventsfilter(django_filters.FilterSet): 
    class Meta:
        model = Event
        fields = '__all__' 
    
    # def filter_by_project_type(self, queryset, name, value): 
    #     expresssion = 'active' if value =='ascending' else '-active'
    #     return queryset.order_by(expresssion)


