from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, FormView, DetailView, TemplateView
from now.mixins import NextUrlMixin, RequestFormAttachMixin
from .urls import url
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect



#class RegisterView(CreateView):
#    form_class  = forms.RegisterForm
#    success_url = '/login'
#    template_name = "accounts/signup.html"


class LoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
    form_class = forms.LoginForm
    success_url = '/profileacc/update'
    template_name = 'accounts/login.html'
    default_next = '/profileacc/update'

    def form_valid(self, form):
        next_path = self.get_next_url()
        return redirect(next_path)

#class AccountHomeView(LoginRequiredMixin, DetailView):
#    template_name = 'accounts/home.html'
#    def get_object(self):
#        return self.request.user


class RegisterView(CreateView):
    form_class  = forms.RegisterForm
    success_url = '/login'
    template_name = "accounts/signup.html"

#    def get_context_data(self, **kwargs):
#        context = super(RegisterView, self).get_context_data(**kwargs)
#        context['modelone'] = User.objects.get(username=request.user.username)
##        return context
