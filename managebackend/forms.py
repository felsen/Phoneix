# From Dajngo Package Imports:
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

# From Django App Imports:
from hospitalinfo.models import HospitalInfo, ClinicInfo, DgLabsInfo, DoctorsInfo, PharmacyInfo

class HospitalInfoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(HospitalInfoForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['desc'].required = True
        self.fields['email'].required = True
        self.fields['phone'].required = True
        self.fields['spacility'].required = True
        self.fields['image'].required = False
        self.fields['addr'].required = True

    class Meta:
        model = HospitalInfo
        fields = ('name', 'email', 'phone', 'desc', 'spacility', 'image', 'addr')
        widgets = { 'name' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Hospital Name'}),
                    'desc' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Hospital Description'}),
                    'email': forms.EmailInput(attrs = {'class':'form-control', 'placeholder':'Hospital Email'}),
                    'phone': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Hospital Phone'}),
                    'spacility': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Hospital Speciality'}),
                    'image' : forms.FileInput(attrs = {'class':'form-control', 'placeholder':'Hospital Image'}),
                    'addr' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Hospital Address'}),
                }


class DoctorsInfoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(DoctorsInfoForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['desc'].required = True
        self.fields['email'].required = True
        self.fields['phone'].required = True
        self.fields['spacility'].required = True
        self.fields['image'].required = False
        self.fields['addr'].required = True

    class Meta:
        model = DoctorsInfo
        fields = ('name', 'email', 'phone', 'desc', 'spacility', 'image', 'addr')
        widgets = { 'name' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Doctors Name'}),
                    'desc' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Doctors Description'}),
                    'email': forms.EmailInput(attrs = {'class':'form-control', 'placeholder':'Doctors Email'}),
                    'phone': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Doctors Phone'}),
                    'spacility': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Doctors Speciality'}),
                    'image' : forms.FileInput(attrs = {'class':'form-control', 'placeholder':'Doctors Image'}),
                    'addr' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Doctors Address'}),
                }


class ClinicInfoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClinicInfoForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['desc'].required = True
        self.fields['email'].required = True
        self.fields['phone'].required = True
        self.fields['spacility'].required = True
        self.fields['image'].required = False
        self.fields['addr'].required = True

    class Meta:
        model = ClinicInfo
        fields = ('name', 'email', 'phone', 'desc', 'spacility', 'image', 'addr')
        widgets = { 'name' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Clinic Name'}),
                    'desc' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Clinic Description'}),
                    'email': forms.EmailInput(attrs = {'class':'form-control', 'placeholder':'Clinic Email'}),
                    'phone': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Clinic Phone'}),
                    'spacility': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Clinic Speciality'}),
                    'image' : forms.FileInput(attrs = {'class':'form-control', 'placeholder':'Clinic Image'}),
                    'addr' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Clinic Address'}),
                }


class DgLabsInfoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(DgLabsInfoForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['desc'].required = True
        self.fields['email'].required = True
        self.fields['phone'].required = True
        self.fields['spacility'].required = True
        self.fields['image'].required = False
        self.fields['addr'].required = True

    class Meta:
        model = DgLabsInfo
        fields = ('name', 'email', 'phone', 'desc', 'spacility', 'image', 'addr')
        widgets = { 'name' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'DgLab Name'}),
                    'desc' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'DgLab Description'}),
                    'email': forms.EmailInput(attrs = {'class':'form-control', 'placeholder':'DgLab Email'}),
                    'phone': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'DgLab Phone'}),
                    'spacility': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'DgLab Speciality'}),
                    'image' : forms.FileInput(attrs = {'class':'form-control', 'placeholder':'DgLab Image'}),
                    'addr' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'DgLab Address'}),
                }


class PharmacyInfoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PharmacyInfoForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['desc'].required = True
        self.fields['email'].required = True
        self.fields['phone'].required = True
        self.fields['spacility'].required = True
        self.fields['image'].required = False
        self.fields['addr'].required = True

    class Meta:
        model = PharmacyInfo
        fields = ('name', 'email', 'phone', 'desc', 'spacility', 'image', 'addr')
        widgets = { 'name' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Pharmacy Name'}),
                    'desc' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Pharmacy Description'}),
                    'email': forms.EmailInput(attrs = {'class':'form-control', 'placeholder':'Pharmacy Email'}),
                    'phone': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Pharmacy Phone'}),
                    'spacility': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Pharmacy Speciality'}),
                    'image' : forms.FileInput(attrs = {'class':'form-control', 'placeholder':'Pharmacy Image'}),
                    'addr' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Pharmacy Address'}),
                }
