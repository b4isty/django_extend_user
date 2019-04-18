from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ValidationError
from .models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             label='Email',
                             error_messages={'exists': 'user with this email id already exists'})

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    # def save(self, commit=True):
    # 
    #     user = super(UserForm, self).save(commit=False)
    #     user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
    #     return user
    # 
    # def clean_email(self):
    #     if User.objects.filter(email=self.cleaned_data['email']).exists():
    #         raise ValidationError(self.fields['email'].error_messages['exists'])
    #     return self.cleaned_data['email']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
