from django.urls import path
from . import views

urlpatterns = [
    path('', views.sca_list, name='sca_list')
]