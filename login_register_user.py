#-----------------------------------------
# Created By : Dony a.k.a scioss.
# SISTEM LOGIN SEDERHANA
#-----------------------------------------
import json
import time

data_user = []

fileName = "data_pengguna.json"

try:
    with open(fileName, 'r') as file:
        data_user = json.load(file)
    print("sukses load data")
except (FileNotFoundError, json.JSONDecodeError):
    print("file tidak ditemukan atau data tercorrupt, memakai list kosong.")


email = ['@gmail.com', '@outlook.com', '@yahoo.com', '@std.trisakti.ac.id', '@mail.com']

isTrue = True

def create_user():

    while True:
        print("\nRegister User\n")
        username = input("Masukan Username : ")
        if username.isdigit():
            print("Nama Tidak Valid")
            continue

    
        emails = input("Masukan Email : ")
        emailValid = True
        for ending in email:
            if emails.endswith(ending):
                emailValid = True
                break
            if not emails.endswith(ending):
                emailValid = False
                continue
        if not emailValid:
            print("Email Tidak Valid")
            continue

        password = input("Masukan Password : ")
        
        existUser = None
        for user in data_user:
            if user['nama'] == username:
                
                existUser = user
                break
            elif user['email'] == emails:
                
                existUser = user
                break
        if existUser:
            print("Data yang anda masukan sudah ada!")
            print("Silahkan masukan data yang lain")
            continue 
        else:
            user = {'nama': username, 'email': emails, 'password': password}
            data_user.append(user)
            print("Berhasil mendaftarkan pengguna {}!".format(username))
            break

def login():
    while isTrue:
        print("\nLogin User\n")
        username = input("Masukan Username : ")
        password = input("Masukan Password : ")
        loginSuccess = False
        for user in data_user:
            if user['nama'] == username and user['password'] == password:
                print("Berhasil Login!")
                print("Selamat Datang {}".format(user['nama']))
                loginSuccess = True
                break
        if not loginSuccess:
            print("User tidak dapat ditemukan.")
            print("Silahkan Login ulang atau Register User baru!")
            continue
        break



def edit_user():
    while True:
        print("\nEdit User\n")
        username = input("Masukan Username : ")
        password = input("Masukan Password : ")
        userFound = False
        for user in data_user:
            if user['nama'] == username and user['password'] == password:
                userFound =  True
                print("User ditemukan!")
                print("Silahkan pilih")
                print("a.) Edit Nama : ")
                print("b.) Edit Email : ")
                print("c.) Edit Password : ")
                opsi = input("Masukan Opsi a/b/c : ").lower()
                while opsi == "a":
                    usernameBaru = input("Masukan Username Baru : ")
                    user['nama'] = usernameBaru
                    existUser = None
                    isBenar = False
                    for user in data_user:
                        if user['nama'] == usernameBaru:
                            
                            
                            existUser = user
                            break

                    if not existUser:
                        print("Username sudah digunakan oleh orang lain!")
                        continue
                    else:
                        for user in data_user:
                            if user == existUser:
                                user['nama'] = usernameBaru
                                break
                        print("Username Berhasil Diganti")
                        break
            

                
                    
                while opsi == "b":
                    
                        emailBaru = input("Masukan Email Baru : ")
                        user['email'] = emailBaru
                        for ending in email:
                            if emailBaru.endswith(ending):
                                isBenar = True
                                print("Email Berhasil di-ganti!")
                                break
                        if not isBenar:
                            print("Email Tidak Valid!")
                            continue
                        break
                
                if opsi == "c":
                    passwordBaru = input("Masukan Password Baru : ")
                    user['password'] = passwordBaru
                    print("Password Telah Diperbarui.")
                    isTrue = True
                    break
        if not userFound:
            print("Data tidak valid")
            break
        
        break

def list_user():
    print("\nList Data User\n")
    
    for idx, user in enumerate(data_user, start=1):
        print("{}- {}".format(idx, user['nama']))

def hapus_akun():
    while True:
        username = input("Masukan Username : ")
        emails = input("Masukan Email : ")
        password = input("Masukan Password : ")
        akunDitemukan = False
        for user in data_user:
            if user['nama'] == username and user['password'] == password and user['email'] == emails:
                akunDitemukan = True
                print("User ditemukan")
                hapusAkun = input("Hapus akun ini? y/n : ")
                if hapusAkun.lower() == "y":
                    data_user.remove(user)
                    print("Akun Telah dihapus!")
                else:
                    break
        if not akunDitemukan:
            print("Akun tidak ditemukan!")
            continue

        break

def lupa_password():
    emails = input("Masukan Email : ")
    dataValid = False
    for user in data_user:
        if user['email'] == emails:
            dataValid = True
            print("User ditemukan!")
            newPass = input("Masukan Password Baru : ")
            user['password'] = newPass
            break
    if not dataValid:
        print("User dengan email tersebut tidak ditemukan!")

def list_user_admin():
    print("\nList Data User\n")
    
    for idx, user in enumerate(data_user, start=1):
        print("{}- Nama : {}, Email : {}, Password : {} ".format(idx, user['nama'], user['email'], user['password']))

def showMenu():
    while True:  
        print("===Menu===")
        print("1.) Register >>")
        print("2.) Login >>")
        print("3.) Edit User >>")
        print("4.) Hapus User >>")
        print("5.) Lupa Password >>")
        print("6.) List User >>")
        print("7.) Keluar")
        print("===OPSI===")
        opsi = input(">> ")

        if opsi == "1":
            create_user()
        elif opsi == "2":
            login()
        elif opsi == "3":
            edit_user()
        elif opsi == "4":
            hapus_akun()
        elif opsi == "5":
            lupa_password()
        elif opsi == "6":
            list_user()
        elif opsi == "7":
            with open(fileName, "w") as file:
                json.dump(data_user, file)
            print("sukses menyimpan data")
            time.sleep(1)
            print("Otomatis Keluar dalam 10 detik.")
            time.sleep(10)
            break
        elif opsi == "Admin":
            list_user_admin()
        else:
            print("Opsi tidak valid!")


if __name__ == "__main__":
    showMenu()
    time.sleep(1)
