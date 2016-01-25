"""Phoneix URL Configuration

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

# local file imports.
import settings
from userprofile.views import HomePage, HospitalsListView, ClinicsListView, DgLabsPageView, \
    PharmacyListView, ContactPageView, HospitalPageView, UserLoginView, UserRegistrationView, \
    AboutUsPageView, TermsServicePageView, BlogPageView, ClinicsPageView, DgLabsListView, \
    PharmacyPageView, UserProfileView, UserGetListView

urlpatterns = [

    # Django backend admin app url(If you don't want comment it.).
    url(r'^admin/', include(admin.site.urls)),

    # Phoneix backend admin app url(If you don't want comment it.).
    url(r'^manage-', include('managebackend.urls')),

    # Logout url accessing django in-built logout functions.

    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}),

    # User Profile App Urls:

    url(r'^user-registration/$', UserRegistrationView.as_view(), name = 'user-registration'),
    url(r'^user-login/$', UserLoginView.as_view(), name = 'user-login'),
    url(r'^user-profile/$', UserProfileView.as_view(), name = 'user-profile'),

    url(r'^$', HomePage.as_view(), name = 'home-page'),

    url(r'^hospitals-list/$', HospitalsListView.as_view(), name = 'hospitals-list'),
    url(r'^hospital-page/(?P<slug>.*)/$', HospitalPageView.as_view(), name = 'hospital-page'),

    url(r'^clinics-list/$', ClinicsListView.as_view(), name = 'clinics-list'),
    url(r'^clinics-page/(?P<slug>.*)/$', ClinicsPageView.as_view(), name = 'clinics-page'),

    url(r'^dglabs-list/$', DgLabsListView.as_view(), name = 'dglabs-list'),
    url(r'^dglabs-page/(?P<slug>.*)/$', DgLabsPageView.as_view(), name = 'dglabs-page'),

    url(r'^pharmacy-list/$', PharmacyListView.as_view(), name = 'pharmacy-list'),
    url(r'^pharmacy-page/(?P<slug>.*)/$', PharmacyPageView.as_view(), name = 'pharmacy-page'),

    url(r'^get-user-list/$', UserGetListView.as_view(), name = 'get-user-list'),
    url(r'^about-us/$', AboutUsPageView.as_view(), name = 'about-us-page'),
    url(r'^terms-of-services/$', TermsServicePageView.as_view(), name = 'terms-of-page'),
    url(r'^blog/$', BlogPageView.as_view(), name = 'blog-page'),
    url(r'^contact-page/$', ContactPageView.as_view(), name = 'contact-page'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





