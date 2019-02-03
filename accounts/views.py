from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model, login, authenticate



class SignupView(TemplateView):
    template_name = 'accounts/signup.html'

    def post(self, request, *args, **kwargs):

        #sign up user

        first_name = self.request.POST.get('first_name')

        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        password2= self.request.POST.get('password2')

        if password != password2:
            return HttpResponseRedirect(reverse('accounts:signup'))
        if password != password2:
            return HttpResponseRedirect(reverse('accounts:signup'))

        # If the username already exists, send the user back
        user = User.objects.filter(username=username)
        if user.count() > 0:
            return HttpResponseRedirect(reverse('accounts:signup'))

        # save user database record using fancy hashing on password
        User.objects.create_user(username=username, password=password)

        # Authenticate the user checks provided password against the hash
        user = authenticate(username=username, password=password)

        # Login the user (does the session table/cookie stuff)
        login(self.request, user)

        return HttpResponseRedirect(reverse('accounts:index'))
