# Django Imports:
from django.shortcuts import render, render_to_response
from django.views.generic.base import TemplateView
from django.contrib.auth import login as auth_login, authenticate, get_user
from django.http import HttpResponseRedirect
from django.views.generic import FormView, View, CreateView, ListView
from django.contrib.auth.models import User

# Project Imports:
from userprofile.forms import UserLoginForm
from managebackend.forms import HospitalInfoForm, DoctorsInfoForm, ClinicInfoForm, DgLabsInfoForm, \
    PharmacyInfoForm
from hospitalinfo.models import HospitalInfo, DoctorsInfo, ClinicInfo, DgLabsInfo, PharmacyInfo

class ManageLoginView(FormView):

    """ Login view for admin page """

    template_name = 'admin_templates/admin_login.html'
    success_url = "/manage-home/"
    form_class = UserLoginForm
    user_error = "username or password incorrect."

    def form_valid(self, form):
        user = authenticate(username=self.request.POST.get('username'), \
                            password = self.request.POST.get('password'))
        if user is not None:
            if user.is_superuser:
                auth_login(self.request, user)
                return super(ManageLoginView, self).form_valid(form)
        return render(self.request, self.template_name, {
            'form':form, 'user_error':self.user_error
        })

class ManageHomeView(TemplateView):

    template_name = 'admin_templates/admin_index.html'


class ManageVisitorsView(TemplateView):

    template_name = 'admin_templates/admin_visitors.html'

class ManageDoctorsView(CreateView):

    model = DoctorsInfo
    form_class = DoctorsInfoForm
    template_name = 'admin_templates/admin_doctors.html'
    success_url = '/manage-doctors/'

    def get_context_data(self, *args, **kwargs):
        context = super(ManageDoctorsView, self).get_context_data(*args, **kwargs)
        context['doctors_list'] = DoctorsInfo.objects.all()
        return context

class ManageHospitalsView(CreateView):

    model = HospitalInfo
    form_class = HospitalInfoForm
    template_name = 'admin_templates/admin_hospitals.html'
    success_url = '/manage-hospitals/'

    def get_context_data(self, *args, **kwargs):
        context = super(ManageHospitalsView, self).get_context_data(*args, **kwargs)
        context['hospital_list'] = HospitalInfo.objects.all()
        return context


class ManageClinicView(CreateView):

    model = ClinicInfo
    form_class = ClinicInfoForm
    template_name = 'admin_templates/admin_clinic.html'
    success_url = '/manage-clinic/'

    def get_context_data(self, *args, **kwargs):
        context = super(ManageClinicView, self).get_context_data(*args, **kwargs)
        context['clinic_list'] = ClinicInfo.objects.all()
        return context

class ManageDignosticView(CreateView):

    model = DgLabsInfo
    form_class = DgLabsInfoForm
    template_name = 'admin_templates/admin_dignostic.html'
    success_url = '/manage-dignostic/'

    def get_context_data(self, *args, **kwargs):
        context = super(ManageDignosticView, self).get_context_data(*args, **kwargs)
        context['dglabs_list'] = DgLabsInfo.objects.all()
        return context

class ManagePharmacyView(CreateView):

    model = PharmacyInfo
    form_class = PharmacyInfoForm
    template_name = 'admin_templates/admin_pharmacy.html'
    success_url = '/manage-pharmacy/'

    def get_context_data(self, *args, **kwargs):
        context = super(ManagePharmacyView, self).get_context_data(*args, **kwargs)
        context['pharmacy_list'] = PharmacyInfo.objects.all()
        return context
