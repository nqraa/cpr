from django.urls import path, re_path , include
from .import views
from django.conf.urls  import url


app_name = 'crp'

urlpatterns = [
    # url('^$' , views.Create, name='create'),
    # url('cpt.html/^$' , views.create, name='create'),
    path('',views.create),
    path('', views.index, name='home'),
    re_path(r'^.*\.*', views.pages, name='pages'),
]