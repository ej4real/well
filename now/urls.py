"""now URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static


from . import views
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LogoutView
from accounts.views import LoginView, RegisterView
from django.views.generic import TemplateView, RedirectView

from django.contrib.auth import views as auth_views
from profileacc.urls import urlpatterns
from patient.urls import urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", views.HomePage.as_view(), name="home"),
    #url(r"^test/$", views.TestPage.as_view(), name="test"),
    #url(r"^thanks/$", views.ThanksPage.as_view(), name="thanks"),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r"register/$", RegisterView.as_view(), name="register"),
    url(r'^accounts/$', RedirectView.as_view(url='/')),
    url(r"logout/$", auth_views.LogoutView.as_view(),name='logout'),
    url(r"^profileacc/", include("profileacc.urls", namespace="profileacc")),
    url(r"^patient/", include("patient.urls", namespace="patient")),

]
