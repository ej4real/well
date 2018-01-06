from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, FormView, DetailView
from now.mixins import NextUrlMixin, RequestFormAttachMixin
from .urls import url
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect

class RegisterView(CreateView):
    form_class  = forms.RegisterForm
    success_url = '/login'
    template_name = "accounts/signup.html"

    def some_view(request):
        if request.method == 'POST':
            form1 = RegisterForm(request.POST, prefix='form1')
            form2 = ProfileRegForm(request.POST, prefix='form2')
            if all([form1.is_valid(), form2.is_valid()]):
                pass # Do stuff with the forms
        else:
            form1 = GeneralForm(prefix='form1')
            form2 = GeneralForm(prefix='form2')
        return render_to_response('/accounts/signup.html', {
            'form1': form1,
            'form2': form2,
        })


class LoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
    form_class = forms.LoginForm
    success_url = '/'
    template_name = 'accounts/login.html'
    default_next = '/'

    def form_valid(self, form):
        next_path = self.get_next_url()
        return redirect(next_path)

class AccountHomeView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/home.html'
    def get_object(self):
        return self.request.user
