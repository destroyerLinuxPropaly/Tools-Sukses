#!/usr/bin/python3
import sys
import subprocess
import time

try: # Import Module
    import requests
    import time
    import random
    import os
    import urllib3
    import json
    import bs4
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'urllib3'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'bs4'])
finally:
    import requests # Post, Get, & Put URL API
    import urllib3  # HTTP client untuk Python
    from bs4 import BeautifulSoup as bs

from time import sleep
from datetime import date
from urllib3.exceptions import *
from bs4 import BeautifulSoup as bs
from pip._vendor.requests import post,get

#Tahun tanggal bulan
today = date.today()

# Mengambil input
nama = input(f'Masukkan nama anda: ')

def rod2(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.050)

def rod(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.008)

 #warna inisial hit
hijau   =   "\033[1;92m"
putih   =   "\033[1;97m"
abu     =   "\033[1;90m"
kuning  =   "\033[1;93m"
ungu    =   "\033[1;95m"
merah   =   "\033[1;91m"
biru    =   "\033[1;96m"
ungu2   =   "\33[3;47;43m" #Purple

def ask():
    a = input (f"""Pilih Pertanyaan Mu >
    {ungu} [a] {hijau} Cara menghapus dosa ringan
    {ungu} [b] {hijau} Cara menghapus dosa besar
    {ungu} [c] {hijau} Cara meneladani Allah Maha Esa
    {ungu} [d] {hijau} Bagi bagi tools gratis
    {ungu} [e] {hijau} Exit
    {ungu} [z] {hijau} Clear

{kuning}Input:{merah}~# {putih}""")
    if a == "a" or a == "A":
       check_input = 1
       jawab5()
    elif a == "b" or a == "B":
       check_input = 1
       jawab3()
    elif a == "c" or a == "C":
       check_input = 1
       jawaban()
    elif a == "e" or a == "E":
       check_input = 1
       rod2(f"""{biru} Terima Kasih sudah mencoba tools saya {kuning} Selamat tinggal""")
       sys.exit()
    elif a == "z" or a == "Z":
       check_input = 1
       os.system("clear")
       ask()
    elif a == "d" or a == "D":
       check_input = 1
       rod2(f"""{biru}
[=] {putih} https://github.com/destroyerLinuxPropaly/Btg-SpamV2.git {hijau} Spam OTP
{biru}[=] {putih} https://github.com/fahadsyihab06/Track-ip {ungu} VVIP From TC20 {hijau} Osint
{biru}[=] {putih} https://github.com/Hisoka-Morrou/hisoka-baileys.git {hijau} Bot WA
{biru}[=] {putih} https://github.com/isuruwa/Phoenix.git {hijau} TOOLS PHISING
{biru}[=] {putih} https://github.com/Ignitetch/AdvPhishing.git {hijau} TOOLS PHISING 2
{biru}[=] {putih} https://github.com/thewhiteh4t/seeker.git {ungu} VVIP TOOLS! {hijau} Track location
{biru}[=] {putih} https://github.com/TZdev7/spam-wa.git {hijau} spam wa otp
{biru}[=] {putih} https://github.com/Bhai4You/Bull-Attack.git {hijau} Track ip
{biru}[=] {putih} https://github.com/KasRoudra2/maxfiles.git {biru} Rare {hijau} MaxPhisher
{biru}[=] {putih} https://github.com/Cabbagec/termux-ohmyzsh.git {biru} Rare {hijau} Theme Termux
{biru}[=] {putih} https://github.com/HyukIsBack/KARMA-DDoS.git {ungu} VVIP TOOLS {hijau} DDoS """)

       ulang()
    else:
       rod2(f"""{merah}Ketik dengan benar""")
       ask()

def ulang():
     a = input (f"""{kuning} Apakah anda ingin kembali?
{kuning}Input:{merah}~# {putih}""")
     if a == "y" or a == "Y":
         check_input = 1
         ask()
     elif a == "n" or a == "N":
         check_input = 1
         sys.exit()
     else:
       print(f"""{merah} Ketik dengan benar cog""")
       ulang()

def jawaban():
    rod2(f"""{hijau} Cara meneladani Allah Maha esa adalah.....""")
    rod2(f"""{putih}
{merah}[>] {putih} Senantiasa Berbuat Baik Terhadap Sesama. Allah SWT memiliki sifat pengasih
                   dan penyayang kepada semua makhluk-Nya.
{merah}[>] {putih} Teguh Pendirian dalam Beribadah.
{merah}[>] {putih} Selalu Tunduk, Patuh dan Bersyukur.
{merah}[>] {putih} Memiliki Sifat Sabar dan Ikhlas.
{merah}[>] {putih} Bersungguh Sungguh dalam Menuntut Ilmu.
""")
    rod2(f"""{kuning} kembali dalam 5 detik""")
    time.sleep(5.0)
    ask()
def jawab3():
    rod2(f""" {hijau}
      • Cara Menghapus dosa {merah}Besar {hijau}adalah........
{putih}dihapuskan dengan taubat atau dengan rahmat
 dari Allah Ta'ala dan keutamaan dari Allah”
 (Syarah Shahih Muslim lin Nawawi).
""")
    time.sleep(1.0)
    ask()
def jawab5():
    rod2(f"""{hijau}
      • Berdzikir dan membaca istigfar
      • Berwudhu
      • Bersholawat atas nabi
      • Mengucapkan 'Aamiin' saat sholat
      • Memperbanyak sujud
      • Sholat jumat
  {kuning}> Jika masih belum paham silahkan copy webdibawah ini
{ungu}-----> {putih}https://www.google.com/amp/s/www.detik.com/edu/detikpedia/d-5808569/7-amalan-ringan-penghapus-dosa-sudah-tunaikan-yang-mana/amp
""")
    time.sleep(1.0)
    ask()
def jawab():
    rod2("• Jangan Pernah Berhenti. “Tidak masalah seberapa lambat kamu berjalan, asalkan kamu tidak berhenti” ")
    rod2("• Tidak Ada Kata Terlambat. “Belum terlambat untuk menjadi apa yang kau inginkan” ")
    rod2(f"""• “Ubah hidupmu hari ini. Jangan bertaruh pada masa depan, bertindaklah sekarang tanpa menunda”
           Saat baru ingin memulai meraih cita-cita atau kesuksesan, pasti kamu pernah berpikir
           tentang harus melakukan apa untuk menuju sukses itu. Benar, bukan? Percaya
           taau tidak,
           sukses itu tidak membutuhkan resep khusus. Kamu harus segera melakukan tindakan dan
           berhenti menunda.

           Apapun yang ingin kamu lakukan, kerjakan itu mulai dari {merah}sekarang.
           Jadikan kata-kata motivasi sukses di atas ini sebagai pacuan.
           Soalnya, kalau kamu terus-menerus menunda, kapan lagi kamu akan memiliki
           waktu untuk bekerja mewujudkan impian yang selama ini kamu inginkan? """)
    tanya2()

def tanya():
        a = input(f"""{merah}[*] {ungu}Hello sir, anda ingin melihat motivasi cara sukses? {putih}y/n {ungu}atau {putih}s/S {ungu}(skip)
{kuning}Input:{merah}~# {putih}""")
        if a == "y" or a == "Y":
            check_input = 1
            jawab()
        elif a == "s" or a == "S":
            check_input = 1
            rod2(f"""{kuning} Mengskip Kalimat Awal !
{merah}[+] {hijau} Tunggu 5 Detik untuk halaman selanjutnya""")
            os.system("clear")
            print(f"{biru} Waktu 5")
            time.sleep(1.0)
            os.system("clear")
            print(f"{biru} Waktu 4")
            time.sleep(1.0)
            os.system("clear")
            print(f"{biru} Waktu 3")
            time.sleep(1.0)
            os.system("clear")
            print(f"{biru} Waktu 2")
            time.sleep(1.0)
            os.system("clear")
            print(f"{biru} Waktu 1")
            time.sleep(1.0)
            os.system("clear")
            tanya2()
        elif a == "n" or a == "N":
            check_input = 1
            rod2(f"{hijau}Good Bye 👋")
            sys.exit()
        else:
            print (f"""Ketik huruf dengan benar {merah}Kawanku!""")
            tanya()

def tanya2():
        a = input(f"""{merah}[*] {ungu}Apakah anda, ingin bertanya? {merah} y/n ?
{kuning}Input:{merah}~# {putih}""")
        if a == "y" or a == "Y":
            check_input = 1
            ask()
        elif a == "n" or a == "N":
            check_input = 1
            rod2(f"{hijau}Selamat Tinggal 👋")
            sys.exit()
        else:
            print (f"""Ketik huruf dengan benar {merah}Kawanku!""")
            tanya2()
try:
        os.system("clear") # Clear Terminal
        print(f'{ungu}</> {biru}Halo',nama,' Selamat Datang Di Tools Sukses Dan Motivasi cara sukses') 
        time.sleep(3.0)
        rod2(f"""{kuning} Update Tools""")
        time.sleep(6.0)
        rod2(f"""{hijau} Succesfully!""")
        rod(f"""{merah}
           _____       _
          / ____|     | |
         | (___  _   _| | _____  ___  ___
          \___ \| | | | |/ / __|/ _ \/ __l
          {putih}____) | |_| |   <\__ \  __/\__ \\
         |_____/ \__,_|_|\_\___/\___||___/
     {kuning} B Y >{merah}  D E S T R O Y E R 4 6
                                 {ungu} And Free Tools!
""")
        rod(f"""
           {biru}< Inform >
{biru}╔═════════════════════════════╗
{biru}║ {hijau}Upload : {kuning}13 maret{biru}           ║  {merah} No Recode anj!
{biru}║ {hijau}Date   : {kuning}{today}{biru}         ║
{biru}║ {hijau}Version: {kuning}1.2.1 {biru}             ║
{biru}╚═════════════════════════════╝ """)
        
        tanya()
except KeyboardInterrupt:
    rod2(f"""{merah}Keluar {ungu}➣
{putih} ⸻⸻⸻⸻ ⻄⻠{kuning}Terima Kasih {putih}⺴⻄ ⸻⸻⸻⸻""")
    sys.exit()
