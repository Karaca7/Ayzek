import time

from django.shortcuts import render,HttpResponse,redirect
from oz.models import nesne1

from .forms import kullanıcı, koyit
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from django.contrib import messages

from .models import matematik,mantık,ahlak,felsefe,yazılım,anad

from django.conf import settings
from django.conf.urls.static import static









def ana (request):


  postlaraktar = anad.objects.all()
  depos = []
  for i in postlaraktar:
    depos.append(i)


  return render(request ,'oz/oz.html',{'depos':depos})




def giris(request):

    form=kullanıcı(request.POST )





    if form.is_valid():

      username=form.cleaned_data.get('username')
      password=form.cleaned_data.get('password')
      user=authenticate(username=username, password=password)
      login(request,user)



      return redirect('ev')




    return render(request, 'oz/giris.html', {'form':form})





def kayıt(request):
    form=koyit(request.POST)

    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()

        new_user=authenticate(username=user.username, password=password)

        login(request,new_user)
        return redirect('ev')

    return render(request, 'oz/kayıt.html',{'form':form},)



def deneme(request,id):

    cagrılanpost=matematik.objects.filter(id=id)
    return render(request,'oz/deneme.html', {'cagrılanpost':cagrılanpost})





def matematiks(request):

    postlaraktar = matematik.objects.all()
    depo = []
    for i in postlaraktar:
        depo.append(i)

    return render(request,'oz/matematik.html',{'depo':depo} )


def mantıks(request):

    postlaraktar = mantık.objects.all()
    depos = []
    for i in postlaraktar:
        depos.append(i)

    return render(request,'oz/mantık.html',{'depos':depos} )


def mantıkdeneme(request,id):

    mantıkpost=mantık.objects.filter(id=id)
    return render(request,'oz/mantıkdeneme.html', {'mantıkpost':mantıkpost})



def baslangıc(request):
    postlaraktar = ahlak.objects.all()
    depos = []
    for i in postlaraktar:
        depos.append(i)

    return render(request, 'oz/baslangıc.html', {'depos': depos})


def baslangıcdeneme(request,id):

    baslan=ahlak.objects.filter(id=id)
    return render(request,'oz/baslangıcdeneme.html', {'baslan':baslan})





def felsefes(request):
    postlaraktar = felsefe.objects.all()
    depos = []
    for i in postlaraktar:
        depos.append(i)

    return render(request, 'oz/felsefe.html', {'depos': depos})


def felsefedeneme(request,id):

    baslan=felsefe.objects.filter(id=id)
    return render(request,'oz/felsefedeneme.html', {'baslan':baslan})



def yazılıms(request):
    postlaraktar = yazılım.objects.all()
    depos = []
    for i in postlaraktar:
        depos.append(i)

    return render(request, 'oz/yazılım.html', {'depos': depos})


def yazılımdeneme(request,id):

    baslan=yazılım.objects.filter(id=id)
    return render(request,'oz/felsefedeneme.html', {'baslan':baslan})



def iletisim(request):

    return render(request,'oz/iletisim.html')







