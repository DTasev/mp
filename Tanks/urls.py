"""Tanks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView, RedirectView
from tanks_utility.views import signup

urlpatterns = [
    # uncomment this if you want a redirection to the Tanks URL
    # path('', RedirectView.as_view(url='tanks/', permanent=True)),
    path('tanks/', TemplateView.as_view(template_name='index.html')),
    path('tanks/mc.html', TemplateView.as_view(template_name='mc.html')),
    path('tanks/', include('django.contrib.auth.urls')),
    path('tanks/api/', include('tanksapi.urls')),
    path('tanks/signup/', signup, name="signup"),
]
