import os
import pelanggan 
import admin
import petugasnikah
import transaksi
import paketnikah
from datetime import datetime

def login():
    os.system("cls")
    print("Halaman Login".center(115))
    global username
    username = input('Username: ')
    password = input('Password: ')
    adaUser = False
    if user == "1":
        for cust in pelanggan.readcust():
            if username == cust[0] and password == cust[2]:
                adaUser = True
                break
    elif user == "2": 
        for data in admin.readadmin():
            if username == data[0] and password == data[1]:
                adaUser = True
                break
    if adaUser == True:
        if user == '1':
            menucust()
        elif user == '2':
            menuadmin()
    else:
        input('Yah, username/password yang kamu masukkan salah. Coba lagi yuk 🙌\nTekan enter untuk lanjut => ')
        os.system("cls")
        login()

def punyaakun():
    os.system("cls")
    print("Apakah kamu sudah punya akun?".center(115))
    status_akun = input("|1| Sudah\n|2| Belum\nPilih: ")
    os.system("cls")
    if status_akun == '1':
        login()
    elif status_akun == '2':
        regist()

def regist():
        os.system("cls")
        print("Pendaftaran Akun\n".center(115))
        nama_pengguna = input('Nama lengkap (sesuai kartu identitas)         : ')
        email = input("Masukkan alamat Email                         : ")
        no_telp = input("Masukkan nomor telepon                        : ")
        while no_telp.isdigit() == False:
            os.system("cls")
            print("Nomor telepon harus berupa angka".center(115))
            print(f"Nama Lengkap           : {nama_pengguna}\nEmail                  : {email}")
            no_telp = input("Masukkan nomor telepon : ")
        for cust in pelanggan.readcust(): 
            while len(no_telp) > 12:
                os.system("cls")
                print("Maaf, nomor telepon tidak boleh lebih dari 12 karakter".center(115))
                print(f"Nama Lengkap                              : {nama_pengguna}")
                email = input("Masukkan alamat Email                     : ")
                no_telp = input("Masukkan nomor telepon                    : ")
            while no_telp == cust[4] or email == cust[3]:
                os.system("cls")
                print("Email atau nomor telepon sudah terdaftar. Gunakan Email atau nomor telepon yang lain".center(115))
                print(f"Nama Lengkap                              : {nama_pengguna}")
                email = input("Masukkan alamat Email                     : ")
                no_telp = input("Masukkan nomor telepon                    : ")
        username = input("Masukkan username (digunakan saat login)      : ")
        for cust in pelanggan.readcust(): 
            while username == cust[0]:
                os.system("cls")
                print("Username sudah terdaftar. Gunakan nama lain sebagai username".center(115))
                print(f"Nama Lengkap      : {nama_pengguna}\nEmail             : {email}\nNomor Telepon     : {no_telp}") 
                username = input("Masukkan username : ")
        password = input("Masukkan password (Harus 8 Karakter)          : ")
        text = (f"Nama Lengkap      : {nama_pengguna}\nEmail             : {email}\nNomor Telepon     : {no_telp}\nUsername          : {username}")  
        while len(password) != 8:
            os.system("cls")
            print("Maaf, Password harus 8 karakter\n".center(115))
            print(text)
            password = input("Password          : ")
        os.system("cls")
        print("Apakah data yang kamu masukkan sudah benar?".center(115))
        konfirmasi_data = input((f"{text}\nPassword          : {password}\n\n|1| Benar\n|2| Salah\nPilih : "))
        if konfirmasi_data == "1":
            customer_baru = {'nama_pengguna': nama_pengguna, 'email': email, 'no_telp': no_telp, 'username': username, 'password': password}
            pelanggan.writecust(customer_baru)
            os.system("cls")
            input("Pendaftaran akun berhasil. Klik enter untuk lanjut => ")
            login()
        elif konfirmasi_data == "2":
            regist()
        else:
            input("Maaf, inputanmu salah. Klik enter untuk lanjut =>")
            regist()

def menuadmin():
    os.system("cls")
    print("Selamat datang di menu admin. Pilih menu yang kamu inginkan\n".center(115))
    menu_admin = input("|1| Tambah data petugas pernikahan\n|2| Hapus data petugas Pernikahan\n|3| Edit data petugas pernikahan\n|4| Konfirmasi Pembayaran Reservasi\nPilih => ")
    if menu_admin == "1":
        menu_tambahpetugas()
    elif menu_admin == "2":
        hapus_data_petugas()
    elif menu_admin == "3":
        menu_edit_petugas()
    elif menu_admin == "4":
        konfirmasi_pembayaran()
    else:
        input("Maaf, inputanmu salah. Klik enter untuk lanjut =>")
        menuadmin()

def menu_tambahpetugas():
    input_data_petugas()
    tambah_petugasbaru()

def input_data_petugas():
    os.system("cls")
    global petugas_baru, nama_petugas, telp_petugas, honorarium_petugas, jenis_petugas
    print("Tambah data petugas pernikahan".center(115))
    nama_petugas = input("Nama Petugas  : ")
    telp_petugas = input("Nomor Telepon Petugas : ")
    while (len(telp_petugas) > 12) or (telp_petugas.isdigit() == False):
        os.system("cls")
        print("Maaf, nomor telepon tidak boleh lebih dari 12 karakter dan harus berupa angka\n".center(115))
        telp_petugas = input(f"Nama Lengkap Petugas  : {nama_petugas}\nNomor Telepon Petugas : ")
    honorarium_petugas = input("Honorarium Petugas    : ")
    while honorarium_petugas.isdigit() is False:
        os.system("cls")
        print("Maaf, honorarium harus berupa angka\n".center(115))
        print(f"Nama Lengkap Petugas  : {nama_petugas}\nNomor Telepon Petugas : {telp_petugas}")
        honorarium_petugas = input("Honorarium Petugas    : ")
    jenis_petugas = input("Pilih jenis petugas :\n  a) MC\n  b) Tim Hadrah\n  c) Qori'\n  d) Mubaligh\n  Pilih: ")
    if jenis_petugas == "a":
        jenis_petugas = "1"
    elif jenis_petugas == "b":
        jenis_petugas = "2"
    elif jenis_petugas == "c":
        jenis_petugas = "3"
    elif jenis_petugas == "d":
        jenis_petugas = "4"
    else:
        input("Maaf, inputanmu salah. Klik enter untuk lanjut =>")
        input_data_petugas()
    petugas_baru = {'nama_petugas': nama_petugas, 'no_telp' : telp_petugas, 'Honorarium': honorarium_petugas, 'jenis_petugas' : jenis_petugas}
    
def tambah_petugasbaru():
    petugasnikah.writepetugas(petugas_baru)
    os.system("cls")
    input("Penambahan data petugas pernikahan berhasil\nKlik enter untuk lanjut => ".center(115))
    close()

def hapus_data_petugas():
    os.system("cls")
    print("Pilih data petugas yang ingin dihapus\n".center(115))
    data = petugasnikah.readpetugas()
    nomor = 1
    for petugas in data:
        print(f"{nomor}. Nama Lengkap Petugas  : {petugas[1]}\n   Nomor Telepon Petugas : {petugas[2]}\n   Honorarium Petugas    : {petugas[3]}\n   Jenis Petugas         : {petugas[4]}\n")
        nomor += 1
    data_dihapus = input("Pilih Petugas (Ketik nomornya) : ")
    while data_dihapus.isdigit() == False or int(data_dihapus) > len(data):
        os.system("cls")
        print("Maaf, inputan harus berupa angka. Klik enter untuk lanjut =>".center(115))
        hapus_data_petugas()
    id_dihapus = data[int(data_dihapus)-1][0]
    hapus = {'id' : id_dihapus}
    petugasnikah.deletepetugas(hapus)
    input("Penghapusan data petugas pernikahan berhasil\nKlik enter untuk lanjut => ".center(115))
    close()

def menu_edit_petugas():
    edit_data_petugas()
    update_petugas()

def edit_data_petugas():
    os.system("cls")
    print("Pilih data petugas yang ingin diubah\n".center(115))
    nomor = 1
    data = petugasnikah.readpetugas()
    for petugas in data:
        print(f"{nomor}. Nama Lengkap Petugas  : {petugas[1]}\n   Nomor Telepon Petugas : {petugas[2]}\n   Honorarium Petugas    : {petugas[3]}\n   Jenis Petugas         : {petugas[4]}\n")
        nomor+=1
    global id_edit
    data_diedit = input("Pilih Petugas (Ketik nomornya) : ")
    id_edit = data[int(data_diedit)-1][0]
    while data_diedit.isdigit() == False:
        os.system("cls")
        input("Maaf, inputan harus berupa angka. Klik enter untuk lanjut =>".center(115))
        edit_data_petugas()
    os.system("cls")
    print("Masukkan data petugas yang baru".center(115))
    input_data_petugas()
    
def update_petugas():
    petugas_baru['id'] = int(id_edit)
    petugasnikah.updatepetugas(petugas_baru)
    os.system("cls")
    input("Edit data petugas pernikahan berhasil\nKlik enter untuk lanjut => ".center(115))
    close()

def konfirmasi_pembayaran():
    data_konfirmasi()
    ubah_status()

def data_konfirmasi():    
    os.system("cls")
    print("Pilih data pembayaran yang ingin dikonfirmasi".center(115))
    nomor = 1
    for pembayaran in transaksi.datapembayaran():
        print(f"{nomor}. Nomor Reservasi       : {pembayaran[1]}\n   Waktu pembayaran      : {pembayaran[2]}\n   Nama Pemilik Rekening : {pembayaran[3]}\n   Status Konfirmasi     : {pembayaran[4]}\n")
        nomor += 1
    global pilih_konfirm
    pilih_konfirm = input("Pilih : ")
    while pilih_konfirm.isdigit() == False:
        input("Maaf, inputan harus berupa angka. Klik enter untuk lanjut =>".center(115))
        data_konfirmasi()

def ubah_status():
    os.system("cls")
    print(f"Konfirmasi pembayaran nomor {pilih_konfirm}".center(115))
    for pembayaran in transaksi.datapembayaran():
        if pembayaran[1] == int(pilih_konfirm):
            if pembayaran[4] != 'Sudah dikonfirmasi' and pembayaran[4] != 'Pembayaran ditolak':
                pilih_ubah = input("|1| Konfirmasi Pembayaran\n|2| Tolak Pembayaran\nPilih : ")
                while pilih_ubah.isdigit() == False:
                    input("Maaf, inputan harus berupa angka. Klik enter untuk lanjut =>".center(115))
                    ubah_status()
                if pilih_ubah == "1":
                    status = "Sudah dikonfirmasi" 
                elif pilih_ubah == "2":
                    status = "Pembayaran ditolak"
                data_ubah_status = {'id' : int(pilih_konfirm), 'status_konfirmasi' : status}
                transaksi.updatestatusbayar(data_ubah_status)
                os.system("cls")
                input(f"Konfirmasi pembayaran nomor {pilih_konfirm} berhasil\nKlik enter untuk lanjut => ".center(115))
                close()
            else:
                print("Maaf. Pembayaran sudah dikonfirmasi".center(115))
                pilih = input("|1| Konfirmasi pembayaran yang lain\n|2| Kembali ke menu utama\n|3| Keluar Aplikasi\nPilih => ")
                if pilih == "1":
                    konfirmasi_pembayaran()
                elif pilih == "2":
                    menuadmin()
                elif pilih == "3":
                    close()
                else:
                    input("Maaf, inputan tidak sesuai. Klik enter untuk lanjut => ".center(115))
                    ubah_status()

def menucust():
    os.system("cls")
    print("Selamat datang di NikMate App. Pilih menu yang kamu inginkan!".center(115))
    pilih_menu = input("|1| Buat reservasi baru\n|2| Cek reservasi sebelumnya\nPilih: ")
    if pilih_menu == "1":
        reservasi()
    elif pilih_menu =="2":
        pemesan()
        cek_reservasi()
    while pilih_menu.isdigit() == False and pilih_menu != "1":
        input("Maaf, inputan harus berupa angka. Klik enter untuk lanjut =>".center(115))
        os.system("cls")
        menucust()

def reservasi():
    admin_bertugas()
    pemesan()
    data_pengantin()
    data_paket()
    data_waktu()
    data_petugas()
    jumlah_undangan()

def data_pengantin():
    os.system("cls")
    print("Masukkan data pengantin dengan benar".center(115))
    global nama_pengantin_pria, nama_pengantin_wanita
    nama_pengantin_pria = input("Nama Pengantin Pria   : ")
    nama_pengantin_wanita = input("Nama Pengantin Wanita : ")

def data_paket():
    global paket_nikah, nama_paket
    os.system("cls")
    print("Pilih paket yang kamu inginkan".center(115))
    for paket in paketnikah.readpaket():
        print(f"{paket[0]}. Paket {paket[3]}\n   Ruangan   : {paket[1]}\n   Fasilitas : {paket[4]}\n   Harga     : {paket[2]}\n")
    pilih_paket = input("Pilih => ")
    while not pilih_paket.isdigit() or int(pilih_paket) not in [paket[0] for paket in paketnikah.readpaket()]:
        input("Maaf, inputan harus berupa angka yang sesuai dengan salah satu paket\nKlik enter untuk lanjut =>".center(115))
        os.system("cls")
        data_paket()
    for paket in paketnikah.readpaket():
        paket_nikah = int(pilih_paket)
        if paket[0] == paket_nikah:
            nama_paket = paket[3]
            break
    print(nama_paket)

def data_waktu():
    global waktu_akad
    os.system("cls")
    print("Pilih waktu pernikahan".center(115))
    tahun = int(input("Tahun (isi menggunakan angka)   : "))
    bulan = int(input("Bulan (isi menggunakan angka)   : "))
    hari = int(input("Tanggal (isi menggunakan angka) : "))
    pilih_hari = datetime(tahun, bulan,hari)
    acara = []
    for data in transaksi.riwayatreservasi():
        if pilih_hari.date() == data[2].date() and data[8] != "Pembayaran ditolak":
            waktu = data[2].strftime("%H:%M:%S")
            acara.append(waktu)
    jam_akad = ['08:00:00', '10:00:00', '13:00:00']
    nomor = 1
    pilihan_jam = []
    if len(acara) <= 2:
        pilihan_jam = [jam for jam in jam_akad if jam not in acara]
        if pilihan_jam:
                print("Pilihan Jam : ")
                for nomor, jam in enumerate(pilihan_jam, start=1):
                    print(f"  {nomor}. {jam}")
                pilih_jam = input("Pilih => ")
                if pilih_jam.isdigit() and 1 <= int(pilih_jam) <= len(pilihan_jam):
                    jam = pilihan_jam[int(pilih_jam) - 1]
                else:
                    input("Maaf, inputan harus berupa angka. Pilih salah satu jam\nKlik enter untuk lanjut =>".center(115))
                    data_waktu()
                waktu_nikah = datetime.combine(pilih_hari.date(), datetime.strptime(jam, "%H:%M:%S").time())
                waktu_akad = waktu_nikah.strftime("%Y-%m-%d %H:%M:%S")
    else:    
        print("Maaf, jadwal pada hari ini tidak tersedia. Cobalah untuk mengganti hari atau paketnya".center(115))
        pilih_kembali = input("|1| Ganti Paket\n|2| Ganti Tanggal\n|3| Batalkan Reservasi\n Pilih => ")
        if pilih_kembali == "1":
            data_paket()
            data_waktu()
        elif pilih_kembali == "2":
            data_waktu()
        elif pilih_kembali == "3":
            close()
        else:
            input("Maaf, inputan tidak sesuai. Klik enter untuk lanjut => ")
            data_waktu()
            
def data_petugas():
    os.system("cls")
    print("Pilih petugas pernikahan".center(115))
    print("-Petugas MC -".center(115))
    nomor = 1
    list_mc = petugasnikah.petugasmc()
    list_hadrah = petugasnikah.petugashadrah()
    list_mubaligh = petugasnikah.petugasmubaligh()
    list_qori = petugasnikah.petugasqori()
    global mc_akad, hadrah_akad, mubaligh_akad, qori_akad, id_mc, id_hadrah, id_mubaligh, id_qori
    for mc in list_mc:
        print(f"{nomor}. {mc[1]}")
        nomor += 1
    pilih_mc = input("Pilih => ")
    while pilih_mc.isdigit == False or int(pilih_mc) > len(list_mc):
        input("Maaf, inputan harus berupa angka. Pilih salah satu petugas\nKlik enter untuk lanjut => ")
        data_petugas()
    data_mc = {'jenis_petugas':"MC", 'id_sekarang': int(pilih_mc)}
    id_mc = petugasnikah.panggilidpetugas(data_mc)
    mc_akad = list_mc[int(pilih_mc) - 1][1]
    os.system("cls")
    print("Pilih petugas pernikahanmu 🤗".center(115))
    print("-Petugas Hadrah -".center(115))
    nomor = 1
    for hadrah in list_hadrah:
        print(f"{nomor}. Tim {hadrah[1]}")
        nomor += 1
    pilih_hadrah = input("Pilih => ")
    while pilih_hadrah.isdigit == False or int(pilih_hadrah) > len(list_hadrah):
        input("Maaf, inputan harus berupa angka. Pilih salah satu petugas\nKlik enter untuk lanjut => ")
        data_petugas()
    data_hadrah = {'jenis_petugas':"Tim Hadrah", 'id_sekarang': int(pilih_hadrah)}
    id_hadrah = petugasnikah.panggilidpetugas(data_hadrah)
    hadrah_akad = list_hadrah[int(pilih_hadrah) - 1][1]
    os.system("cls")
    print("Pilih petugas pernikahanmu 🤗".center(115))
    print("-Petugas Mubaligh -".center(115))
    nomor = 1
    for mubaligh in list_mubaligh:
        print(f"{nomor}. {mubaligh[1]}")
        nomor += 1
    pilih_mubaligh = input("Pilih => ")
    while pilih_mubaligh.isdigit == False or int(pilih_mubaligh) > len(list_mubaligh):
        input("Maaf, inputan harus berupa angka. Pilih salah satu petugas\nKlik enter untuk lanjut => ")
        data_petugas()
    data_mubaligh = {'jenis_petugas':"Mubaligh", 'id_sekarang': int(pilih_mubaligh)}
    id_mubaligh = petugasnikah.panggilidpetugas(data_mubaligh)
    mubaligh_akad = list_mubaligh[int(pilih_mubaligh) - 1][1]
    os.system("cls")
    print("Pilih petugas pernikahanmu 🤗".center(115))
    print("-Petugas Qori' -".center(115))
    nomor = 1
    for qori in list_qori:
        print(f"{nomor}. {qori[1]}")
        nomor += 1
    pilih_qori = input("Pilih => ")
    while pilih_qori.isdigit == False or int(pilih_qori) > len(list_qori):
        input("Maaf, inputan harus berupa angka. Pilih salah satu petugas\nKlik enter untuk lanjut => ")
        data_petugas()
    data_qori = {'jenis_petugas':"Qori", 'id_sekarang': int(pilih_qori)}
    id_qori = petugasnikah.panggilidpetugas(data_qori)
    qori_akad = list_qori[int(pilih_qori) - 1][1]

def pemesan():
    global pengguna_memesan, nama_pengguna
    data_pengguna = pelanggan.readcust()
    for pengguna in data_pengguna:
        if pengguna[0] == username:
            pengguna_memesan = pengguna[5]
            nama_pengguna = pengguna[0]

def admin_bertugas():
    global next_admin
    data_admin = admin.readadmin()
    reservasi = transaksi.bacareservasi()
    total_admin = len(data_admin)
    if reservasi:
        last_admin = reservasi[-1][8]
        next_admin = (last_admin % total_admin) + 1
    else:
        next_admin = 1   

def data_pembayaran():
    os.system("cls")
    print("Pembayaran".center(115))
    print("Lakukan pembayaran pada nomor rekening 012344321 (BCA) an. Yayasan Masjid Jami' Al-Baitul Amien Jember".center(115))
    print("Reservasi tidak akan tersimpan sebelum melakukan transfer\n".center(115))
    for harga in paketnikah.readpaket():
        if harga[0] == paket_nikah:
            print(f"Total Pembayaran : {harga[4]}")
            break
    input("Klik enter apabila telah melakukan transfer => ")
    global wkt_tf, pemilik_rek
    wkt_tf = datetime.now()
    waktu_tf = wkt_tf.strftime("%Y-%m-%d %H:%M:%S")
    pemilik_rek = input("Masukkan nama pemilk rekening yang digunakan untuk transfer : ")
    data_pembayaran = {'waktu_pembayaran' : waktu_tf, 'nama_pemilik_rekening' : pemilik_rek, 'status_konfirmasi': 'Belum dikonfirmasi'}
    transaksi.tambahpembayaran(data_pembayaran)
    tambahkanreservasi()

def tambahkanreservasi():
    os.system("cls")
    pembayaran = transaksi.bacapembayaran()
    last_pembayaran = pembayaran[-1][0]
    wkt_reservasi = datetime.now()
    waktu_reservasi = wkt_reservasi.strftime("%Y-%m-%d %H:%M:%S")
    data_reservasi = {'waktu_reservasi': waktu_reservasi, 'waktu_akad_nikah' : waktu_akad, 'catatan_pengantin': catatan, 'jumlah_undangan' : undangan_akad, 'nama_pengantin_pria' : nama_pengantin_pria, 'nama_pengantin_wanita' : nama_pengantin_wanita, 'id_paket' : paket_nikah, 'id_admin': next_admin, 'id_pembayaran' : last_pembayaran, 'id_pengguna' : pengguna_memesan}
    transaksi.tambahreservasi(data_reservasi)
    print("Selamat! Reservasi berhasil dilakukan 🙌".center(115))
    input("Klik enter untuk melanjutkan => ")
    tambahpetugas()
    close()

def tambahpetugas():
    reservasi = transaksi.bacareservasi()
    last_reservasi = reservasi[-1][0]
    id_petugas = [id_mc, id_hadrah, id_mubaligh, id_qori]
    for petugas in id_petugas:
        detail_petugas = {'id_reservasi': last_reservasi, 'id_petugas':petugas}
        petugasnikah.tambahkedetail(detail_petugas)

def jumlah_undangan():
    os.system("cls")
    global undangan_akad
    print("Jumlah Undangan\n".center(115))
    undangan_akad = input("Masukkan jumlah undangan yang hadir di acara akad nikah (Maksimal 100 orang) : ")
    if int(undangan_akad) <= 100:
        catatan_pengantin()
    else:
        input("Inputan tidak sesuai. Jumlah undangan tidak boleh lebih dari 100 orang. Klik enter untuk lanjut => ")
        jumlah_undangan()

def catatan_pengantin():
    os.system("cls")
    print("Catatan Pengantin".center(115))
    print("Isi dengan tanda '-' apabila tidak ingin menambah catatan\n".center(115))
    global catatan
    catatan = input("Catatan (Contoh: Tolong pakai bunga melati di meja akad): ")
    konfirmasi_reservasi()

def konfirmasi_reservasi():
    os.system("cls")
    print("Konfirmasi reservasi".center(115))
    print(f"Nama pengantin pria        : {nama_pengantin_pria}\nNama Pengantin Wanita      : {nama_pengantin_wanita}\nWaktu akad nikah           : {waktu_akad}\nPaket Pernikahan           : Paket {nama_paket}\nJumlah Undangan            : {undangan_akad}\nCatatan                    : {catatan}\nPetugas Pernikahan         : \n  MC         : {mc_akad}\n  Tim Hadrah : {hadrah_akad}\n  Mubaligh   : {mubaligh_akad}\n  Qori'      : {qori_akad}\n")
    pilih_konfirm = input("|1| Konfirmasi Reservasi\n|2| Ganti nama pengantin\n|3| Ganti Paket Pernikahan\n|4| Ganti Waktu Pernikahan\n|5| Ganti Petugas Pernikahan\n|6| Ubah Jumlah Undangan \n|7| Ubah catatan \n|8| Batalkan Reservasi\nPilih => ")
    if pilih_konfirm == "1":
        data_pembayaran()
    elif pilih_konfirm == "2":
        data_pengantin()
        konfirmasi_reservasi()
    elif pilih_konfirm == "3":
        data_paket()
        konfirmasi_reservasi()
    elif pilih_konfirm == "4":
        data_waktu()
        konfirmasi_reservasi()
    elif pilih_konfirm == "5":
        data_petugas()
        konfirmasi_reservasi()
    elif pilih_konfirm == "6":
        jumlah_undangan()
        konfirmasi_reservasi()
    elif pilih_konfirm == "7":
        catatan_pengantin()
        konfirmasi_reservasi()
    elif pilih_konfirm == "8":
        close()
    else: 
        input("Maaf, inputan tidak valid. Klik enter untuk lanjut => ")
        konfirmasi_reservasi()

def cek_reservasi():
    os.system("cls")
    nomor = 1
    print("Riwayat Reservasi".center(115))
    print("Harap lakukan reservasi ulang atau hubungi CP 085806500458 (Fadlan) apabila pembayaran anda ditolak\n".center(115))
    for reservasi in transaksi.riwayatreservasi():
        if nama_pengguna == reservasi[9]:
            print(f"{nomor}. Nama Pengantin    : {reservasi[5]}\n   Waktu Reservasi   : {reservasi[1]}\n   Waktu Akad Nikah  : {reservasi[2]}\n   Nama Paket        : Paket {reservasi[6]}\n   Jumlah Undangan   : {reservasi[4]}\n   Catatan           : {reservasi[3]}\n   Status Konfirmasi : {reservasi[8]}\n   MC                : {petugasnikah.detailpetugas({'id_reservasi' : reservasi[0], 'jenis_petugas': 'MC'})}\n   Tim Hadrah        : {petugasnikah.detailpetugas({'id_reservasi' : reservasi[0], 'jenis_petugas': 'Tim Hadrah'})}\n   Mubaligh          : {petugasnikah.detailpetugas({'id_reservasi' : reservasi[0], 'jenis_petugas': 'Mubaligh'})}\n   Qori'             : {petugasnikah.detailpetugas({'id_reservasi' : reservasi[0], 'jenis_petugas': 'Qori'})}\n")
            nomor += 1
        else:
            continue
    if nomor == 1:
        print("Maaf. Kamu belum pernah melakukan reservasi\n")
    pilih_keluar = input("|1| Kembali ke menu utama\n|2| Keluar dari aplikasi\nPilih => ")
    if pilih_keluar == "1":
        menucust()
    elif pilih_keluar == "2":
        close()
    else: 
        input("Maaf, inputan tidak valid. Klik enter untuk lanjut => ")
        cek_reservasi()

def close():
    os.system("cls")
    print("Apakah kamu ingin keluar dari aplikasi?\n".center(115))
    pilih_close = input("|1| Ya\n|2| Tidak, kembali ke menu utama\nPilih: ")
    while pilih_close.isdigit() == False:
        os.system("cls")
        print("Maaf, inputan harus berupa angka. Klik enter untuk lanjut =>\n".center(115))
        pilih_close = input("|1| Ya\n|2| Tidak, kembali ke menu utama\nPilih: ")
    if pilih_close == "1":
        os.system("cls")
        print("Terima kasih telah menggunakan aplikasi NikMate. See You 👋".center(115))
    elif pilih_close == "2":
        menucust() if user == "1" else menuadmin()
    
def home():
    os.system("cls")
    print("Hai! Selamat Datang di NikMate App 👋".center(115))
    print("|1| Masuk sebagai customer\n|2| Masuk sebagai admin")
    global user
    user = input("Pilih: ")
    if user == "1":
        punyaakun()
    elif user == "2":
        login()
    else: 
        input('Yah, yang kamu masukkan salah. Coba lagi yuk🙌\nTekan enter untuk lanjut => ')
        os.system("cls")
        home()
home()
