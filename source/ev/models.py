from django.db import models


from django.contrib.auth.models import User

# Create your models here.




class nesnemenejer(models.Manager):
    def olustur(self):
        nesne=self.create(ad='ad', ad2='ad2')
        return nesne


class nesneleer(models.Model):

    ad=models.CharField(max_length=15)
    ad2=models.CharField(max_length=15)

    objects=nesnemenejer()

    user=models.ForeignKey(User, default=None ,on_delete=models.CASCADE)





    def __str__(self):
        return self.ad, self.ad2



