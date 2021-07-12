from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


import time
import threading


# Create your models here.



class nesne1Menejer(models.Manager):
    def olusturnesne(self, *args):
        nesnee=self.create(args)
        return nesnee
    def cagır(self):
        nesne1.objects.all()







class nesne1(models.Model):
    ısım=models.CharField(max_length=15)
    ısım2=models.TextField()

    user=models.ForeignKey(User, default=None ,on_delete=models.CASCADE)
    nesne=nesne1Menejer()


    def __str__(self):
        return self.ısım+" "+self.ısım2





class calısannesnemenejer(models.Manager):

    def olusturnesne(self, *args):
        nesnee = self.create(args)
        return nesnee

    def cagır(self):
        calısannesne.objects.all()




class calısannesne(models.Model):
    ısım=models.CharField(max_length=15)
    ısım2=models.TextField()

    user=models.ForeignKey(User,default=None, on_delete=models.CASCADE ,null=True)
    nesne=calısannesnemenejer()


    def __str__(self):
        return self.ısım




class matematikmenejer(models.Manager):

    def olustur(self, *args):
        nesnee=self.create(args)
        return nesnee

    def cagır(self):
        matematik.objects.all()







class matematik(models.Model):

    baslıkpost=models.CharField(max_length=20)
    icerikpost=RichTextField()

    imageflied=models.ImageField(upload_to="images" ,blank=True)

    objects = matematikmenejer()

    def __str__(self):
        return self.baslıkpost


class ahlakmenejer(models.Manager):

    def olustur(self, *args):
        nesnee = self.create(args)
        return nesnee

    def cagır(self):
        ahlak.objects.all()


class ahlak(models.Model):
    baslıkpost = models.CharField(max_length=20)
    icerikpost = RichTextField()

    imageflied = models.ImageField(upload_to="images", blank=True)

    objects = ahlakmenejer()

    def __str__(self):
        return self.baslıkpost






class mantıkmenejer(models.Manager):

    def olustur(self, *args):
        nesnee = self.create(args)
        return nesnee

    def cagır(self):
        mantık.objects.all()


class mantık(models.Model):
    baslıkpost = models.CharField(max_length=20)
    icerikpost = RichTextField()

    imageflied = models.ImageField(upload_to="images", blank=True)

    objects = mantıkmenejer()

    def __str__(self):
        return self.baslıkpost





class felsefemenejer(models.Manager):

    def olustur(self, *args):
        nesnee = self.create(args)
        return nesnee

    def cagır(self):
        felsefe.objects.all()


class felsefe(models.Model):
    baslıkpost = models.CharField(max_length=20)
    icerikpost = RichTextField()

    imageflied = models.ImageField(upload_to="images", blank=True)

    objects = felsefemenejer()

    def __str__(self):
        return self.baslıkpost


class yazılımmenejer(models.Manager):

    def olustur(self, *args):
        nesnee = self.create(args)
        return nesnee

    def cagır(self):
        yazılım.objects.all()


class yazılım(models.Model):
    baslıkpost = models.CharField(max_length=20)
    icerikpost = RichTextField()

    imageflied = models.ImageField(upload_to="images", blank=True)

    objects = yazılımmenejer()

    def __str__(self):
        return self.baslıkpost


class anamenejer(models.Manager):
    def olustur(self, *args):
        nesnee = self.create(args)
        return nesnee

    def cagır(self):
        ana.objects.all()

class ana(models.Model):
    baslıkpost=models.CharField(max_length=100)
    içerikpost=RichTextField()
    objects=anamenejer()


    def __str__(self):
        return self.baslıkpost



class anadmenejer(models.Manager):
    def olustur(self, *args):
        nesnee = self.create(args)
        return nesnee

    def cagır(self):
        ana.objects.all()

class anad(models.Model):
    baslıkpost=models.CharField(max_length=100)
    içerikpost=RichTextField()
    objects=anamenejer()


    def __str__(self):
        return self.baslıkpost