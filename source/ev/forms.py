
from django.contrib.auth.models import User

from django.contrib.auth import authenticate
from django.forms import ModelForm
from oz.models import nesne1
from django import forms
from django.contrib.auth import authenticate



class nesneform(ModelForm):

       class Meta:
           model=nesne1

           fields = [ 'ısım','ısım2',]
           labels = {
               "ısım":"Başlık","ısım2":"İçerik"
           }



class sil(ModelForm):


    class Meta:
        model=nesne1
        fields =['ısım']









