"""messageDel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from messDel import views
from messDel.views import userProfile
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.userLogin, name="login"),
    re_path(r'^emailauth/(?P<auth>[0-9a-zA-Z]{56})/$', views.emailAuth , name="emailAuth"),
    re_path(r'^wrongEmail/(?P<auth>[0-9a-zA-Z]{56})/$', views.wrongEmail , name="wrongEmail"),
    re_path(r'^userProfile/(?P<auth>[0-9a-zA-Z]{56})/$', views.userProfile, name="userAuth"),
    path('accounts/', include('allauth.urls')),	
    url(r'chat.html/' , views.googleRedirect, name="googleRedirect")
]
