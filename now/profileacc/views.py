from django.contrib.auth import authenticate, login, get_user_model
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView, DetailView, UpdateView
from profileacc.forms import ProfileDetailChangeForm
from django.db.models.signals import pre_save, post_save
from django import forms




class DashboardView(LoginRequiredMixin, DetailView):
    template_name = 'profileacc/dashboard.html'

    def get_object(self):
        return self.request.user

    def get_docprofile(self):
        return self.request.user.docprofile

    def get_patientprofile(self):
        return self.request.user.patientprofile

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileDetailChangeForm
    template_name = 'profileacc/detail-update-view.html'
    success_url = '/'

    def get_object(self):
        return self.request.user.docprofile

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Your Profile Details'
        return context

#class RegisterView2(FormView):
#    form_class  = ProfileRegForm
#    success_url = '/login'
#    template_name = "profileacc/register2.html"

#    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
#        form.save()
#        return super().form_valid(form)
