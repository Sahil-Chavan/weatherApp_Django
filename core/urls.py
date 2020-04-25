from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
path('home',views.home,name="weather-home"),
path('logout',views.logout,name="weather-logout")
]