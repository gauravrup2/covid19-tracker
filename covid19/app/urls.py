from django import urls
from django.urls import path
from .views import home

urlpatterns = [
    path('', home),
]