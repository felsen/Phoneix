"""Phoneix Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

# django imports.
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

# Manage backend module Imports:
from Phoneix import settings
from managebackend.views import ManageLoginView, ManageHomeView, ManageVisitorsView, \
    ManageDoctorsView, ManageHospitalsView, ManageClinicView, ManageDignosticView, \
    ManagePharmacyView


urlpatterns = [

    # Admin backend login & logout function:
    url(r'login/$', ManageLoginView.as_view(), name = 'admin-login'),
    url(r'logout/$', 'django.contrib.auth.views.logout', {'next_page':'/manage-login/'}),

    url(r'home/$', ManageHomeView.as_view(), name = "admin-home"),
    url(r'visitors/$', ManageVisitorsView.as_view(), name = "admin-visitors"),
    url(r'doctors/$', ManageDoctorsView.as_view(), name = "admin-doctors"),
    url(r'hospitals/$', ManageHospitalsView.as_view(), name = "admin-hospitals"),
    url(r'clinic/$', ManageClinicView.as_view(), name = "admin-clinic"),
    url(r'dignostic/$', ManageDignosticView.as_view(), name = "admin-dignostic"),
    url(r'pharmacy/$', ManagePharmacyView.as_view(), name = "admin-pharmacy"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
