from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    # we use reverse_lazy instead of reverse because we need to wait
    #     until the forms are set up properly
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
