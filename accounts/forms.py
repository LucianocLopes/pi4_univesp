from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts import models

class CustomUserCreateForm(UserCreationForm):

    class Meta:
        model = models.CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {'username': 'Username'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = models.CustomUser
        fields = ('username','first_name', 'last_name', 'email')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = models.CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']


# class SignupForm(forms.Form):   
#     username = forms.CharField(label = 'Usuário')
#     password1 = forms.CharField(label = 'Senha', widget = forms.PasswordInput)
#     password2 = forms.CharField(label = 'Confirme', widget = forms.PasswordInput)


# class LoginForm(forms.Form):   
#     username = forms.CharField(label = 'Usuário')
#     password = forms.CharField(label = 'Senha', widget = forms.PasswordInput)