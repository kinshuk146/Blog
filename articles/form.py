from django import forms
from django.contrib.auth.models import User
from .models import Article

class LoginForm(forms.Form):
    username= forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class UserRegistration(forms.ModelForm):

    password= forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('username','first_name','email')

    def clean_password(self):
        cd=self.cleaned_data
        if cd['password'] != cd['password']:
            raise forms.ValidationError('Passwords Do not Match')
        else:
            return cd['password']


class ArticleRegistrationForm(forms.ModelForm):

    class Meta:
        model=Article
        fields=('title','description')


class ArticleUpdateForm(forms.ModelForm):

    class Meta:
        model=Article
        fields=('title','description')






