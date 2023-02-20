from django.db import models
from unicodedata import name

# Create your models here.


class data_hp_is_iii_gabungan(models.Model):
    Type_HP = models.CharField(max_length=7)
    Serial_Number = models.CharField(max_length=14)
    IMEI_1 = models.BigIntegerField(blank=True)
    IMEI_2 = models.BigIntegerField(blank=True)
    Nama_Penanggung_Jawab = models.CharField(blank=True, max_length=29)
    Nopek = models.CharField(blank=True, max_length=18)
    Pengguna_Jabatan = models.CharField(blank=True, max_length=56)
    Bagian = models.CharField(blank=True, max_length=40)
    Fungsi = models.CharField(blank=True, max_length=38)
    No_HP_IS = models.CharField(blank=True, max_length=13)
    Alokasi = models.CharField(blank=True, default=None, max_length=12)
    Keterangan= models.CharField(blank=True, max_length=94)
        
    

    