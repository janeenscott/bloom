from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views

app_name = 'bloom'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('create/', views.CreateView.as_view(), name='create'),

]