# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#tugas list array Quiz 2
#menampilkan beberapa merk oli motor 
print ("========================================")
print ("==TRANSAKSI PERBAIKAN BENGKEL MOTOR UD==")
print ("========================================")

print (" kode a = Duration SW20 1L")
print (" kode b = Castrol Magnatec 1L ")
print (" kode c = Federal Supreme XX 1L ")
print (" kode d = Yamalube 1L ")
print (" kode e = Shell 1L ")
print ("====================================")

#masukan inputan 
kode = [ 'a','b', 'c', 'd', 'e' ]
merk = [ 'Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L' ]
harga = [53000, 50000, 54000, 45000, 46000]
pilihan = input ("MASUKAN KODE MERK = ")
print ("==============================")

#identifikasi pilihan

if pilihan == "a" :
    idx = 0
elif pilihan == "b" :
    idx = 1
elif pilihan == "c" :
    idx = 2
elif pilihan == "d" :
    idx = 3
elif pilihan == "e" :
    idx = 4
else :
    idx = 0
        
print (">>KODE MERK   =" + kode[idx])
print (">>MERK        =" + merk[idx])
print (">>HARGA       =Rp." + str(harga [idx]))
print ("===================================")

#hitung harga 
FIXHARGA = harga [idx]
#potongan harga 
if FIXHARGA > 200000:
    diskon = FIXHARGA * (25/100)
print (">>TOTAL HARGA =Rp." + str(FIXHARGA)) 
 







 


