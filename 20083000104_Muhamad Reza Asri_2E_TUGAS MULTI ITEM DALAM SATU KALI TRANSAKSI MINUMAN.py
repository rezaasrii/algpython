# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 23:03:51 2021

@author: HP
"""

print ("=========================================")
print ("===KANTIN FAKULTAS TEKNOLOGI INFORMASI===")
print ("=========================================")

print (" ============= ")
print (" =DAFTAR MENU= ")
print (" =============")
print (" MENU MINUMAN ")
print (" =============")
print (" A= TEH DINGIN/HANGAT/PANAS Rp.2.500 ")
print (" B= KOPI DINGIN             Rp.5.000 ")
print (" C= KOPI TEH PANAS          Rp.6.500 ")
print (" D= COCA COLA DINGIN        Rp.3.500 ")
print (" E= COCA COLA PANAS         Rp.5.000 ")
print ("=======================================")
#1.SIAPKAN VARIABLE
KODE     = ['A','B','C','D','E']
MINUMAN  = ['TEH DINGIN/HANGAT/PANAS','KOPI DINGIN','KOPI TEH PANAS','COCA COLA DINGIN','COCA COLA PANAS' ]
HARGA    = [2500,5000,6500,3500, 5000]

#2. INPUT PILIHAN
PILIHAN = input (">> MASUKAN KODE BARANG   = " )


#3. INPUT QTY
QTY     = input (">> MASUKAN JUMLAH BARANG = " )

#4. HITUNG BAYAR 
#CEK NAMA BARANG DAN AMBIL HARGA SATUAN
i = 0 
while i<len(MINUMAN):
    # JIKA VALUE PADA LIST KODE [i] == pilihan 
    if KODE[i]  == PILIHAN:
        #AMBIL NAMA BARANG 
        NM_BRG  = MINUMAN[i]
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
print (">>> TOTAL BAYAR   :Rp." +str(TOT_BYR))