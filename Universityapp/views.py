from django.shortcuts import get_object_or_404,render
from .filters import searchForm
from .models import student_data
from django.core.paginator import Paginator
import pandas as pd
import numpy as np

# Create your views here.
def studsearch(request):
	studdata = student_data.objects.get_queryset().order_by('id')
	myFilter = searchForm(request.GET, queryset=studdata)
	studdata = myFilter.qs
	paginator = Paginator(studdata,35)
	page = request.GET.get('page')
	studdata = paginator.get_page(page)
	return render(request,'basic_app/search.html',{'all_data':studdata,'myFilter':myFilter})


def details_stu(request,id):
	data = get_object_or_404(student_data,pk=id)
	return render(request,'basic_app/details.html',{'data': data })