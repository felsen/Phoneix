# Django Imports:
from django.shortcuts import render, render_to_response
from django.views.generic.base import TemplateView
from django.contrib.auth import login as auth_login, authenticate, get_user
from django.http import HttpResponseRedirect
from django.views.generic import FormView, View, CreateView, ListView
from django.contrib.auth.models import User

# Project Imports:
from userprofile.forms import UserLoginForm
from managebackend.forms import HospitalInfoForm
from hospitalinfo.models import HospitalInfo

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

class ManageDoctorsView(TemplateView):

    template_name = 'admin_templates/admin_doctors.html'

class ManageHospitalsView(CreateView):

    model = HospitalInfo
    form_class = HospitalInfoForm
    template_name = 'admin_templates/admin_hospitals.html'
    success_url = '/manage-hospitals/'

    def get_context_data(self, *args, **kwargs):
        context = super(ManageHospitalsView, self).get_context_data(*args, **kwargs)
        context['hospital_list'] = HospitalInfo.objects.all()
        return context


class ManageClinicView(TemplateView):

    template_name = 'admin_templates/admin_clinic.html'

class ManageDignosticView(TemplateView):

    template_name = 'admin_templates/admin_dignostic.html'

class ManagePharmacyView(TemplateView):

    template_name = 'admin_templates/admin_pharmacy.html'
