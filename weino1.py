#웨이보 views수 증가를 위한 파이썬 코드

# 쉘에 $nordvpn login, $nordvpn connect로 코드실행전에 먼저 연결해야 에러가 없다.

# vpn 랜덤 설정

import platform
import random
import os
import time

linux_countries= ['AL','AR','AU','AT','BE','BA','BR','BG','CA','CL',
                  'CO','CR','HR','CY','CZ','DK','EE','FI','FR','GE',
                  'DE','GR','HK','HU','IS','ID','IE','IL','IT','JP',
                  'LV','LT','LU','MY','MX','MD','NL','NZ','MK','NO',
                  'PL','PT','RO','RS','SG','SK','SI','ZA','KR','ES',
                  'SE','CH','TW','TH','TR','UA','AE','GB','US','VN']


def nordvpn() :
    version = platform.system()
    if version == "Linux" or version == "Ubuntu" :
        command = "nordvpn connect "+random.choice(linux_countries)+" > /dev/null 2>&1"
        
    else :
        command = "nordvpn connect"+random.choice(linux_countries)+" > /dev/null 2>&1"
    os.system(command)
    time.sleep(5)


while True :
    import requests
   
    # ip = requests.get("https://api.ipify.org").text
    # print(f"IP체인지\nIP:\t{ip}")
    nordvpn()

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
 

    driver = webdriver.Chrome('chromedriver.exe')
    driver.set_window_size(400,664)
    driver.get('https://m.weibo.cn/u/7757466328?uid=7757466328&t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%9E%97%E5%85%8B%E6%95%B4%E5%BD%A2%E5%A4%96%E7%A7%91')  
    time.sleep(3)

    # 이제부터 마우스를 움직여 클릭할 수 밖에 없다. weibo에는 class나 ID로 특정할 수 없는 elements가 많다. 따라서 pyautogui를 사용한다.
    import pyautogui

    # print(pyautogui.position()) 로 커서의 위치값을 알 수 있다.
    pyautogui.moveTo(x=335,y=611)
    pyautogui.click()

    time.sleep(4)
    

    # 무한반복은 While True : 로 감싸면 된다. 여기까지 끝
