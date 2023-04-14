from django.contrib import admin
from django.urls import path
from .views import *
from frontend import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    
    path('', views.home, name="home"),
    

]


