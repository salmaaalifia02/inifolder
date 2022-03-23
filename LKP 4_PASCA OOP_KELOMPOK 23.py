from tkinter import CENTER
import pandas as pd
from tabulate import tabulate 
from pandas._config import (
    get_option,
    set_option,
    reset_option,
    describe_option,
    option_context,
    options,
)

# # inheritance
# class Sepatu:
#     def __init__(self, jenis, ukuran, warna, model):
#         self.__jenis = jenis
#         self.__ukuran = ukuran
#         self.__warna = warna
#         self.__model = model
#     def get_jenis(self):
#         return self.__jenis
#     def get_ukuran(self):
#         return self.__ukuran
#     def get_warna(self):
#         return self.__warna
#     def get_model(self):
#         return self.__model

#     def keterangan(self):
#         return(f'Saya membeli sepatu {self.__jenis} ukuran {str(self.__ukuran)} warna {self.__warna} model {self.__model}')

# class Sepatu_kulit(Sepatu):
#     def __init__(self, jenis, ukuran, warna, model):
#         super().__init__(jenis, ukuran, warna, model)

# class Sepatu_karet(Sepatu):
#     def __init__(self, jenis, ukuran, warna, model):
#         super().__init__(jenis, ukuran, warna, model)

# class Sepatu_denim(Sepatu):
#     def __init__(self, jenis, ukuran, warna, model):
#         super().__init__(jenis, ukuran, warna, model)


# def main():
#     kulit = Sepatu_kulit('kulit', 42, 'Hitam', 'pantopel')
#     print(kulit.keterangan())
#     karet = Sepatu_karet('karet', 40, 'cokelat', 'boots')
#     print(karet.keterangan())
#     denim = Sepatu_denim('denim', 38, 'biru', 'sneakers')
#     print(denim.keterangan())
# main()




# #override
# class Sepatu:
#     def __init__(self, nama, jenis, ukuran, warna, model):
#         self.__nama = nama
#         self.__jenis = jenis
#         self.__ukuran = ukuran
#         self.__warna = warna
#         self.__model = model
#     def get_nama(self):
#         return self.__nama
#     def get_jenis(self):
#         return self.__jenis
#     def get_ukuran(self):
#         return self.__ukuran
#     def get_warna(self):
#         return self.__warna
#     def get_model(self):
#         return self.__model

#     def keterangan(self):
#         return(f'{self.__nama} membeli sepatu {self.__jenis} ukuran {str(self.__ukuran)} warna {self.__warna} model {self.__model}')

# class Sepatu_kulit(Sepatu):
#     def __init__(self, nama, jenis, ukuran, warna, model):
#         super().__init__(nama, jenis, ukuran, warna, model)
        
# class Sepatu_karet(Sepatu):
#     def __init__(self, nama, jenis, ukuran, warna, model, kode = 'ATT000'):
#         super().__init__(nama, jenis, ukuran, warna, model)
#         self.__kode = kode
#     def keterangan(self):
#         return super().keterangan() + ' dengan kode ' + self.__kode

# class Sepatu_denim(Sepatu):
#     def __init__(self, nama, jenis, ukuran, warna, model):
#         super().__init__(nama, jenis, ukuran, warna, model)


# def main():
#     kulit = Sepatu_kulit('Ilham', 'kulit', 42, 'Hitam', 'pantopel')
#     print(kulit.keterangan())

#     karet = Sepatu_karet('Yoga', 'karet', 40, 'cokelat', 'boots')
#     print(karet.keterangan())

#     denim = Sepatu_denim('hesti', 'denim', 38, 'biru', 'sneakers')
#     print(denim.keterangan())

# main() 



# # program lengkap

nama_anggota = ['Salmaa Alifia Rizka','Yoga Randiansyah','Hestiavin Eka Dhelpi','Moch Miftah Fauzan A','Ilham Ardian']
nim = [215060700111006, 215060700111040, 215060701111010, 215060701111037, 215060707111048]

print('[SISTEM PENCATATAN PENJUALAN BARANG DI STORE ICL.SHOE]')
print('\n')
print('Asisten : Maulana Ahmad Fahreza')
print('Kelompok 23')
print('-'*40)
tabel={
    'Nama Anggota':nama_anggota,
    'NIM':nim,}

pddataframe1 = pd.DataFrame(tabel)
pddataframe1.index +=1
pd.set_option('display.colheader_justify','center')
print(tabulate(pddataframe1, showindex=True, headers=pddataframe1.columns))
## pddataframe1.style.set_properties(align="left")
print('-'*40) 
print('\n')


class Sepatu:
    jumlahsepatu = 0
    def __init__(self, nama, jenis, ukuran, warna, model):
        self.__nama = nama
        self.__jenis = jenis
        self.__ukuran = ukuran
        self.__warna = warna
        self.__model = model
        Sepatu.jumlahsepatu += 1

    def get_nama(self):
        return self.__nama
    def get_jenis(self):
        return self.__jenis
    def get_ukuran(self):
        return self.__ukuran
    def get_warna(self):
        return self.__warna
    def get_model(self):
        return self.__model

    def keterangan(self):
        return(f'{self.__nama} membeli sepatu {self.__jenis} ukuran {str(self.__ukuran)} warna {self.__warna} model {self.__model}')

class Sepatu_kulit(Sepatu):
    jumlahsepatukulit=0
    def __init__(self, nama, jenis, ukuran, warna, model):
        super().__init__(nama, jenis, ukuran, warna, model)
        Sepatu_kulit.jumlahsepatukulit += 1
        
class Sepatu_karet(Sepatu):
    jumlahsepatukaret = 0
    def __init__(self, nama, jenis, ukuran, warna, model, kode = 'ATT000'):
        super().__init__(nama, jenis, ukuran, warna, model)
        self.__kode = kode
        Sepatu_karet.jumlahsepatukaret += 1

    def keterangan(self):
        return super().keterangan() + ' dengan kode ' + self.__kode

class Sepatu_denim(Sepatu):
    jumlahsepatudenim = 0
    def __init__(self, nama, jenis, ukuran, warna, model):
        super().__init__(nama, jenis, ukuran, warna, model)
        Sepatu_denim.jumlahsepatudenim += 1

class Sepatu_kaca(Sepatu):
    jumlahsepatukaca = 0
    def __init__(self, nama, jenis, ukuran, warna, model, merk):
        super().__init__(nama, jenis, ukuran, warna, model)
        self.__merk = merk
        Sepatu_kaca.jumlahsepatukaca += 1

    def keterangan(self):
        return super().keterangan() + ' merk ' + self.__merk

def main():
    print('Detail penjualan:               ')
    kulit = Sepatu_kulit('Ilham', 'kulit', 42, 'Hitam', 'pantopel')
    print(kulit.keterangan())

    karet = Sepatu_karet('Yoga', 'karet', 40, 'cokelat', 'boots')
    print(karet.keterangan())

    denim = Sepatu_denim('hesti', 'denim', 38, 'biru', 'sneakers')
    print(denim.keterangan())

    denim = Sepatu_denim('Salmaa','denim',40,'abu-abu', 'sneakers')
    print(denim.keterangan())

    kaca = Sepatu_kaca('ojannn', 'kaca', 44, 'pink', 'sneakers', 'LV' )
    print(kaca.keterangan())


    
    print('\n')
    print('Detail sepatu terjual: ')
    print('Jumlah sepatu kulit terjual adalah',Sepatu_kulit.jumlahsepatukulit)
    print('Jumlah sepatu karet terjual adalah',Sepatu_karet.jumlahsepatukaret)
    print('Jumlah sepatu denim terjual adalah', Sepatu_denim.jumlahsepatudenim)
    print('Jumlah sepatu kaca terjual adalah', Sepatu_kaca.jumlahsepatukaca)
    print('\n')
    print('Total sepatu terjual adalah', Sepatu.jumlahsepatu)



main() 