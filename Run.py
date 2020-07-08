# import
import csv

# F01 - Load File

# fungsi load
def load(namaFile):
  # Prosedur mengubah CSV menjadi array

  # KAMUS
  # N : banyaknya baris : integer
  # DB : data : array of strings
  # namaFile : nama file : string
  # f : SEQFILE of strings
  #     (1) csvreader : strings * 7
  #     (*) "EOP"
  # i, hia : index : integer

  # ALGORITMA
  DB = [['' for i in range(7)] for j in range(N)]
  f = open(namaFile, 'r')
  csvreader = csv.reader(f)
  
  i = 0
  for hia in csvreader:
    DB[i] = hia
    if (hia[0] == "EOP"):
      DB[i][0] == "EOP"
      break
    i += 1

  return DB
  f.close()

# Prosedur bacaFile
def bacaFile():
  namaFile = input("Masukkan nama File User: ")
  DBuser = load(namaFile)
  namaFile = input("Masukkan nama File Daftar Wahana: ")
  DBwahana = load(namaFile)
  namaFile = input("Masukkan nama File Pembelian Tiket: ")
  DBbeli = load(namaFile)
  namaFile = input("Masukkan nama File Penggunaan Tiket: ")
  DBguna = load(namaFile)
  namaFile = input("Masukkan nama File Kepemilikan Tiket: ")
  DBtiket = load(namaFile)
  namaFile = input("Masukkan nama File Refund Tiket: ")
  DBrefund = load(namaFile)
  namaFile = input("Masukkan nama File Kritik dan Saran: ")
  DBkrisar = load(namaFile)
  print()
  print("File perusahaan Willy Wangky's Chocolate Factory telah di-load.")
  
  return DBuser, DBwahana, DBbeli, DBguna, DBtiket, DBrefund, DBkrisar

# F02 - Login User
# Hanya jika belum login
# Program tidak dapat berlanjut jika belum login

def login(DB):
    user = input("Masukkan username: ")#input dari user
    password = input("Masukkan password: ")
    
    i = 0 #penghitung baris
    indexuser = -999 #indexuser untuk baris keberapa user terdapat
    for j in range(N):
        if (DB[j][3] == user):
            if (DB[j][4] == password):
                print("Selamat bersenang-senang,", DB[j][0], "!")
                return user, True
            else :
                print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
                return '', False
        
        elif (DB[j][0] == mark):
            print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
            return '', False

# F03 - Save File

# fungsi save
def save(namaFile, DB):
  # Prosedur mengubah array menjadi csv

  # KAMUS
  # N : banyaknya baris : integer
  # DB : data : array of strings
  # namaFile : nama file : string
  # f : SEQFILE of
  #     (1) csvwriter
  #     (*) EOP = "EOP"
  # csvwriter : array of strings

  # ALGORITMA

  # Converting Array to CSV
  writeFile = open(namaFile, 'w', newline='')
  fileWriter = csv.writer(writeFile, delimiter=',')
  for j in range(0, N):
      if (DB[j][0] == "EOP"):
          break
      else:
          fileWriter.writerow(DB[j])
  
  # user_table habis atau sudah 100, tulis EOP
  fileWriter.writerow(DB[j])
  
  # close file
  writeFile.close()

# Prosedur saveFile
def saveFile():
  namaFile = input("Masukkan nama File User: ")
  save(namaFile, DBuser)
  namaFile = input("Masukkan nama File Daftar Wahana: ")
  save(namaFile, DBwahana)
  namaFile = input("Masukkan nama File Pembelian Tiket: ")
  save(namaFile, DBbeli)
  namaFile = input("Masukkan nama File Penggunaan Tiket: ")
  save(namaFile, DBguna)
  namaFile = input("Masukkan nama File Kepemilikan Tiket: ")
  save(namaFile, DBtiket)
  namaFile = input("Masukkan nama File Refund Tiket: ")
  save(namaFile, DBrefund)
  namaFile = input("Masukkan nama File Kritik dan Saran: ")
  save(namaFile, DBkrisar)
  print()
  print("Data berhasil disimpan!")

# F04 - Sign Up User
# KHUSUS ADMIN
# Username tidak boleh sudah ada (harus baru)
# prosedur signup
def signup(DB):
    nama = input("Masukkan nama pemain: ")
    tgl_lahir = input("Masukkan tanggal lahir permain (DD/MM/YY): ")
    tinggibadan = input("Masukkan tinggi badan pemain (cm): ")
    username = input("Masukkan username pemain: ")
    password = input("Masukkan password pemain: ")
    role = "Pemain"
    saldo = "0"
    
    for j in range(N):
        if (DB[j][0] == mark):
            break
    DB[j+1] = DB[j]
        
    tempArr = [nama, tgl_lahir, tinggibadan, username, password, role, saldo]
    DB[j] = tempArr
    
    return DB

# F05 - Pencarian Pemain

# Prosedur untuk cari username

### KAMUS
  # N : banyaknya baris : integer
  # DBuser : database user : array of strings
  # username : username pemain : array of string
  # namaPemain : nama pemain : array of string
  # tinggiPemain : data tinggi pemain : array of integer
  # tanggalLahir : data tanggal lahir pemain : array of string
  # mark : penanda akhir file (mark = 'EOP') : array of string

### ALGORITMA

def cari_user():
    # Input dianggap valid
    # KAMUS
    # username : username pemain : string
    # namaPemain : nama pemain : string
    # tinggiPemain : tinggi pemain : integer
    # tanggalLahir : tanggal lahir pemain : ?

    # Input User
    username = input("Masukkan username: ")

    # Mencari username
    for j in range(0, N):
        # username ditemukan         
        if (DBuser[j][3] == username):
            namaPemain = DBuser[j][0]
            tinggiPemain = DBuser[j][3]
            tanggalLahir = DBuser[j][1]
            print("Nama Pemain: ", namaPemain)
            print("Tinggi Pemain: " + str(tinggiPemain))
            print("Tanggal Lahir Pemain: " + str(tanggalLahir))
            return
        # username tidak ditemukan
        elif (DBuser[j][0] == "EOP"):
            print("Pemain tidak ditemukan")
            break

# F06 - Pencarian Wahana

### KAMUS
  # N : banyaknya baris : integer
  # DBuser : database user : array of strings
  # DBfilter : database terfilter : array of strings
  # DBwahana : database wahana : array of strings
  # username : username pemain : array of string
  # inputUmur : kategori umur wahana : integer
  # inputTinggi : kategori tinggi wahana : integer
  # kriteria : kata kunci filter : array of string
  # mark : penanda akhir file (mark = 'EOP') : array of string

### ALGORITMA

# Prosedur untuk filter file (Array)
def filter_wahana(x,kriteria):
  N = 1000
  DBfilter = []

  # Menyalin DBwahana menuju DBfilter
  for j in range (0,N):
    if (DBwahana[j][x] == kriteria):
      DBfilter[j] = DBwahana[j]
    elif (DBwahana[j][x] == mark):
      DBfilter[j][0] == 'EOP'
      break
  
  # Mengatasi row kosong pada DBfilter
  for j in range (0,N):
    if (DBfilter[j] == null):
      DBfilter[j] = DBfilter[j+1]
    elif (DBfilter[j] == mark):
      break

  return DBfilter

# Prosedur untuk cari wahana
def cari():

    # Menampilkan Faktor
    print("Jenis batasan umur: ")
    print("1. Anak-anak (<17 tahun)")
    print("2. Dewasa (>=17 tahun)")
    print("3. Semua umur")
    print("")
    
    print("Jenis batasan tinggi badan: ")
    print("1. Lebih dari 170 cm")
    print("2. Tanpa batasan")
    print("")

    # Input Umur
    inputUmur = input("Batasan umur pemain: ")
    
    # Validasi Input User
    if (0 < inputUmur < 4):
        # Melakukan penyaringan sesuai filter
        # Eksekusi fungsi filter_wahana(row yang ingin difilter,kriteria filter)
        if (inputUmur == 1) :
            filter_wahana(3,'Anak-anak')
        elif (inputUmur == 2) :
            filter_wahana(3,'Dewasa')            
        elif (inputUmur == 3) :
            filter_wahana(3,'Semua umur')   
    else:
        print("Batasan umur tidak valid!")
        return

    # Input Tinggi
    inputTinggi = input("Batasan tinggi badan: ")
    
    # Validasi Input Tinggi
    if (0 < inputTinggi < 4):
        # Melakukan penyaringan sesuai filter
        # Eksekusi fungsi filter_wahana(row yang ingin difilter,kriteria filter)
        if (inputUmur == 1) :
            filter_wahana(4,'Lebih dari 170 cm')
        elif (inputUmur == 2) :
            filter_wahana(4,'Tanpa batasan')            
    else:
        print("Batasan tinggi tidak valid!")
        return

    # Menampilkan hasil pencarian
    for j in range(0, N):

        # Wahana ditemukan         
        if (DBfilter[j][0] != "EOP"):
            print('Hasil pencarian: ')
            print(DBfilter[j][0] + ' | ' + DBfilter[j][1] + ' | ' + DBfilter[j][2])
            return
            
        # wahana tidak ditemukan
        elif (DBfilter[j][0] == "EOP"):
            print("Wahana tidak ditemukan")
            return

# F07 - Pembelian Tiket
### KAMUS

### ALGORITMA
def beli_tiket(user):
    # Fitur hanya dapat dilakukan pemain terdaftar dan logged in
    # Memasukkan ID
    inputID = input('Masukkan ID wahana: ')
    # Tinggi badan pemain dan tanggal lahir
    # Sudah login
    for j in range(N):
        if (DBuser[j][3] == user):
            tinggi = int(DBuser[j][2])
            tanggal_lahir = DBuser[j][1]
            print(tanggal_lahir)
            break
        elif (DBuser[j][0] == mark):
            break

    # Pengecekkan Wahana
    for j in range(0, N):

        # Wahana terdaftar
        if (DBwahana[j][0] == inputID):

            # Tinggi tidak mencukupi
            if (tinggi < 170 and DBwahana[j][4] == 'Lebih dari 170 cm'):
                print('Tinggi anda tidak mencukupi untuk memainkan wahana ini')
                return

            # Convert DD/MM/YYYY menjadi tahun, bulan, hari
            # 01 2 34 5 6789
            # DD / MM / YYYY
            for item in tanggal_lahir:
                tahun = tanggal_lahir[6] + tanggal_lahir[7] + tanggal_lahir[8] + tanggal_lahir[9]
                bulan = tanggal_lahir[3] + tanggal_lahir[4]
                hari = tanggal_lahir[0] + tanggal_lahir[1]
                break

            # Cek Umur
            hariTahun = int(tahun) * 365
            hariBulan = int(bulan) * 30
            umur = hariTahun + hariBulan + int(hari)
            dewasa = 17 * 365

            # Umur tidak mencukupi
            if (umur < dewasa and DBwahana[j][3] == 'Dewasa'):
                print('Umur anda tidak sesuai persyaratan wahana.')
                return

            elif (umur >= dewasa and DBwahana[j][3] == 'Anak-anak'):
                print('Umur anda tidak sesuai persyaratan wahana')
                return

            # Umur dan tinggi sesuai
            else:

                # Memasukkan Tanggal
                inputTanggal = input('Masukkan tanggal hari ini: ')

                # Memasukkan Jumlah Tiket
                inputTiket = input('Jumlah tiket yang dibeli: ')

                # Pengecekkan harga tiket dengan saldo yang dimiliki
                for j in range(0, N):
                    if (DBwahana[j][0] == inputID):

                        # Total Harga =  Harga Tiket * Jumlah Tiket Dibeli
                        if (not (isGold(user))):
                            totalHarga = int(DBwahana[j][2]) * inputTiket
                        elif (isGold(user)):
                            totalHarga = int(DBwahana[j][2]) * inputTiket * (0.5)
                        # Saldo Akhir = Saldo Awal - Total Harga
                        saldoAkhir = int(DBuser[j][6]) - int(totalHarga)

                        # Validasi Kecukupan Saldo
                        if (saldoAkhir >= 0):  # Saldo mencukupi

                            # Saldo = Saldo Akhir
                            DBuser[j][6] == saldoAkhir

                            # Menambah tiket yang dimiliki
                            for j in range(0, N):

                                # Bila user telah memiliki tiket wahana sebelumnya
                                if (DBtiket[j][0] == user and DBtiket[j][1] == inputID):

                                    # Jumlah Tiket Akhir = Jumlah Tiket Awal + Jumlah Tiket Dibeli
                                    DBtiket[j][2] = DBtiket[j][2] + inputTiket

                                    # Selamat bersenang-senang di Wahana
                                    print("Selamat bersenang-senang di ", DBwahana[j][1])

                                # Bila user belum memiliki tiket wahana sebelumnya
                                elif (DBtiket[j][0] == mark):

                                    # Membuat row data baru
                                    DBtiket[j + 1] = DBtiket[j]
                                    DBtiket[j] = [user, inputID, inputTiket]

                                    # Selamat bersenang-senang di Wahana
                                    print("Selamat bersenang-senang di ", DBwahana[j][1])

                        else:  # (saldoAkhir < 0):

                            # Saldo tidak mencukupi
                            print('Saldo yang anda miliki tidak cukup.')
                            return

        # Wahana tidak terdaftar
        elif (DBuser[j][0] == mark):
            print('ID wahana tidak terdaftar')
            return


# F08 - Menggunakan Tiket
### KAMUS

### ALGORITMA
def main(user):
    # Input ID Wahana
    inputID = input('Masukkan ID wahana: ')
    username = user

    # Pengecekkan ID wahana
    for j in range(0, N):
        if (DBwahana[j][0] == inputID):

            # Input Tanggal
            inputTanggal = input('Masukkan tanggal hari ini: ')

            # Input Tiket yang Digunakan
            inputTiket = int(input('Jumlah tiket yang digunakan: '))

            # Validasi tiket
            if (inputTiket <= int(DBtiket[j][2])):  # Valid
                for j in range(N):
                    if (DBtiket[j][0] == username):
                        rekam = j
                        DBtiket[rekam][2] = int(DBtiket[rekam][2]) - inputTiket
                        print('Terima kasih telah bermain.')
                        break
            elif (inputTiket > int(DBtiket[j][2])):  # Tidak cukup
                print('Anda tidak valid dalam sistem kami')

            elif (DBtiket[j][0] == mark):  # Tidak memiliki tiket
                print('Tiket Anda valid dalam sistem kami')

        elif DBwahana[j][0] == mark:  # Wahana tidak terdaftar
            break


# F09 - Refund
def refund(user):

    ID = input("Masukkan ID Wahana: ")
    TGL= input("Masukkan Tanggal Refund: ")
    JML = int(input("Jumlah tiket yang di-refund: "))

    username = user
    # Pengecekan ID
    cek_ID = False
    for j in range(0, N):
        # ID ditemukan
        if (DBwahana[j][0] == ID):
            Harga = int(DBwahana[j][2])
            Harga_Refund = Harga*(0.25)
            valid_ID = ID
            cek_ID = True
        # File kosong
        elif (DBwahana[j][0] == "EOP"):
            break
    # Pengecekan Kepemilikan Tiket
    cek_tiket = False
    for j in range(0, N):
        # Temukan Username
        if (DBtiket[j][0] == username):
            rekam = j
            # Tiket ada dan jumlah memenuhi
            if DBtiket[rekam][1] and JML <= int(DBtiket[rekam][2]) :
                cek_tiket = True
            # File kosong
            elif (DBtiket[j][0] == "EOP"):
                break
        elif (DBtiket[j][0] == "EOP"):
            break

    # Menyimpan ke array untuk dimasukkan ke File Refund
    if cek_ID and cek_tiket:
        for j in range(N):
            if DBrefund[j][0] == "EOP":
                DBrefund[j][0] = username # Dr LOGIN USER
                DBrefund[j][1] = TGL
                DBrefund[j][2] = valid_ID
                DBrefund[j][3] = JML
                break
        # Tulis EOP
        DBrefund[j+1] = ["EOP","","",""]
    if cek_ID and cek_tiket:
        for j in range(N):
            if (DBtiket[j][0] == username):
                rekam = j
                DBtiket[rekam][2] = int(DBtiket[rekam][2]) - JML
                break
    if cek_ID and cek_tiket:
        for j in range(N):
            if (DBuser[j][3] == username):
                saldo = float(DBuser[j][6]) + Harga_Refund
                DBuser[j][6] = saldo
                print("Uang refund sudah kami kami berikan pada akun Anda.")
                break
    else:
        print("Anda tidak memiliki tiket terkait")


# F10 - Kritik dan Saran
def add_krisar(user):
    # Input dianggap valid
    # KAMUS
    # username : username pemain : string
    # tambah : banyak penambahan saldo : integer
    # user_table : matrix data pemain : matrix of strings
    # saldo : saldo pemain : integer
    # nama : nama pemain : string

    # Input User
    ID = input("Masukkan ID Wahana: ")
    TGL = input("Masukkan tanggal pelaporan: ")
    Krisar = input("Kritik/saran Anda: ")
    # Misal
    username = user
    # Mencari username
    for j in range(0, N):

        if (DBkrisar[j][0]) == mark:
            DBkrisar[j][0] = username   # username Dr login user
            DBkrisar[j][1] = TGL
            DBkrisar[j][2] = ID
            DBkrisar[j][3] = Krisar
            break
    # Tulis EOP
    DBkrisar[j+1] = [mark,"","",""]


    print("Kritik/saran Anda kami terima")


# F11 - Melihat Kritik dan Saran
def length_of_DBKrisar():
    for j in range(N):
        if DBkrisar[j][0] == mark:
            rekam = (j-1)
    return rekam

# Referensi fungsi Sort_ID dari https://www.geeksforgeeks.org/python-program-to-sort-a-list-of-tuples-alphabetically/?ref=rp
def SortID(arrayDB):

    n = length_of_DBKrisar()
    for i in range(n):
        for j in range(n-i-1):
            if arrayDB[j][2] > arrayDB[j+1][2]:
                arrayDB[j][2], arrayDB[j+1][2] = arrayDB[j+1][2], arrayDB[j][2]
    return arrayDB

def lihat_laporan():
    i = 0
    DBkrisar_FIX = ["" for i in range(length_of_DBKrisar())]
    while i < length_of_DBKrisar():
        DBkrisar_FIX[i] = DBkrisar[i+1]
        i += 1

    DBkrisar_sort = SortID(DBkrisar_FIX)
    for i in range(length_of_DBKrisar()):
        print(DBkrisar_sort[i][2],"|",DBkrisar_sort[i][1],"|",DBkrisar_sort[i][0],"|",DBkrisar_sort[i][3])

# F12 - Menambahkan Wahana Baru
def add_wahana():
    # Input dianggap valid
    # KAMUS
    # username : username pemain : string
    # tambah : banyak penambahan saldo : integer
    # user_table : matrix data pemain : matrix of strings
    # saldo : saldo pemain : integer
    # nama : nama pemain : string

    # Input User
    ID = input("Masukkan ID Wahana: ")
    NAMA = input("Masukkan Nama Wahana: ")
    HARGA = int(input("Masukkan Harga Tiket: "))
    UMUR = input("Batasan umur: ")
    TINGGI = input("Batasan tinggi badan: ")

    for j in range(0, N):

        if (DBwahana[j][0]) == mark:
            DBwahana[j][0] = ID
            DBwahana[j][1] = NAMA
            DBwahana[j][2] = HARGA
            DBwahana[j][3] = UMUR
            DBwahana[j][4] = TINGGI
            break
    # Tulis EOP
    DBwahana[j+1] = [mark,"","","",""]


    print("Info wahana telah ditambahkan")


# F13 - Top Up Saldo
def tambah_saldo():
    # KAMUS
    # username : username pemain : string
    # tambah : banyak penambahan saldo : integer
    # DBuser : matrix data pemain : matrix of strings
    # saldo : saldo pemain : integer
    # nama : nama pemain : string
    # mark : penanda akhir proses : string
    # j : variabel
    
    # Input User
    username = input("Masukkan username: ")
    tambah = int(input("Masukkan saldo yang di-top up: "))

    # Mencari username
    for j in range(0, N):
        # username ditemukan         
        if (DBuser[j][3] == username):
            nama = DBuser[j][0]
            saldo = int(DBuser[j][6]) + tambah
            DBuser[j][6] = saldo
            print("Top up berhasil. Saldo", nama, "bertambah menjadi " +str(saldo))
        
        # username tidak ditemukan
        elif (DBuser[j][0] == mark):
            break

# F14 - Melihat Riwayat Penggunaan Wahana
def lihat_riwayat():
    # KAMUS
    # ID_wahana : string
    # DBguna : data penggunaan : matrix of strings
    # j : variabel

    # ALGORITMA
    ID_wahana = input("Masukkan ID Wahana: ")
    print("Riwayat:")
    for j in range(N):
        # ID Wahana ditemukan
        if (DBguna[j][2] == ID_wahana):
            print(DBguna[j][1] + " | " + DBguna[j][0] + " | " + DBguna[j][3])
        
        # ID Wahana tidak ditemukan
        elif (DBguna[j][0] == mark):
            break

# F15 - Melihat Jumlah Tiket Pemain
def lihat_tiket():
    # KAMUS
    # username : username pemain : string
    # ID_Wahana, Nama_Wahana : string
    # DBtiket, DBwahana : data : matrix of strings
    # j : variabel
    # mark : penanda -akhir proses- : string

    # ALGORITMA
    username = input("Masukkan username: ")
    print("Riwayat:")
    for j in range(N):
        # username ditemukan
        if (DBtiket[j][0] == username):
            ID_Wahana = DBtiket[j][1]

            # ID Wahana ditemukan
            for i in range(N):
                # Nama Wahana ditemukan
                if (DBwahana[i][0] == ID_Wahana):
                    Nama_Wahana = DBwahana[i][1]
                    print(ID_Wahana + " | " + Nama_Wahana + " | " + DBtiket[j][2])
                    break

                # Nama Wahana tidak ditemukan
                elif (DBwahana[i][0] == mark):
                    break
                
        # username tidak ditemukan
        elif (DBtiket[j][0] == mark):
            break

# F16 - Exit
def Exit(): 
    # Menampilkan pilihan untuk exit program, saveFile atau tidak.

    # KAMUS
    # choice : pilihan save : character
    # namaFile : nama file : string
    # prosedur saveFile : prosedur untuk menyimpan array ke file .csv

    # ALGORITMA
    choice = input("Apakah Anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ")
    if (choice == "Y"):
        saveFile()


# B01 - Enkripsi Password
def newlen(all_possible_char):
    sum = 1
    for character in all_possible_char:
        if character == '"':
            break
        else:
            sum = sum + 1
    return sum

# Referensi def enkripsi(password) dari https://koding.alza.web.id/teknik-enkripsi-caesar-cipher-dengan-bahasa-pemrograman-python/

def enkripsi(password):
    almost_possible_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+{}|:<>?,./';[]\-=`"
    rest = '"'
    all_possible_char = almost_possible_char + rest
    ubah = ""
    for symbol in password:
         if symbol in all_possible_char:
             old_index = all_possible_char.index(symbol)
             new_index = (old_index + 17) % (newlen(all_possible_char))
             enkripsi_password = all_possible_char[new_index]
             ubah = ubah + enkripsi_password
    return ubah

# ALGORITMA
def length_of_DB():
    for j in range(N):
        if DBuser[j][0] == mark:
            rekam = (j-1)
            break
    return rekam

def save_pass():
    for j in range(length_of_DB() + 1 ):
            DBuser[j][4] = enkripsi(DBuser[j][4]) 


# B02 - Golden Account
def upgrade_account():
    # KAMUS
    # username : username untuk diupgrade : strings
    # DBuser : data pemain : matrix of strings
    # mark : penanda -akhir proses- : string
    # j : variabel

    # ALGORITMA
    # Upgrade Account ke Golden Account
    username = input("Masukkan username yang ingin di-upgrade: ")
    print()
    print()
    
    # Mencari username
    for j in range(0, N):
        # username ditemukan         
        if (DBuser[j][3] == username):
            if (DBuser[j][5] == "Pemain"): # Hanya pemain yang diupgrade
                # Data Gold dimasukan ke dalam Role
                DBuser[j][5] = "Gold"
                print("Akun Anda telah di-upgrade.")
            else :
                break

        # username tidak ditemukan
        elif (DBuser[j][0] == mark):
            break

# Fungsi cek status Gold
def isGold(user):
    for j in range(N):
        if (DBuser[j][3] == user):
            if (DBuser[j][5] == "Gold"):
                return True
            else:
                return False
        else:
            return False

# Fungsi cek apakah admin
def isAdmin(user):
    # Memeriksa, admin atau bukan.
    for j in range(N):
        if (DBuser[j][3] == user):
            if (DBuser[j][5] == "Admin"):
                return True
            else :
                return False
        elif (DBuser[j][0] == mark):
            return False

# KAMUS
N = 1000 # banyaknya array : integer
mark = "EOP" # penanda stop proses : string
# do : perintah dalam program : string
# loggedin : status login : bool
# loaded : status load file : bool
# DBuser, DBwahana, DBbeli, DBguna, DBtiket, DBrefund, DBkritsar : data : matrix of strings
# user : username akun yang sudah login : string
############ FUNCTION DAN PROCEDURE ##############
# function bacaFile (output : DB <matrix of strings>)
# function login (input : DBuser , output : string, bool)
# procedure saveFile (output : file csv)
# procedure signup (input : DBuser <matrix of strings>, output : DBuser)
# procedure cari_user (output : string)
# procedure cari_wahana (output : strings)
# procedure beli_tiket (output : strings, DBuser, DBtiket)
# procedure ##MAIN
# procedure ##REFUND
# procedure ##KRISAR
# procedure #LIHAT_LAPORAN
# procedure #TAMBAH_WAHANA
# procedure tambah_saldo (output : DBuser)
# procedure lihat_riwayat (output : strings)
# procedure lihat_tiket (output : strings)
# procedure Exit (output : CSV file)

# ALGORITMA UTAMA

# Untuk memeriksa sudah login atau belum
loggedin = False
loaded = False

# Mulai Program
command = input("$ ")

while (command != "exit"):
  
  # F01 - Load File
  if (command == "load") :
    DBuser, DBwahana, DBbeli, DBguna, DBtiket, DBrefund, DBkrisar = bacaFile()
    loaded = True

  if (loaded == True):
  # F02 - Login
    if (command == "login") :
      if (loggedin == False):
        user, loggedin = login(DBuser)

    # F03 - Save File
    elif (command == "save") :
      saveFile()

    # F04 - Sign Up
    elif (command == "signup") :
      if (loggedin == True):
        if (isAdmin(user)):
          signup(DBuser)

    # F05 - Pencarian Pemain
    elif (command == "cari_pemain"):
      if (loggedin == True):
        if (isAdmin(user)):
          cari_user()
        
    # F06 - Pencarian Wahana
    elif (command == "cari"):
      cari_wahana()
    
    # F07 - Pembelian Tiket
    elif (command == "beli_tiket"):
      if (loggedin == True):
        beli_tiket(user)

    # F08 - Menggunakan Tiket
    elif (command == "main"):
      if (loggedin == True):
        main(user)

    # F09 - Refund
    elif (command == "refund"):
      if (loggedin == True):
        refund(user)

    # F10 - Kritik dan Saran
    elif (command == "kritik_saran"):
      if (loggedin == True):
        add_krisar(user)

    # F11 - Melihat Kritik dan Saran
    elif (command == "lihat_laporan"):
      if (loggedin == True):
        if (isAdmin(user)):
          lihat_laporan() # fungsi lihat laporan

    # F12 - Menambahkan Wahana Baru
    elif (command == "tambah_wahana"):
      if (loggedin == True):
          if (isAdmin(user)):
            add_wahana() # fungsi tambah wahana

    # F13 - Top Up Saldo
    elif (command == "topup"):
      if (loggedin == True):
        if (isAdmin(user)):
          tambah_saldo()

    # F14 - Melihat Riwayat Penggunaan wahana
    elif (command == "riwayat_wahana"):
      if (loggedin == True):
        if (isAdmin(user)):
          lihat_riwayat()

    # F15 - Melihat Jumlah Tiket Pemain
    elif (command == "tiket_pemain"):
      if (loggedin == True):
        if (isAdmin(user)):
          lihat_tiket()

    # B01 - Penyimpanan Password

    
    # B02 - Golden Account
    elif (command == "upgrade_gold"):
      if (loggedin == True):
        if (isAdmin(user)):
          upgrade_account()
    
    # B03 - Best Wahana


    # B04 - Lapor Kehilangan Tiket


  # reinput do
  command = input("$ ")

# Akhir - F16 - Exit
Exit()