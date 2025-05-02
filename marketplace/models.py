from django.db import models
from django.contrib.auth.models import AbstractUser

class Towar(models.Model):
    naswan = models.CharField(max_length=30)
    zena = models.DecimalField(max_digits=12, decimal_places=2)
    proiswoditel = models.CharField(max_length=30)
    nalichie = models.IntegerField()
    data_prois = models.DateField()
    opisanie = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True, default='images/default.jpg')

class Polso(AbstractUser):
    adres = models.CharField(max_length=50, default="Адрес не указан")
    kontakt = models.CharField(max_length=13, default="Телефон не указан")

class Korsin(models.Model):
    pols = models.OneToOneField(Polso, on_delete=models.CASCADE, related_name="korsinka")
    towari = models.ManyToManyField(Towar, related_name="korsinki", through="Korsin_towari")

class Korsin_towari(models.Model):
    korsin = models.ForeignKey(Korsin, on_delete=models.CASCADE)
    towar = models.ForeignKey(Towar, on_delete=models.CASCADE)
    kolich = models.IntegerField(default=1)