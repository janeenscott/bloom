from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model, login, authenticate

from .models import Bloom


User = get_user_model()


class HomeView(TemplateView):

    template_name = 'bloom/list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            ctx['equipment'] = Bloom.objects.filter(user=self.request.user)

        return ctx


# # Create your views here.
class CreateView(TemplateView):

    template_name = 'bloom/create.html'

    def post(self, request, *args, **kwargs):
        item = self.request.POST.get('item')
        price = self.request.POST.get('price')

        equipment = Bloom(item=item, price=price)
        equipment.user = self.request.user
        equipment.save()

        return HttpResponseRedirect(reverse('bloom:index'))
