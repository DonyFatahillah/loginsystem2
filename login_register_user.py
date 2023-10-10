#-----------------------------------------
# Created By : Dony a.k.a scioss.
# SISTEM LOGIN SEDERHANA
# BESERTA MENU MENU OPERASI
#-----------------------------------------

import json
import time
import os

data_user = []

fileName = "data_pengguna.json"

def clear():
    os.system('cls' if os.name == "nt" else "clear")

try:
    with open(fileName, 'r') as file:
        data_user = json.load(file)
    print("sukses load data")
    clear()
except (FileNotFoundError, json.JSONDecodeError):
    print("file tidak ditemukan atau data tercorrupt, memakai list kosong.")


email = ['@gmail.com', '@outlook.com', '@yahoo.com', '@std.trisakti.ac.id', '@mail.com']

isTrue = True

def create_user():

    while True:
        print("\n===Register User===\n")
        username = input("Masukan Username : ")
        if username.isdigit():
            print("Nama Tidak Valid")
            continue

    
        emails = input("Masukan Email : ").lower()
        emailValid = True
        for ending in email:
            if emails.endswith(ending):
                emailValid = True
                break
            if not emails.endswith(ending):
                emailValid = False
                continue
        if not emailValid:
            clear()
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
            clear()
            print("Data yang anda masukan sudah ada!")
            print("Silahkan masukan data yang lain")
            continue 
        else:
            clear()
            user = {'nama': username, 'email': emails, 'password': password, 'permission': 'default'}
            data_user.append(user)           
            print("Berhasil mendaftarkan pengguna {}!".format(username))
            mainMenu2()
            break

def login():
    while isTrue:
        print("\n======Login User======\n")
        username = input("Masukan Username : ")
        password = input("Masukan Password : ")
        loginSuccess = False
        for user in data_user:
            if user['nama'] == username and user['password'] == password:
                clear()
                if user['permission'] == 'Admin':
                    print("Berhasil Login!")
                    print("Selamat Datang admin {}".format(user['nama']))
                    loginSuccess = True
                    mainMenuAsAdmin()
                    break
                else:
                    print("Berhasil Login!")
                    print("Selamat Datang {}".format(user['nama']))
                    loginSuccess = True
                    mainMenu2()
                    break
            
        if not loginSuccess:
            clear()
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
    
    while True:
        print("====List Data User====\n")
        
        for idx, user in enumerate(data_user, start=1):
            print("{}- {}".format(idx, user['nama']))
        keluar = input("Keluar dari tampilan ini? (y/n) : ").lower()
        if keluar == "y":
            break
        else:
            continue

def hapus_akun():
    while True:
        print("====Hapus Akun====\n")
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
    while True:
        username = input("Masukan Username Admin : ")
        isAdmin = False
        for user in data_user:
            if user['nama'] == username:
                if user.get('permission') == 'Admin':
                    isAdmin = True
                    print("\nList Data User\n")
                    
                    for idx, user in enumerate(data_user, start=1):
                        print("{}- Nama : {}, Email : {}, Password : {}, Permission : {} ".format(idx, user['nama'], user['email'], user['password'], user['permission']))
        keluar = input("Keluar dari tampilan ini? (y/n) : ").lower()
        if keluar == "y":
            break
        else:
            continue
        
    if not isAdmin:
        print("User is not An Admin")
        
def list_user_admin2():
    while True:
        print("\nList Data User\n")
                    
        for idx, user in enumerate(data_user, start=1):
            print("{}- Nama : {}, Email : {}, Password : {}, Permission : {} ".format(idx, user['nama'], user['email'], user['password'], user['permission']))
        keluar = input("Keluar dari tampilan ini? (y/n) : ").lower()
        if keluar == "y":
            break
        else:
            continue    


def calculator():
    print("\nCalculator\n")

    operators = set(['+', '-', '*', '/', '^', '%'])

    def is_operator(string):
        return string in operators

    while True:        
        angka = input(">>> ").strip()
        
        if angka.lower() == 'exit':
            break

        if angka.isdigit() or is_operator(angka) or not angka.isdigit():
            valid_angka = angka.replace("x", "*").replace(":", "/").replace("=", "").replace("^", "**")
            try:
                hasil = eval(valid_angka)
                hasil2 = str(valid_angka.replace("**", "^").replace("/", ":").replace("*", "x"))
                print(f"Hasil dari {hasil2} = {hasil:.0f}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Input tidak valid!")

        keluar = input("Keluar? (y/n): ").lower()
        if keluar == "y":
            break
    clear()
  
def konversiSuhu():
    while True:
        suhu = input("masukan jenis suhu celcius (C), fahrenheit (F), reamur (R), kelvin (K)= ").lower()

        if suhu in ("c", "celcius"):
            angkaSuhu = (input("masukan suhu celcius : "))

            if angkaSuhu.isalpha():
                print("masukan angka yang valid!")
                continue

            celcius = int(angkaSuhu)

            print("""
    konversi suhu
    a.) fahrenheit
    b.) reamur
    c.) kelvin
            """)

            opsi = input("masukan opsi : ")

            if opsi == "a":
                fahrenheit = (9/5) * celcius + 32
                print(f"celcius '{celcius}' ke fahrenheit adalah {fahrenheit}")
            elif opsi == "b":
                reamur = (4/5) * celcius
                print(f"celcius '{celcius}' ke reamur adalah {reamur}")
            elif opsi == "c":
                kelvin = celcius + 273
                print(f"celcius '{celcius}' ke kelvin adalah {kelvin}")
            else:
                print("opsi tidak valid!")

        elif suhu in ("f", "fahrenheit"):
            angkaSuhu = (input("masukan suhu fahrenheit : "))
            if angkaSuhu.isalpha():
                print("masukan angka yang valid!")
                continue

            fahrenheit = int(angkaSuhu)

            print("""
    konversi suhu
    a.) celcius
    b.) reamur
    c.) kelvin
            """)

            opsi = input("masukan opsi : ")

            if opsi == "a":
                celcius = 5/9 * (fahrenheit - 32)
                print(f"fahrenheit '{fahrenheit}' ke celcius adalah {celcius}")
            elif opsi == "b":
                reamur = 4/9 * (fahrenheit - 32)
                print(f"fahrenheit '{fahrenheit}' ke reamur adalah {reamur}")
            elif opsi == "c":
                kelvin = 5/9 * (fahrenheit - 32) + 273
                print(f"fahrenheit '{fahrenheit}' ke kelvin adalah {kelvin}")
            else:
                print("opsi tidak valid!")

        elif suhu in ("r", "reamur"):
            angkaSuhu = (input("masukan suhu reamur : "))

            if angkaSuhu.isalpha():
                print("masukan angka yang valid!")
                continue

            reamur = int(angkaSuhu)

            print("""
    konversi suhu
    a.) celcius
    b.) fahrenheit
    c.) kelvin
            """)
            
            opsi = input("masukan opsi : ")

            if opsi == "a":
                celcius = (5/4) * reamur
                print(f"reamur '{reamur}' ke celcius adalah {celcius}")
            elif opsi == "b":
                fahrenheit = (9/4) * reamur + 32
                print(f"reamur '{reamur}' ke fahrenheit adalah {fahrenheit}")
            elif opsi == "c":
                kelvin = (5/4) * reamur + 273
                print(f"reamur '{reamur}' ke kelvin adalah {kelvin}")
            else:
                print("opsi tidak valid!")

        elif suhu in ("k", "kelvin"):
            angkaSuhu = (input("masukan suhu kelvin : "))

            if angkaSuhu.isalpha():
                print("masukan angka yang valid!")
                continue

            kelvin = int(angkaSuhu)

            print("""
    konversi suhu
    a.) celcius
    b.) fahrenheit
    c.) reamur
            """)

            opsi = input("masukan opsi : ")

            if opsi == "a":
                celcius = kelvin - 273
                print(f"kelvin '{kelvin}' ke celcius adalah {celcius}")
            elif opsi == "b":
                fahrenheit = 9/5 * (kelvin - 273) + 32
                print(f"kelvin '{kelvin}' ke fahrenheit adalah {fahrenheit}")
            elif opsi == "c":
                reamur = 4/5 * (kelvin - 273)
                print(f"kelvin '{kelvin}' ke reamur adalah {reamur}")
            else:
                print("opsi tidak valid!")
        else:
            print("opsi tidak valid!")
            continue

        ulangi = input("ulangi program? (y/n) : ")
        if ulangi.lower() != "y":
            break

def binarycode():
    while True:
        print("===PROGRAM KONVERSI BILANGAN===")
        print("1.) Angka Ke Biner >> ")
        print("2.) Biner Ke Angka >> ")
        print("3.) Exit")
        opsi = input("Opsi : ")


        while opsi.isdigit() and opsi == "1":
            angka = int(input("Masukan Angka : "))

            print(f"{angka} ke Biner adalah {format(angka, 'b')}")
            leave = input("kembali ke menu? y/n : ").lower()
            if leave in ("y", "yes"):
                break
            elif leave in ("n", "no"):
                continue
            else:
                break

        while opsi.isdigit() and opsi == "2":
            biner = input("Masukan Angka Biner : ")

            binerInt = int(biner, 2)

            print(f"{biner} ke Angka adalah {int(binerInt)} ")
            if leave in ("y", "yes"):
                break
            elif leave in ("n", "no"):
                continue
            else:
                break
        if opsi.isdigit() and opsi == "3":
            print("Terimakasih Sudah Menggunakan Program ini <3 *muach")
            break 
        
    
def pytagoras():
    
    while True:
        import math
        print("""
            
Kalkulator Pytagoras
            
a.) hitung sisi A <>
b.) hitung sisi B <>
c.) hitung sisi C <>
    """)

        opsi = input("Masukan opsi : ").lower()

        if opsi == "a":

            b = input("masukan angka b : ")
            c = input("masukan angka c : ")

            if not b.isdigit() or not c.isdigit():
                print("\nmasukan angka, bukan huruf.")
                continue
            angkaB = float(b)
            angkaC = float(c)
            if angkaC < angkaB:
                print("c harus lebih besar dari b")
                continue
            hitungA = math.sqrt(angkaC**2 - angkaB**2)

            print(f"hasilnya, sisi a adalah {hitungA}")
            

        elif opsi == "b":

            a = input("masukan angka a : ")
            c = input("masukan angka c : ")

            if not a.isdigit() or not c.isdigit():
                print("\nmasukan angka, bukan huruf.")
                continue
            angkaA = float(a)
            angkaC = float(c)
            if angkaC < angkaA:
                print("c harus lebih besar dari a")
                continue
            hitungB = math.sqrt(angkaC**2 - angkaA**2)
            print(f"hasilnya, sisi b adalah {hitungB}")

        elif opsi == "c":

            a = input("masukan angka a : ")
            b = input("masukan angka b : ")

            if not a.isdigit() or not b.isdigit():
                print("\nmasukan angka, bukan huruf.")
            angkaA = float(a)
            angkaB = float(b)

            hitungC = math.sqrt(angkaA**2 + angkaB**2)
            print(f"hasilnya, sisi c adalah {hitungC}")
        else:
            print("opsi tidak valid!")

        ulangi = input("ulangi proses? (y/n) : ")
        if ulangi.lower() in ("n", "no"):
            break

        if ulangi.lower() in ("y", "yes"):
            continue

        else:
            break
        
def mainMenu():
    while True:
        print("===OPSI===")
        print("a.) Calculator >>")
        print("b.) Pytagoras >>")
        print("c.) Konversi Suhu >>")
        print("d.) Binary Conversion >>")
        print("=========")
        print("0.) Exit")
        print("=========")
        opsi = input(">> ").lower()
        
        if opsi == "a": 
            clear()          
            calculator()
            break
        elif opsi == "b":
            clear()
            pytagoras()           
            break
        elif opsi == "c":
            clear()
            konversiSuhu()            
            break
        elif opsi == "d":
            clear()
            binarycode()
            break
        elif opsi == "0":
            clear()
            mainMenu2()
            break

def mainMenuAdmin():
    while True:
        print("===OPSI===")
        print("a.) Calculator >>")
        print("b.) Pytagoras >>")
        print("c.) Konversi Suhu >>")
        print("d.) Binary Conversion >>")
        print("=========")
        print("0.) Exit")
        print("=========")
        opsi = input(">> ").lower()
        
        if opsi == "a": 
            clear()          
            calculator()
            break
        elif opsi == "b":
            clear()
            pytagoras()           
            break
        elif opsi == "c":
            clear()
            konversiSuhu()            
            break
        elif opsi == "d":
            clear()
            binarycode()
            break
        elif opsi == "0":
            clear()
            mainMenuAsAdmin()
            break
            
def mainMenu2():
    while True:
        print("===Menu===")
        print("1.) Edit User >>")
        print("2.) Hapus User >>")
        print("3.) Menu >>")
        print("4.) List User >>")
        print("=========")
        print("0.) Keluar >>")
        print("==========")
        opsi = input(">> ")
        
        if opsi == "1":
            clear()
            edit_user()
            continue
        elif opsi == "2":
            clear()
            hapus_akun()
            showMenu()
        elif opsi == "3":
            clear()
            mainMenu()
            
        elif opsi == "4":
            clear()
            list_user()
            continue
        elif opsi == "0":
            clear()
            showMenu()
            break
        else:
            print("Opsi tidak valid")
            break
        break

def mainMenuAsAdmin():
    while True:
        print("===Menu===")
        print("1.) Edit User >>")
        print("2.) Hapus User >>")
        print("3.) Menu >>")
        print("4.) List User >>")
        print("5.) List User (Admin) >>")
        print("=========")
        print("0.) Keluar >>")
        print("==========")
        opsi = input(">> ")
        
        if opsi == "1":
            clear()
            edit_user()
            continue
        elif opsi == "2":
            clear()
            hapus_akun()
            showMenu()
        elif opsi == "3":
            clear()
            mainMenuAdmin()
            continue
        elif opsi == "4":
            clear()
            list_user()
            continue
        elif opsi ==  "5":
            clear()
            list_user_admin2()
            clear()
            continue
        elif opsi == "0":
            clear()
            showMenu()
            break
        else:
            print("Opsi tidak valid")
            break
        break

def showMenu():
    while True:  
        print("===Menu===")
        print("1.) Register >>")
        print("2.) Login >>")
        print("3.) Edit User >>")
        print("4.) Hapus User >>")
        print("5.) Lupa Password >>")
        print("6.) List User >>")
        print("=========")
        print("0.) Keluar >>")
        print("==========")
        opsi = input(">> ")

        if opsi == "1":
            clear()
            create_user()
            time.sleep(2)
            clear()
            continue
            
        elif opsi == "2":
            clear()
            login()
            time.sleep(2)
            clear()
        elif opsi == "3":
            clear()
            edit_user()
            time.sleep(2)
            clear()
            continue
        elif opsi == "4":
            clear()
            hapus_akun()
            time.sleep(2)
            clear()
            continue
        elif opsi == "5":
            clear()
            lupa_password()
            time.sleep(2)
            clear()
            continue
        elif opsi == "6":
            clear()
            list_user()
            time.sleep(2)
            clear()
            continue
        elif opsi == "0":
            with open(fileName, "w") as file:
                json.dump(data_user, file)
            print("sukses menyimpan data")
            print("Otomatis Keluar dalam 5 detik.")
            clear()

            break
                    
        elif opsi == "Admin":
            clear()
            list_user_admin()
            time.sleep(2)
            clear()
            continue
        else:
            print("Opsi tidak valid!")
        break

if __name__ == "__main__":
    showMenu()
    time.sleep(1)
