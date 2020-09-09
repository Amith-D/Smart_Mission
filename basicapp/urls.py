from django.urls import path
from basicapp import views
app_name = 'basicapp'

urlpatterns =[
    path('index/',views.index, name='index'),
    path('formpage/',views.AdmitStudent_view, name='formpage'),
    path('dash/',views.dash,name='dash'),
    path('result/<id>',views.result,name='result'),
    path('action/<id>',views.del_stu_data,name='delete'),
]