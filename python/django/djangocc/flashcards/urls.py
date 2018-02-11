#flachcards url
from django.urls import path

from . import views

app_name="flashcards"

urlpatterns = [
    path(r'', views.home, name='home'),
]