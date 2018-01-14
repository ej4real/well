from django.conf.urls import url
#from django.contrib.auth import views as auth_views
from patient.views import PatProfileUpdateView, PatDashboardView, PatRegView

app_name = 'patient'

urlpatterns = [
        url(r"patdash/$", PatDashboardView.as_view(),name='pdash'),
        url(r"patupdate/$", PatProfileUpdateView.as_view(),name='pupdate'),
        url(r"addpatient/$", PatRegView.as_view(),name='pregister'),
]
