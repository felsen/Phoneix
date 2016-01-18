# From Dajngo Package Imports:
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

# From Django App Imports:
from hospitalinfo.models import HospitalInfo

class HospitalInfoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(HospitalInfoForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['desc'].required = True
        self.fields['email'].required = True
        self.fields['phone'].required = True
        self.fields['spacility'].required = True

    class Meta:
        model = HospitalInfo
        fields = ('name', 'email', 'phone', 'desc', 'spacility')
        widgets = { 'name' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Hospital Name'}),
                    'desc' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Hospital Description'}),
                    'email': forms.EmailInput(attrs = {'class':'form-control', 'placeholder':'Hospital Email'}),
                    'phone': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Hospital Phone'}),
                    'spacility': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Hospital Speciality'}),
                }
