import time

from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, logout

from django.shortcuts import render, get_object_or_404

from ev.models import nesneleer

from django.contrib.auth.models import User
from .forms import nesneform
import threading
from oz.models import nesne1 ,calısannesne
import re
from .forms import sil

from django.core.mail import send_mail, send_mass_mail
from django.conf import settings



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

from ev.cagrılan import Cagrılan
import threading
import sqlite3
from calisan import Calisan




def ev(request):

    if not request.user.is_authenticated:
        return redirect('giris')


    else:

        form = nesneform(request.POST)

        if form.is_valid():


            post=form.save(commit=False)
            post.user=request.user
            post.save()
            text=form.cleaned_data.get('ısım')
            text2=form.cleaned_data.get('ısım2')
            form=nesneform()
            gd = request.user.id


            ab=nesne1.nesne.filter(user_id=gd).values_list('ısım').last()
            cv=ab[0]

            t = threading.Thread(target=h ,args=(text,gd))
            t.start()
        biten=calısannesne.nesne.filter(user=request.user)
        detay2=biten  #.values_list('ısım','id')

        ısımler2=list()
        ısımler2+=detay2

        biten_d=[]
        for i in detay2:
            biten_d.append(i)





        aaa = nesne1.nesne.filter(user=request.user)
        detay = aaa   
        ısımler=list()
        ısımler+=detay
        depo = []
        for i in detay:
            depo.append(i)

        return render(request,'ev/eve.html',{'form' :form , 'biten_depo':biten_d,'bbb':depo })


def cıkıs(request):
    logout(request)
    messages.info(request, "çıkış yapılıyor...") 
    time.sleep(1)
    return redirect('giris')




def silici(request, id):
        nesnesil = nesne1.nesne.filter(id=id).delete()
        return redirect('ev')
       

def silici2(request, id):
        nesnesil = calısannesne.nesne.filter(id=id).delete()
        return redirect('ev')


def h(text,gd):
    hatırlatma_nesnesi = Calisan(text,gd) 



def caldır(text,gd):
    gelen_nesne = Cagrılan.getir(text,gd)
    
    