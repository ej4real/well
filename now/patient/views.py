from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView, DetailView, UpdateView, DeleteView
from patient.forms import PatProfileDetailChangeForm, RegPatientForm
from django.db.models.signals import pre_save, post_save
from django import forms
# Create your views here.

class PatProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PatProfileDetailChangeForm
    template_name = 'patient/detail-update-view.html'
    success_url = 'patupdate'

    def get_object(self):
        return self.request.user.patientprofile

    def get_context_data(self, *args, **kwargs):
        context = super(PatProfileUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Profile Details'
        return context

class PatRegView(LoginRequiredMixin, CreateView):
    form_class = RegPatientForm
    template_name = 'patient/regpatient.html'
    success_url = 'addpatient/'

    def get_context_data(self, *args, **kwargs):
        context = super(PatRegView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create Patient Profile'
        return context


class PatDashboardView(LoginRequiredMixin, DetailView):
    template_name = 'patient/patdash.html'

    def get_patientprofile(self):
        return self.request.user.patientprofile

class PatDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'patient/patdelete.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PatRegView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Delete Patient Profile'
        return context
