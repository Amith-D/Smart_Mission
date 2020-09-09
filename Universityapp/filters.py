
import django_filters
from django_filters import CharFilter,NumberFilter
from .models import student_data


class searchForm(django_filters.FilterSet):
	University=CharFilter(field_name ='University',lookup_expr='icontains',label='University')
	First_Name=CharFilter(field_name ='First_Name',lookup_expr='icontains',label='First Name')
	Last_Name=CharFilter(field_name ='Last_Name',lookup_expr='icontains',label='Last Name')
	joinyear=NumberFilter(field_name ='joinyear',lookup_expr='icontains',label='Join Year')
	USN=CharFilter(field_name ='USN',lookup_expr='icontains',label='USN')
	
	class Meta:
		model = student_data
		fields = ['University','USN','First_Name','Last_Name','joinyear']
	