from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView, DetailView
from profileacc.forms import ProfileRegForm
from django import forms


class DashboardView(LoginRequiredMixin, DetailView):
    template_name = 'profileacc/dashboard.html'

    def get_object(self):
        return self.request.user


class RegisterView2(CreateView):
    form_class  = ProfileRegForm
    success_url = '/login'
    template_name = "profileacc/register2.html"
