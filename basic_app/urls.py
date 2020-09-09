from django.conf.urls import url,include
from basic_app import views
from django.urls import path
app_name = 'basic_app'

urlpatterns =[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name= 'user_login'),
    url(r'^menu/$',views.dean_login,name= 'menu'),
    url(r'^form_fill/$',views.form_fill,name= 'form_fill'),
    url(r'^archive/$',views.archive,name= 'archive'),
    url(r'^search/$',views.search,name= 'search'),
    path('',views.home,name='home'),
    path('contact/',views.contact,name = 'contact'),
    path('about/',views.about,name='about'),
]
