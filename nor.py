import platform
import random
import os
import time

linux_countries= ['al','ar','jp']


def nordvpn() :
    version = platform.system()
    if version == "Linux" or version == "Ubuntu" :
        command = "nordvpn connect "+random.choice(linux_countries)+" > /dev/null 2>&1"
        
    else :
        command = "nordvpn connect"+random.choice(linux_countries)+" > /dev/null 2>&1"
    os.system(command)
    time.sleep(10)


import requests
ip = requests.get("https://api.ipify.org").text
print(f"IP체인지\nIP:\t{ip}")
nordvpn()



import requests
ip = requests.get("https://api.ipify.org").text

print(f"IP체인지\nIP:\t{ip}")

nordvpn()