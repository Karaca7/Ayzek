from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.db import models

from captcha.fields import CaptchaField




class kullanıcı(forms.Form):


     username=forms.CharField(max_length=20, label='Kullanıcı adı')
     password = forms.CharField(max_length=20, label='Şifre', widget=forms.PasswordInput)

     def clean(self):
          username=self.cleaned_data.get('username')
          password = self.cleaned_data.get('password')
          if username and password:
               user= authenticate(username=username, password=password)
               if not user :
                    raise forms.ValidationError('KULLANICI ŞİFRE VEYA PARALA YANLIŞ')

               return super(kullanıcı, self).clean()



class koyit(forms.ModelForm):
     captcha = CaptchaField()

     username=forms.CharField(max_length=20,label='Kullanıcı adı')

     password1=forms.CharField(max_length=50,label='Şifre',widget=forms.PasswordInput)
     password2 = forms.CharField(max_length=50, label='Şifre doğrulama',widget=forms.PasswordInput)

     class Meta:
          model=User
          fields= [
               'username',
               'first_name',
               'last_name',
               'email',
               'password1',
               'password2',



          ]

     def clean_passowrd2(self):


          password1=self.cleaned_data.get('password1')
          password2 = self.cleaned_data.get('password2')

          if password1 and password2 and password1 !=password2:
               raise  forms.ValidationError('Parola eşleşmiyor ')

          return password2

