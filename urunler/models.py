from django.db import models

# Create your models here.
class AltKategori(models.Model):
    isim=models.CharField(max_length=100)
    def __str__(self):
        return self.isim


class Kategori(models.Model):
       
    isim=models.CharField(max_length=100)
    sub_category=models.ManyToManyField(AltKategori,blank=True)
    def __str__(self):
        return self.isim

class Marka(models.Model):
    resim=models.FileField(upload_to='markalar/',null=True,blank=True)
    isim=models.CharField(max_length=300)

    def __str__(self):
        return self.isim


class Urun(models.Model):
    kategori=models.ForeignKey(Kategori, on_delete=models.CASCADE,null=True)
    sub_category=models.ManyToManyField(AltKategori,blank=True)
    marka=models.ForeignKey(Marka, on_delete=models.CASCADE,null=True)
    resim=models.FileField(upload_to='urunler/',null=True,blank=True)
    isim=models.CharField(max_length=300)
    aciklama=models.TextField(max_length=500)
    fiyat=models.IntegerField()
    
    
    def __str__(self):
        return self.isim

