#!/usr/bin/python3
#-*-coding:utf-8-*-
#!/usr/bin/python3
import os,time,random,string,re,sys,requests,json,uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
try:os.system("pkg install espeak")
except:pass
from platform import system
import sys
import os
import datetime   
from time import sleep


def testPY():
    if(sys.version_info[0] < 3):
        print ('\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n')
        sys.exit()


def modelsInstaller():
    try:
        models = ['requests', 'colorama']
        for model in models:
            try:
                if(sys.version_info[0] < 3):
                    os.system('cd C:\Python27\Scripts & pip install {}'.format(model))
                else:
                    os.system('python -m pip install {}'.format(model))
                print(' ')
                print('[+] {} has been installed successfully, Restart the program.'.format(model))
                sys.exit()
                print(' ')
            except:
                print('[-] Install {} manually.'.format(model))
                print(' ')
    except:
        pass


import base64
import json
import time
import sys
import os
import re
import binascii
import time
import json
import random
import threading
import pprint
import smtplib
import telnetlib
import os.path
import hashlib
import string
import glob
import sqlite3
import urllib
import argparse
import marshal
import datetime   
from platform import system
from datetime import datetime

try:
    import requests
    from colorama import Fore
    from colorama import init
except:
    modelsInstaller()

requests.urllib3.disable_warnings()

def cls():
    if system() == 'Linux':
        os.system('clear')
    else:
        if system() == 'Windows':
            os.system('cls')


cls()
CLEAR_SCREEN = '\033[2J'
RED = '\033[1;37;1m'  # mode 31 = red foreground
RESET = '\033[1;37;1m'  # mode 0  = reset
BLUE = "\033[1;37;1m"
WHITE = "\033[1;37;1m",
YELLOW = "\033[1;37;1m",
CYAN = "\033[1;37;1m"
MAGENTA = "\033[1;37;1m",
GREEN = "\033[1;37;1m"
RESET = "\033[1;37;1m"
BOLD = '\033[1;37;1m'
REVERSE = "\033[1;37;1m"

def logo():
    clear = "\x1b[0m"
    colors = [35, 33, 36]

    x = """   

 \033[1;33m/$$   /$$ /$$           /$$      
\033[1;36m|$$  /$$/|__/          | $$      
\033[1;32m| $$ /$$/  /$$  /$$$$$$$| $$   /$$
\033[1;34m| $$$$$/  | $$ /$$_____/| $$  /$$/
\033[1;37m| $$  $$  | $$| $$      | $$$$$$/ 
\033[1;38m| $$\  $$ | $$| $$      | $$_  $$ 
\033[1;36m| $$ \  $$| $$|  $$$$$$$| $$ \  $$
\033[1;35m|__/  \__/|__/ \_______/|__/  \__/
                                                                                                                                                                                         

"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.07)
def menu3():
    try:
        uid=os.getuid()#auto key garnet by termux uid
        xx = ('libsooney.so')
        try:
            key1=open(https://github.com/Kickwinnerz/Approva/blob/main/Approval.txt)
        except:
            
            key1=open(https://github.com/Kickwinnerz/Approva/blob/main/Approval.txt)
        kk = ('github')
        k1 = ('apvl-xx')
        k2 = ('xd.txt')
        k3 = ('token.txt')
        key1=open(https://github.com/Kickwinnerz/Approva/blob/main/Approval.txt)
        key=(f'KICK-XD-YWR-APRUAL-DO{uid}5X{key1}110E==')#full key
        mysite= requests.get(f'').text#approve site
        if key in mysite:
                print(logo)
                print(f'[+] Congregations! Your Premium User...');time.sleep(2)
                print(logo)
                os.system('espeak -a 300 "well,come to, KICK, tools"')
                print(f"""\x1b[1;97m 

 \033[1;30m/$$   /$$ /$$           /$$      
\033[1;31m| $$  /$$/|__/          | $$      
\033[1;36m| $$ /$$/  /$$  /$$$$$$$| $$   /$$
\033[1;32m| $$$$$/  | $$ /$$_____/| $$  /$$/
\033[1;34m| $$  $$  | $$| $$      | $$$$$$/ 
\033[1;35m| $$\  $$ | $$| $$      | $$_  $$ 
\033[1;38m| $$ \  $$| $$|  $$$$$$$| $$ \  $$
\033[1;37m|__/  \__/|__/ \_______/|__/  \__/
                                  
                                  
                                  
                                  
                                           
\x1b[1;30m<<======== OWNER KICK======>>
\033[1;31m▇==➤ ADMIN       : KICK
\033[1;37m▇==➤ GITHUB      : WINNERZ
\033[1;31m▇==➤ CREATOR   : WINNER
\033[1;37m▇==➤ FACEBOOK : KICK
\x1b[1;30m<<======== OWNER KICK======>>
\033[1;33m[•] 01  START TOOL ADD FB ID\033[1;36m
\033[1;32m[•] 02  START TOOL TOKAN CONVO\033[1;36m
\033[1;30m[•] 00  EXIT TOOL \033[1;36m

<<======== OWNER KICK======>>""")
                os.system('espeak -a 300 "LUND                   ONE                     YA                     TWO                     YA                     ZERO"')
                key = input("[+] Choose : ")                
                if key in [""]:
                    print("(×) Please Select Correct Option")
                    logo()
                elif key in ["1","01"]:
                    os.system("am start https://www.facebook.com/profile.php?id=100000901213884"+key)                
                elif key in ["0","00","E","e"]:
                    exit('\033[1;32m[>] Thank You ')
                else:
                    print('[×] Choose Correct Option');time.sleep(1)
        else:
                print(logo)
                print(f'[•] Your Key Not Registerd...')
                
                print(f'[•] This Tools Only For Paid Users \n[•] Free Users Saty A Way')
                os.system('espeak -a 300 "well,come to, Kick, tools"')
                print(f'[•] Your Key : '+key)
                os.system("am start https://wa.me/+923047082087?text="+key)
                input(f'[] Press Enter For Approve ')    
                whatsapp = "+923047082087"
                url_wa = "https://api.whatsapp.com/send?phone="+whatsapp+"&text="
                tks = ("Hello kick boss , I Need To Buy Your Paid Tools Please Approve My Key :)\n\n Key :- "+key)
                subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
                
                print(f'run :  python RIAZ.py');pass
    except ValueError:
        print('');pass


menu3()        

testPY()
print('''\033[1;33m<<======== OWNER KICK ======>>\n''')
def venom():
    clear = "\x1b[0m"
    colors = [35, 33, 36]

    y = '''
\033[1;33m<<======== OWNER GAMER 😈======>>
\033[1;31m N4ME    \033[1;34m: \033[1;33mGAMER H3R3 |=|_|
\033[1;36m CrEaToR  \033[1;35m: \033[1;34mGAMER                     
\033[1;31m OWN3R   \033[1;36m: \033[1;35mKICK
\033[1;36m Contact \033[1;33m: \033[1;36m+030426929631
\033[1;33m<<======== OWNER KICK ======>>

'''
    for N, line in enumerate(y.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
    	
venom()


headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}


def message_on_messenger(message):
    for i in ns:
        try:
            message = str(mn) + i
            url = "https://graph.facebook.com/v15.0/{0}/".format('t_' + str(thread_id))
            parameters = {'access_token': access_token, 'message': message}
            s = requests.post(url, data=parameters, headers=headers)
            tt = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
            

            if s.ok:
                e =datetime.now()
                print('''\033[1;33m<<======== OWNER KICK======>>\n''')
                print("\033[1;32;40m", end = "")
                print("--> Convo Or Inbox I'd Link  :--", thread_id)
                print (e.strftime("--> KICK H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
                print("--> Message Successfully Sent By KICK ON FIRE :D ::-->> ", message, "\n")
                print('''\033[1;33m<<========OWNER KICK======>>\n''')
                time.sleep(timm)
            else:
                print('\033[1;32m[x] Message Block ' + tt, '\n[×] Token Error\n')
                time.sleep(30)
        except Exception as e:
            print("\033[1;31;40m", end = "")
            print(e , '\n')           
            time.sleep(30)

def get_messages():
    try:
        url = "https://www.facebook.com"
    except HTTPError as e:
        print("HTTP Error")
    except URLError as e:
        print("URL Error")


if int:    
    i = datetime.now()
    print(i.strftime("\033[1;32m[•] Start Time ==> %Y-%m-%d %I:%M:%S %p "))
    print('''\033[1;32m[•] _ Tool Creator == > [ KICK ON FIRE  ]\n''')
    print("\033[1;36;40m", end = "")
    print(f"""\x1b[1;97m 

 \033[1;36m/$$   /$$ /$$           /$$      
\033[1;36m| $$  /$$/|__/          | $$      
\033[1;36m| $$ /$$/  /$$  /$$$$$$$| $$   /$$
|\033[1;36m $$$$$/  | $$ /$$_____/| $$  /$$/
\033[1;36m| $$  $$  | $$| $$      | $$$$$$/ 
\033[1;36m| $$\  $$ | $$| $$      | $$_  $$ 
\033[1;36m| $$ \  $$| $$|  $$$$$$$| $$ \  $$
\033[1;36m|__/  \__/|__/ \_______/|__/  \__/
                                  
                                  
                                  
                                            
                                                            
                                           
\x1b[1;34m<<========OWNER KICK WINNER😈======>>
\033[1;31m▇==➤ ADMIN        : KiCk x Winner 
\033[1;37m▇==➤ GITHUB       : Winnerz
\033[1;31m▇==➤ OWNER        : Winner
\033[1;37m▇==➤ FACEBOOK     : Game Winner
\033[1;32m▇==➤ BROTHER      : Kick x Winner
\x1b[1;34m<<======== ONWER KICK😈 WINN3R ======>>""")
    os.system('espeak -a 300 "TOKAN FILE NAME DALO"')
    token = input("[+] Input Token File Name :: ")
    print('\n') 
    with open(token, 'r') as f2:
        access_token = f2.read()
        payload = {'access_token': access_token}
        a = "https://bb/v15.0/me"
        b = requests.get(a, params=payload)
        d = json.loads(b.text)
        if 'name' not in d:
            print(BOLD + RED + '\n[x] Token Invalid..!!')
            sys.exit()
        mb = d['name']
        print('\033[1;32mYour Profile Name :: \033[1;32;1m%s' % (mb))
        print('\n')
        os.systevbnnm('espeak -a 300 "CONVO ID DALO JAHA GALI DENI HA"')
        thread_id = input(BOLD + CYAN + "\033[1;36m[+] Conservation ID :: \033[1;32;1m")
        os.system('espeak -a 300 "TATE KA NAME DALO"')
        mn= inpuhkott(BOLD + CYAN + "\033[1;36m[+] Enter Kidx Name :: \033[1;32;1m")
        os.system('espeak -a 300 "ALI FILE DALO"')
        ms = input(BOLD + CYAN + "\033[1;36m[+] Add Gali File Name :: \033[1;32;1m")
        os.system('espeak -a 300 "FILE KITNI BAAR REPIT KARANI HA"')
        repeat = int(input(BOLD + CYAN + "\033[1;36m[+] File Repeat No :: \033[1;32;1m"))
        os.system('espeak -a 300 "SPEED DALO YAR"')
        timm = int(input(BOLD + CYAN + "\033[1;36m[+] Speed in Seconds :: \033[1;32;1m"))
        print('\n')
        print('''\033[1;34m________All Done....Loading Profile Info.....!''')
        print('\033[1;34mYour Profile Name :: ', mb)
        print('\n')
        ns = open(ms, 'r').readlines()

        for i in range(repeat):
            messenger = get_messages()
            message_on_messenger(thread_id)
else:
	print(BOLD+RED+'[-] <==> Your Number Is Wrong Please Take Approval From Owner')
