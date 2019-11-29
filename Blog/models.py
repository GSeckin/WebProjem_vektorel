from django.db import models
from django.utils import timezone


class Gonderi(models.Model):
    yazar = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    olustur_zaman = models.DateTimeField(
            default=timezone.now)
    yayim_zaman = models.DateTimeField(
            blank=True, null=True)

    def yayimla(self):
        self.yayim_zaman = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik 

class Alanlar(models.Model):
    adını_buraya_yaz = models.CharField(max_length=50)
    isaretle = models.BooleanField()
    isaretleme = models.BooleanField()
    farketmez = models.BooleanField()
    email = models.EmailField()

    def __str__(self):
        return self.adını_buraya_yaz