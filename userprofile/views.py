# From Django Module Imports:
from django.shortcuts import render, render_to_response
from django.views.generic.base import TemplateView
from django.contrib.auth import login as auth_login, authenticate, get_user
from django.http import HttpResponseRedirect
from django.views.generic import FormView, View, CreateView, ListView, DetailView
from django.contrib.auth.models import User

# From Third Party Package Imports:
import json

# From Current Project Module Imports:
from userprofile.forms import UserLoginForm, UserRegisterForm, UserGetListForm
from userprofile.models import UserGetList
from hospitalinfo.models import HospitalInfo, ClinicInfo, DgLabsInfo, PharmacyInfo


class UserLoginView(FormView):

    """ CBV for user login """

    template_name = "user_login.html"
    success_url = "/"
    form_class = UserLoginForm
    user_error = "username or password incorrect."

    def form_valid(self, form):
        user = authenticate(username=self.request.POST.get('username'), \
                            password = self.request.POST.get('password'))
        if user is not None:
            auth_login(self.request, user)
            return super(UserLoginView, self).form_valid(form)
        return render(self.request, self.template_name, {
            'form':form, 'user_error':self.user_error
        })

class UserRegistrationView(FormView):

    """ CBV for user register """

    template_name = "user_register.html"
    form_class = UserRegisterForm
    success_url = "/"

    def form_valid(self, form):
        User.objects.create_user(username = self.request.POST.get('username'), \
            email = self.request.POST.get('email'), password = self.request.POST.get('password'))
        return super(UserRegistrationView, self).form_valid(form)

class UserGetListView(CreateView):

    form_class = UserGetListForm
    template_name = 'get_userlist.html'
    success_url = "/"

class HomePage(TemplateView):

    template_name = 'index.html'

class HospitalsListView(ListView):

    model = HospitalInfo
    template_name = 'hospitals.html'

class ClinicsListView(ListView):

    model = ClinicInfo
    template_name = 'clinics.html'

class ClinicsPageView(DetailView):

    model = ClinicInfo
    template_name = 'clinic_page.html'

class DgLabsListView(ListView):

    model = DgLabsInfo
    template_name = 'dglabs.html'

class DgLabsPageView(DetailView):

    model = DgLabsInfo
    template_name = 'dglab_page.html'

class PharmacyListView(ListView):

    model = PharmacyInfo
    template_name = 'pharmacy.html'

class PharmacyPageView(DetailView):

    model = PharmacyInfo
    template_name = 'pharmacy_page.html'

class ContactPageView(TemplateView):

    template_name = 'contact.html'

class HospitalPageView(DetailView):

    model = HospitalInfo
    template_name = 'hospital.html'

class AboutUsPageView(TemplateView):

    template_name = 'about_us.html'

class TermsServicePageView(TemplateView):

    template_name = 'tof.html'

class BlogPageView(TemplateView):

    template_name = 'blog.html'

class UserProfileView(TemplateView):

    template_name = 'user_profile.html'




