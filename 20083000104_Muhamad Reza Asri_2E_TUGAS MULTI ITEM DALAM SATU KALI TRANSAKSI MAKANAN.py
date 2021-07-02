# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 21:21:11 2021

@author: HP
"""

print ("=========================================")
print ("===KANTIN FAKULTAS TEKNOLOGI INFORMASI===")
print ("=========================================")

print (" ============= ")
print (" =DAFTAR MENU= ")
print (" =============")
print (" MENU MAKANAN ")
print (" =============")
print (" A= NASI GORENG       Rp.15.000 ")
print (" B= LONTONG GORENG    Rp.14.900 ")
print (" C= BAKSO GORENG      Rp.12.900 ")
print (" D= RUJAK GORENG      Rp.13.000 ")
print (" E= RUJAK BAKSO       Rp.15.000 ")
print (" F= RUJAK BAKSO PECEL Rp.17.000 ")
print ("=================================")

#1.SIAPKAN VARIABLE
KODE     = ['A','B','C','D','E','F']
MAKANAN  = ['NASI GORENG','LONTONG GORENG','BAKSO GORENG','RUJAK GORENG','RUJAK BAKSO','RUJAK BAKSO PECEL' ]
HARGA    = [15000,14900,12900,13000,15000,17000]

#2. INPUT PILIHAN
PILIHAN = input (">> MASUKAN KODE BARANG   = " )


#3. INPUT QTY
QTY     = input (">> MASUKAN JUMLAH BARANG = " )

#4. HITUNG BAYAR 
#CEK NAMA BARANG DAN AMBIL HARGA SATUAN
i = 0 
while i<len(MAKANAN):
    # JIKA VALUE PADA LIST KODE [i] == pilihan 
    if KODE[i]  == PILIHAN:
        #AMBIL NAMA BARANG 
        NM_BRG  = MAKANAN[i]
        #AMBIL HARGA SATUAN
        HRG_SAT = HARGA[i]
    # JIKA TIDAK COCOK, LANJUT KE BERIKUTNYA
    i+=1
TOT_BYR = HRG_SAT * int(QTY)

#5. TAMPILKAN
print ("============================") 
print (">>> NAMA BARANG   :" + NM_BRG)
print (">>> HARGA         :Rp." +str(HRG_SAT))
print (">>> JUMLAH BARANG :" +QTY)
print ("============================")
print (">>> TOTAL         :Rp." +str(TOT_BYR))




