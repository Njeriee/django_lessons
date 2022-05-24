from django import views
from django.contrib import admin
from django.urls import path
from . import views

# mapping the urls 
urlpatterns = [
    path('', views.index, name = 'index'),
]