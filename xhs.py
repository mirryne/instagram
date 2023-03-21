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

    chrome_options = Options()
    chrome_options.add_argument('incognito')
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(400,664)
 

    time.sleep(5)

    videos= [
         'http://xhslink.com/Li2Gho',
         'http://xhslink.com/9caHho',
         'http://xhslink.com/XkbHho',
         ]


    for i in range(1000000) :
        # 블로그나 비디오 리스트 개수를 적는다. 0~비디오개수(-1)
        random_video = random.randint(0,2)
        driver.get(videos[random_video])
        # print("Running the Video for {} time".format(i))
        time.sleep(5)
        # sleep_time = random.randint(10,20)
        # time.sleep(sleep_time)
        driver.delete_all_cookies()
    

    # 무한반복은 While True : 로 감싸면 된다. 여기까지 끝
   
