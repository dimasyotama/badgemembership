from django.db import models
from django.contrib.auth.models import User


class Toko(models.Model):
    jenis_produk_pilihan = [
        ("Baju","Baju"),
        ("Celana","Celana"),
        ("Topi","Topi"),
        ("Aksesoris","Aksesoris")
    ]
    jenis_produk = models.CharField(max_length=200,choices=jenis_produk_pilihan)
    nama_produk = models.CharField(max_length=200,null=True)
    harga_produk = models.CharField(max_length=50,null=True)
    diskon_produk = models.CharField(max_length=5,null=True,blank=True)
    deskripsi_produk = models.TextField()

    def __str__(self):
        return self.nama_produk 

class BadgeName(models.Model):
    nama_badge = models.CharField(max_length=10)
    
    def __str__(self):
        return str(self.nama_badge)
    

class PromoCode(models.Model):
    code_promo = models.CharField(max_length=50)
    discount_promo = models.CharField(max_length=5)

class Profile(models.Model):
    nama = models.CharField(max_length=255)
    freq_shop_user = models.CharField(max_length=20)
    nama_produk = models.ForeignKey(Toko,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    badge_name = models.ForeignKey(BadgeName, on_delete=models.CASCADE,null=True, blank=True)

class MemberPrivilege(models.Model):
    nama_badge = models.ForeignKey(BadgeName,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    code_promo = models.ForeignKey(PromoCode,on_delete=models.CASCADE)
    freq_shop_user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    gratis_ongkir = models.CharField(max_length=120)
    def __str__(self):
        return self.nama_badge.nama_badge
    
