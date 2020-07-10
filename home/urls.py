from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.homepage, name='home'),
    path(r'get_province', views.get_province_information, name='get-province')
]