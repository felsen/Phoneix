# From Dajngo Package Imports:
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

# Form userprofile models imports:
from userprofile.models import UserGetList


class UserLoginForm(forms.Form):

    """ Custom Login form for user. """

    username = forms.CharField(label = ("Username"), max_length = 20, \
                widget = forms.TextInput(attrs = {'class':'form-control'}))
    password = forms.CharField(label = ("Password"), \
                widget = forms.PasswordInput(attrs = {'class':'form-control'}))

class UserRegisterForm(forms.ModelForm):

    """ Custom Registration form for user. """

    confirm_password = forms.CharField(label = ("Confirm Password"), \
                widget = forms.PasswordInput(attrs = {'class':'form-control'}), required = True)
    email = forms.EmailField(label = "Email Address", \
                widget = forms.EmailInput(attrs = {'class':'form-control'}), required = True)

    class Meta:
        model = User
        fields = ("username", "password", "confirm_password", "email")
        widgets = {"username":forms.TextInput(attrs = {'class':'form-control'}),
                   "password":forms.PasswordInput(attrs = {'class':'form-control'}),}

    def clean_confirm_password(self):
    
        """ Password validation matching on register the user details. """
    
        pwd1 = self.cleaned_data['password']
        pwd2 = self.cleaned_data['confirm_password']
        if pwd1 != pwd2:
            raise forms.ValidationError("password and confirm password should be match.")
        return self.cleaned_data

    def clean_email(self):
    
        """ Validating the user email on register. """
    
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

class UserGetListForm(forms.ModelForm):

    """ Get user list model form. """

    def __init__(self,*args, **kwargs):
        super(UserGetListForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['email'].required = True
        self.fields['phone_no'].required = True
        self.fields['organization_name'].required = True
        self.fields['address'].required = True
        self.fields['website'].required = True

    class Meta:
        model = UserGetList
        fields = ('username', 'email', 'phone_no', 'organization_name', 'address', 'website')
        widgets = {"username":forms.TextInput(attrs = {'class':'form-control'}),
                    "email":forms.EmailInput(attrs = {'class':'form-control'}),
                    "phone_no":forms.TextInput(attrs = {'class':'form-control', 'cols':'2'}),
                    "organization_name":forms.TextInput(attrs = {'class':'form-control'}),
                    "address":forms.TextInput(attrs = {'class':'form-control'}),
                    "website":forms.URLInput(attrs = {'class':'form-control'})}

