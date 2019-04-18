from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from .models import User
from .forms import UserForm


class CustomLogInView(LoginView):
    model = User
    template_name = 'profiles/login.html'


class IndexView(TemplateView):
    template_name = 'accounts/index.htm'


class Signup(CreateView):
    model = User
    form_class = UserForm
    template_name = 'profiles/signup.html'
    success_url = reverse_lazy('profiles:login')
