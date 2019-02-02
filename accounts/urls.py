"""
accounts app urls
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('users/')
]