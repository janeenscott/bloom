from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth import get_user_model, login, authenticate

from .models import Rental


User = get_user_model()


class HomeView(TemplateView):

    template_name = 'bloom/list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            ctx['equipment'] = Rental.objects.filter(user=self.request.user)

        return ctx


# # Create your views here.

class CreateView(TemplateView):

    template_name = 'bloom/create.html'

    def post(self, request, *args, **kwargs):
        item = self.request.POST.get('item')
        price = self.request.POST.get('price')

        rental = Rental(item=item, price=price)
        rental.user = self.request.user
        rental.save()


        return HttpResponseRedirect(reverse('bloom:create'))
        # bloom:index is referring to the url route "index" in the bloom app

class UsersInSystemView(ListView):
    template_name = 'bloom/users.html'
    model = User
    # User model is built into django auth


# class UserEquipmentList(TemplateView):
#     template_name = 'bloom/user_equipment.html'
#
#     def get_context_data(self, **kwargs):
#         ctx = super().get_context_data(**kwargs)
#
#         equipment_id = self.kwargs.get('pk')
#
#         ctx['rental'] =Rental.objects.get(pk=equipment_id)
#
#
#
#         return ctx
#
class UserEquipmentList(ListView):
    template_name = 'bloom/user_equipment.html'
    model = Rental

    def get_queryset(self, **kwargs):

        query_set = super().get_queryset(**kwargs)
        user_id = self.kwargs.get('pk', **kwargs)

        query_set = query_set.filter(user_id=user_id)

        return query_set



