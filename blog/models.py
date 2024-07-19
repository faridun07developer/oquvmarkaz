from django.db import models

# Create your models here.


class Darslar(models.Model):
    objects = None
    fan_nomi = models.CharField(max_length=50)

    def __str__(self):
        return self.fan_nomi


class Xonalar(models.Model):
    objects = None
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi


class Oquvchilar(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=40)
    davomati = models.CharField(max_length=50)
    fani = models.ForeignKey(Darslar, on_delete=models.CASCADE)
    tolov = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tolovlar(models.Model):
    objects = None
    oquvchi = models.ForeignKey(Oquvchilar, on_delete=models.CASCADE)
    tolov_miqdori = models.CharField(max_length=100)
    tolovgan_miqdor = models.CharField(max_length=50)

    def __str__(self):
        return self.oquvchi.name


class Oqtuvchilar(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=40)
    oylik = models.CharField(max_length=100)
    oquvchilar = models.IntegerField()
    xonasi = models.ForeignKey(Xonalar, on_delete=models.CASCADE)
    fani = models.ForeignKey(Darslar, on_delete=models.CASCADE, related_name='oqtuvchilar_fani')

    def __str__(self):
        return self.name


class Qabulxona(models.Model):
    objects = None
    admin = models.ForeignKey(Oqtuvchilar, on_delete=models.CASCADE, related_name='qabulxona_admin')
    royxat = models.ForeignKey(Oquvchilar, on_delete=models.CASCADE, related_name='qabulxona_royxat')
    kelgan_oquvchi = models.CharField(max_length=100)

    def __str__(self):
        return self.admin.name


class Davomat(models.Model):
    objects = None
    sana = models.CharField(max_length=100)
    oquvchi = models.ForeignKey(Oquvchilar, on_delete=models.CASCADE, related_name='davomat_oquvchi')
    keldi_kelmadi = models.ForeignKey(Tolovlar, on_delete=models.CASCADE, related_name='davomat_keldi_kelmadi')
    oqtuvchi = models.ForeignKey(Oqtuvchilar, on_delete=models.CASCADE, related_name='davomat_oqtuvchi')

    def __str__(self):
        return self.oquvchi.name


class Oylik(models.Model):
    objects = None
    oqtuvchi = models.ForeignKey(Oqtuvchilar, on_delete=models.CASCADE, related_name='oylik_oqtuvchi')
    oquvchilar_soni = models.CharField(max_length=100)
    tolov_miqdori = models.ForeignKey(Davomat, on_delete=models.CASCADE, related_name='oylik_tolov_miqdori')

    def __str__(self):
        return self.oqtuvchi.name


class Account(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    login = models.CharField(max_length=100)
    phonenumber = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

