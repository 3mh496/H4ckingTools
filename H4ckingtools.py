print('Hallo my friend Welcome To My Channel NetHunter')

import requests, os

def cekip():
 print(f'[!]╭────────=> Mendapatkan IP..')
 re = requests.get('https://api.myip.com').json()
 ip = re['ip']
 print(f'[!] IP kamu : {ip}')
 
def itrackingloc():
 print(f'[!] Menginstall tools Strom-Breaker..')
 os.system('apt update')
 os.system('git clone https://github.com/ultrasecurity/Storm-Breaker')
 os.system('cd Storm-Breaker')
 os.system('sudo bash linux-installer.sh')
 os.system('python3 -m pip install -r requirments.txt')
 os.system('sudo python3 Storm-Breaker.py')
 
def iprank():
 print(f'[!] Menginstall tools prank..')
 os.system('apt update')
 os.system('pkg update')
 os.system('git clone https://github.com/3mh496/Install-Tools-HackingOS-3mh4Sec')
 os.system('apt install bash')
 os.system('pkg install bash')

def iphiscam():
 print(f'[!] Menginstall tools phiscam..')
 os.system('apt update')
 os.system('git clone https://github.com/hangetzzu/saycheese')

def irasomware():
 print(f'[!] Menginstall tools rasomware..')
 os.system('apt update')
 os.system('git clone https://github.com/termuxhackers-id/SARA')
 
print('''-=[ MyTools ]=-

     [Menu]
[1] Cek IP
[2] Install tracking location
[3] Install prank
[4] Install phiscam
[5] Install virus rasomware android
[x] Keluar
''')
menu = input('[?] Silahkan pilih menu : ')

if menu == '1':
 cekip()
elif menu == '2':
 itrackingloc()
elif menu == '3':
 iprank()
elif menu == '4':
 iphiscam()
elif menu == '5':
 irasomware()
if menu =='x':
 print('[?] Keluar..')
 print('[?] oke sampai jumpa di updatan selanjutnya..')
 
