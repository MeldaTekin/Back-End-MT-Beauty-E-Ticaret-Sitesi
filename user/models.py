from django.db import models

# Create your models here.
class Iletisim(models.Model):
    ad= models.CharField(max_length=100)
    soyad= models.CharField(max_length=100)
    eposta= models.EmailField(max_length=100)
    telefon= models.CharField(max_length=11)
    mesaj= models.TextField(max_length=500)

    def __str__(self):

        return self.ad