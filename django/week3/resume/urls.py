from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
   url(r'', views.home, name='home'),
]