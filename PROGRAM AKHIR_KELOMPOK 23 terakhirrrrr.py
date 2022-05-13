# ===============================================================================================================================================
from ast import Index
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tabulate import tabulate 

listmaterial = ['kulit sapi','kulit suede','karet','denim','kulit sintesis'] 
deklarasi_nilai = [
  {'zero stock' : 'stok = 0'},
  {'low stock' : 'stok < 100' },
  {'high stock' : 'stok >= 100'}]
tambahanmaterial=[]
liststok = []
status_stok = []

#loginn
def login():
  userpass = {'admin':'123'}

  maxkesempatanlogin = 2
  kesempatanlogin = 0

  masuk = False
  while masuk == False:
    if kesempatanlogin > maxkesempatanlogin:
      print('Maaf, anda telah melebihi batas login')
      print('\n')
      quit()

    userid = input('Masukkan Username : ')
    password = input('Masukkan Password : ')

    for user in userpass:
      if userid in userpass and password == userpass[userid]:
        print('Login sebagai', userid, 'berhasil')
        masuk = True
        print('\n')
        break

      if masuk == False:
        print('Login gagal, username atau password salah')
        print('Kesempatan login tersisa: ', maxkesempatanlogin - kesempatanlogin)
        kesempatanlogin += 1
        print('\n')


#menu utama
def menu():
  daftar_menu = ['Raw Material dan Status Ketersediaan Stok',
                  'Menambahkan Material Baru',
                  'Set Stock',
                  'Menambahkan Stok Material',
                  'Mengurangi Stok Material',
                  'Keluar' ]
  
  print('-'*45)
  tabel={'              DAFTAR MENU' : daftar_menu}

  tabelmenu = pd.DataFrame(tabel)
  tabelmenu.index +=1
  pd.set_option('display.colheader_justify', 'centre')
  print(tabulate(tabelmenu, showindex=True, headers=tabelmenu.columns))
  tabelmenu.style.set_properties(align='left')
  print('-'*45)
  print('\n')
  pilihan_menu = int(input('Masukkan nomor pilihan menu = '))
  

  if(pilihan_menu == 1):
    daftar_material()
  elif(pilihan_menu == 2):
    tambah_material()
  elif(pilihan_menu == 3):
    setstok()
  elif(pilihan_menu == 4):
    tambah_stok_material()
  elif(pilihan_menu == 5):
    kurang_stok_material()
  elif(pilihan_menu == 6):
    exit()
  else:
    print('\n')
    print('INVALID')
    print('\n')
    menu()

def statusstok():
  status_stok.clear()
  i=0
  for i in liststok:
    if i==0:
      hasil = "zero stock"
    elif i<100:
      hasil = "low stock"
    else:
      hasil = "high stock"
    i+=1
    status_stok.append(hasil)
  
  
def daftar_material():
  print('\n')
  if len(liststok) == 0:
    print('*Anda belum menginputkan stok barang*')
    print('-'*50)
    print('\t Raw Material Tersedia')
    print('-'*50)
    for material in (listmaterial):
      print(material)
    input('press any key to continue...')
    print('\n')
    menu()
  print('-'*50)
  print('              Daftar stok raw material     ')
  print('-'*50)
  tabeldata={
    'Raw Material':listmaterial,
    'Stok':liststok,
    'Status':status_stok}
  pddataframe1 = pd.DataFrame(tabeldata)
  pddataframe1.index +=1
  print(pddataframe1)
  print('-'*50)

  plt.bar(listmaterial, liststok, color='red', alpha=0.25)
  plt.grid(linestyle='--', linewidth=2, axis='y', alpha=0.50)

  plt.xlabel('Raw Material')
  plt.ylabel('Jumlah Stok')
  plt.title('Diagram Ketersediaan Stok Barang')

  plt.show()
  input("Press any key to continue..")
  print('\n')
  menu()

def tambah_material(): 
  global tambahanmaterial
  z = input('Apakah ingin menambahkan raw material? (yes/no): ')
  if z == 'yes':
    while z == 'yes':
      if len(liststok) == 0:
        setstok() 
      print('\n')
      tambahanmaterialbaru = (input('Masukkan jenis material baru :  ')).lower()
      if tambahanmaterialbaru not in listmaterial:  
        listmaterial.append(tambahanmaterialbaru) 
        tambahanmaterial.append(tambahanmaterialbaru) 
        print('Masukkan stok',tambahanmaterialbaru)
        while True:
          try:
            s = int(input('Masukkan stok = '))
            if s >= 0:
                liststok.append(s) 
                statusstok()
                z = input('Apakah ingin menambahkan material lagi? (yes/no) : ').lower()
                break
            else:
              print("\n") 
              print('INVALID')
              print('Silahkan masukkan jumlah stok yang benar!')
              print("\n") 
          except:
            print('Masukkan Angka')

        print('\n')
        tabel = {
        "Material" : listmaterial,
        "Stok" : liststok}
        dataframe = pd.DataFrame(tabel)
        dataframe.index +=1
        print(dataframe)
        print('-'*50)

      else:
        print('Material telah tersedia!')
        print('\n')
        tambah_material()
  if z == 'no':
    print('\n')
    menu()
  else:
    print('INVALID')
    print('Masukkan kata yang benar')
    tambah_material()
  statusstok()
  setstok()
  menu()


def setstok():
  if len(liststok) == 0:
    print("\n")    
    print('*Silahkan masukkan stok raw material awal terlebih dahulu*')
    print('-'*60)
    for i in (listmaterial):
        while True:
          try:   
            print("Masukan stok ",i)
            s = int(input('Jumlah stok = '))
            if s >= 0:
              liststok.append(s) 
              break
            else:
              print("\n") 
              print('INVALID')
              print('Silahkan masukkan jumlah stok yang benar!')
              print("\n") 
          except:
            print("\n") 
            print('INVALID')
            print('Silahkan masukkan angka!')
            print("\n") 
          
  statusstok() 
  print('\n')
  print("\n")    
  print('-'*50)    
  print('                 Raw material dan stok      ')
  print('-'*50)
  tabel = {
    "Material" : listmaterial,
    "Stok" : liststok
  }
  dataframe = pd.DataFrame(tabel)
  dataframe.index +=1
  print(dataframe)
  print('-'*50)
  print('\n')
  z = input('Apakah ingin mengubah jumlah stok? (yes/no): ').lower()
  if z == 'yes':
    while z == 'yes':
      while True:
        try:
          Pilihsembarang = int(input('Pilih nomor material yang ingin diubah = '))
          if 0<=Pilihsembarang<=len(liststok):
            Stokbenar = int(input('Masukkan jumlah stok yang benar = '))
            if Stokbenar >= 0:
              liststok[Pilihsembarang-1] = Stokbenar
              print("\n")    
              print('-'*50)    
              print('                 Raw material dan stok      ')
              print('-'*50)
              i=0
              for indeks,material in enumerate(listmaterial, start=1):
                  print(indeks, material, ': ',liststok[i])
                  i+=1
                  indeks+=1
              print('-'*50)
              z = input('Apakah ingin mengubah jumlah stok lagi? (yes/no): ').lower()
              break
            else:
              print('INVALID')
              print('Masukkan jumlah stok yang benar!')
              print('\n')
          else:
            print('\n')
            print('INVALID')
            print('Nomor yang anda masukkan tidak terdapat dalam daftar')
            print('\n')

        except ValueError:
          print('INVALID')
          print('\n')
          continue
          
  if z == 'no':
    print('\n')
    if len(tambahanmaterial) == 0:
          tambah_material()
  else:
    print('INVALID')
    print('Masukkan kata yang benar')
    statusstok()
    setstok()
    menu()
    
def tambah_stok_material():
  if len(liststok) == 0:
    print('-'*50)
    print('*Anda belum menginputkan stok barang*')
    print('-'*50)
    input('press any key to continue...')
    print('\n')
    setstok()
  t = input('Apakah ingin menambahkan stok material? (yes/no) : ').lower()
  if t == 'yes':
    while t == 'yes':
      print("\n")    
      print('-'*50)    
      print('                 Raw material dan stok      ')
      print('-'*50)
      i=0
      for indeks,material in enumerate(listmaterial, start=1):
        print(indeks, material, ': ',liststok[i])
        i+=1
        indeks+=1
      print('-'*50)
      print("\n")
      while True:
        try:
          pilih_material = int(input('Pilih nomor material yang ingin ditambah stoknya = '))
          if 0<= pilih_material<=len(liststok):
            stok_masuk = int(input('masukkan jumlah stok masuk = '))
            liststok[pilih_material-1] = liststok[pilih_material-1] + stok_masuk
            print("\n")    
            print('-'*50)    
            print('                 Raw material dan stok      ')
            print('-'*50)
            i=0
            for indeks,material in enumerate(listmaterial, start=1):
              print(indeks, material, ': ',liststok[i])
              i+=1
              indeks+=1
            print('-'*50)
            t = input('Apakah ingin menambahkan stok material lagi? (yes/no) : ').lower()
            print('\n') 
            break #kayanya
            
          else:
            print('INVALID')
            print('\n')
            continue
        
        except ValueError:
            print('INVALID')
            print('\n')
            continue

  
  if t == 'no':
    print('\n')
    menu()
  else:
    print('INVALID')
    print('Masukkan kata yang benar')
    print('\n')
    tambah_stok_material()


def kurang_stok_material():
  if len(liststok) == 0:
    print('-'*50)
    print('*Anda belum menginputkan stok barang*')
    print('-'*50)
    input('press any key to continue...')
    print('\n')
    setstok()
  v = input('Apakah ingin mengurangi stok material? (yes/no) : ').lower()
  if v == 'yes':
    while v == 'yes':
      print("\n")    
      print('-'*50)    
      print('                 Raw material dan stok      ')
      print('-'*50)
      i=0
      for indeks,material in enumerate(listmaterial, start=1):
        print(indeks, material, ': ',liststok[i])
        i+=1
        indeks+=1
      print('-'*50)
      print("\n")
      while True:
        try:
          pilih_material = int(input('Pilih nomor material yang ingin dikurangi stoknya = '))
          if 0<= pilih_material<=len(liststok):
            stok_keluar = int(input('masukkan jumlah stok keluar = '))
            if stok_keluar > liststok[pilih_material-1]:
              print('INVALID')
              print('Stok barang keluar lebih banyak daripada jumlah stok yang ada')
              stok_keluar = int(input('masukkan jumlah stok keluar = '))
              break
            liststok[pilih_material-1] = liststok[pilih_material-1] - stok_keluar
            print("\n")    
            print('-'*50)    
            print('                 Raw material dan stok      ')
            print('-'*50)
            i=0
            for indeks,material in enumerate(listmaterial, start=1):
              print(indeks, material, ': ',liststok[i])
              i+=1
              indeks+=1
            print('-'*50)
            print("\n")
            v = input('Apakah ingin mengurangi stok material lagi? (yes/no) : ').lower()
            break #kayanya
          else:
            print('INVALID')
            print("\n")
            continue
        except ValueError:
            print('INVALID')
            print('\n')
            continue
    
  if v == 'no':
    menu()
  else:
    print('INVALID')
    print('\n')
    kurang_stok_material()
  
def exit():
  print("\n")
  keluar = input('Apakah anda yakin ingin keluar? (yes/no) = ').lower()
  if keluar == 'yes':
    while keluar == 'yes':
      while True:
        try:
          print('Anda telah keluar')
          quit()
        except ValueError:
          print('INVALID')
          print('Masukkan kata yang benar')
          continue
  if keluar == 'no':
    menu()
  else:
    print('INVALID')
    print('Masukkan kata yang benar')
    exit()
  

login()
menu()