from django.conf.urls import url
#from django.contrib.auth import views as auth_views
from profileacc.views import DashboardView, RegisterView2

app_name = 'profileacc'

urlpatterns = [

        url(r"dashboard/$", DashboardView.as_view(),name='dash'),
        url(r"register2/$", RegisterView2.as_view(),name='register2'),

]
