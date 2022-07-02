from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import User


class CustomUserCreationForm(UserCreationForm):
    phone =  PhoneNumberField(widget=forms.TextInput(attrs={'class':'form-control', 'tabindex':'3'}), required=False, region="IN")
    password1 = forms.CharField( required = True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'tabindex':'4'}), label="Password")
    password2 = forms.CharField( required = True, help_text='Enter the same password as before, for verification.', widget=forms.PasswordInput(attrs={'class': 'form-control', 'tabindex':'5'}), label="Password Confirmation")
    class Meta:
        model = User
        fields = ('name', 'email', 'phone', 'password1', 'password2')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'id':'name', 'required':'', 'tabindex':'1', 'autofocus':''}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'id':'email', 'required':'', 'tabindex':'2'}),
            # 'password1': forms.PasswordInput(attrs={'class':'form-control', 'id':'password1', 'required':'', 'tabindex':"3"}),
            # 'password2': forms.PasswordInput(attrs={'class':'form-control', 'id':'password2', 'required':'', 'tabindex':"4"}),
        }


class CustomUserChangeForm(UserChangeForm):
    phone =  PhoneNumberField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False, region="IN")
    class Meta:
        model = User
        fields = ('name', 'phone')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }