# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 19:34:59 2021

@author: HP
"""

print ("========================")
print ("=======SLIP GAJI========")
print ("========================")

# SIAPKAN VARIABLE
NAMA = []
GOLONGAN = ['1','2','3']
GAJI_POKOK = [2500000,4500000,6500000,]   
JK = ['L','P']
JENIS_KELAMIN = ['LAKI-LAKI', 'PEREMPUAN']
KODE_STATUS = ['Y', 'T']
STATUS = ['KAWIN','BELUM KAWIN']

#INPUT 
NAMA  = input ("MASUKAN NAMA : ")
GOLONGAN = input ("MASUKAN GOLONGAN : ")

#IDENTIFIKASI PILIHAN GOLONGAN
if GOLONGAN == '1':
    GAJI_POKOK = 2500000
elif GOLONGAN == '2' :
    GAJI_POKOK = 4500000
elif GOLONGAN == '3' :
    GAJI_POKOK = 6500000
else :
    GAJI_POKOK = 2500000
JK = input ("MASUKAN JENIS KELAMIN : ")

#IDENTIFIKASI PILIHAN JENIS KELAMIN
if JK == 'L' :
    JENIS_KELAMIN = 'LAKI-LAKI' 
elif JK == 'P' :
    JENIS_KELAMIN = 'PEREMPUAN'
STATUS = input ("MASUKAN STATUS : ")

# INDENTIFKASI PILIHAN STATUS 
if STATUS == 'T' :
    STATUS_KAWIN = 'BELUM KAWIN'
elif STATUS == 'Y':
    STATUS_KAWIN = 'KAWIN'
TUNJANGAN_ISTRI = input ("MASUKAN GOLONGAN TUNJANGAN ISTRI : ")

# IDENTIFIKASI TUNJANGAN ISTRI
if TUNJANGAN_ISTRI == '1' and JK == 'L' and STATUS == 'Y' :
    TJ_ISTRI = 25000
elif TUNJANGAN_ISTRI == '2' and JK == 'L' and STATUS == 'Y' :
    TJ_ISTRI = 135000
elif TUNJANGAN_ISTRI == '3' and JK == 'L' and STATUS == 'Y' :
    TJ_ISTRI = 325000
elif TUNJANGAN_ISTRI == 'T' :
    TJ_ISTRI = '0'

# IDENTIFIKASI TUNJANGAN ANAK
TUNJANGAN_ANAK = input ("APAKAH MEMILIKI TUNJANGAN ANAK : ")
if TUNJANGAN_ANAK == 'Y' and GOLONGAN == '1' :
    TJ_ANAK = 50000
elif TUNJANGAN_ANAK == 'Y' and GOLONGAN == '2' :
    TJ_ANAK = 90000
elif TUNJANGAN_ANAK == 'Y' and GOLONGAN == '3' :
    TJ_ANAK = 130000
elif TUNJANGAN_ANAK == 'T':
        TJ_ANAK = '0'

# INPUT GAJI BRUTO
GAJI_BRUTO = (GAJI_POKOK) + int(TJ_ISTRI) + int(TJ_ANAK)

# INPUT IURAN PENSIUN
IURAN_PENSIUN = 15500

# INPUT IURAN ORGANISASI
IURAN_ORGANISASI = 3500

# INPUT GAJI NETO 
GAJI_NETO = GAJI_BRUTO - IURAN_PENSIUN - IURAN_ORGANISASI 

# TAMPILKAN HASIL
print ("=======================================")
print ("===============SLIP GAJI===============")
print ("=======================================")
print ("NAMA              = "  + NAMA)
print ("GOLONGAN          = " + GOLONGAN)
print ("JENIS KELAMIN     = " + JENIS_KELAMIN)
print ("STATUS            = " + STATUS_KAWIN)
print ("GAJI POKOK        = Rp." + str(GAJI_POKOK))
print ("TUNJANGAN ISTRI   = Rp." + str(TJ_ISTRI))
print ("TUNJANGAN ANAK    = Rp." + str(TJ_ANAK))
print ("GAJI BRUTO        = Rp." + str(GAJI_BRUTO))
print ("=======================================")
print ("IURAN PENSIUN     = Rp." + str(IURAN_PENSIUN))
print ("IURAN ORGANISASI  = Rp." + str(IURAN_ORGANISASI))
print ("GAJI NETO         = Rp." + str(GAJI_NETO))






