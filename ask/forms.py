from django import forms
from django.contrib.auth.models import User


class RegForm(forms.Form):
    username = forms.CharField(max_length=16, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_password(self):
        value = self.cleaned_data['password']
        if len(value) < 8:
            raise forms.ValidationError('Password is too short')
        return value

    #def clean(self):
    #    if self.cleaned_data['password'] != self.cleaned_data['password2']:
    #        raise forms.ValidationError('Passwords are different')
    #    return self.cleaned_data

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        return user
