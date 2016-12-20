from __future__ import unicode_literals
from datetime import datetime

from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from students.models import Student


class CreateStudentForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nationality = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    def clean_email(self):
        try:
            existing_user = User.objects.get(email__iexact=self.cleaned_data['email'])
            if existing_user:
                self._errors["email"] = self.error_class(["Email already exist"])
        except User.MultipleObjectsReturned:
            self._errors["email"] = self.error_class(["Email already exist"])
        except:
            pass

        return self.cleaned_data['email']


class GetRequestForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        try:
            get_user = User.objects.get(username__iexact=self.cleaned_data['username'])
            
        except:
            self._errors["username"] = self.error_class(["Username doesn't exist"])

        return self.cleaned_data['username']


class GetDeleteForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        try:
            get_user = User.objects.get(username__iexact=self.cleaned_data['username'])
            
        except:
            self._errors["username"] = self.error_class(["Username doesn't exist"])    

        return self.cleaned_data['username']


class GetEditForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        try:
            get_user = User.objects.get(username__iexact=self.cleaned_data['username'])
            
        except:
            self._errors["username"] = self.error_class(["Username doesn't exist"])

        return self.cleaned_data['username']


class EditStudentForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nationality = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

  