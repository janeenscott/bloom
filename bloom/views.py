from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model, login, authenticate

from .models import Equipment