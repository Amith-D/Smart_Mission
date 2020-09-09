from django.urls import path
from Universityapp import views
app_name = 'Universityapp'

urlpatterns =[
    path('studsearch/',views.studsearch,name='Search'),
    path('details/<int:id>',views.details_stu,name='details'),

]