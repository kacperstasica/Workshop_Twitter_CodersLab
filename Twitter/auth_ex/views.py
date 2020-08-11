from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from .forms import UserCreationForm


class UserCreateView(CreateView):
    model = get_user_model()
    form_class = UserCreationForm
    template_name = 'auth_ex/register.html'
    success_url = reverse_lazy(
        'auth_ex:register'
    )