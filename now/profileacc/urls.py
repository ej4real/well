from django.conf.urls import url
#from django.contrib.auth import views as auth_views
from profileacc.views import DashboardView, ProfileUpdateView

app_name = 'profileacc'

urlpatterns = [

        url(r"dashboard/$", DashboardView.as_view(),name='dash'),
        url(r"update/$", ProfileUpdateView.as_view(),name='update'),

]
