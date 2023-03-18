#웨이보 views수 증가를 위한 파이썬 코드

# 쉘에 $nordvpn login, $nordvpn connect로 코드실행전에 먼저 연결해야 에러가 없다.

# vpn 랜덤 설정
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


while True :
    import requests
    ip = requests.get("https://api.ipify.org").text
    print(f"IP체인지\nIP:\t{ip}")
    nordvpn()
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    import time
    import random

    # Weibo traffic

    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--incognito")

    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome('chromedriver.exe')

    time.sleep(5)

    videos= [
        'https://weibo.com/7757466328/MtTfPvrWp'
        # 'https://weibo.com/7757466328/MvdfeohpP',
        # 'https://weibo.com/7757466328/MvcQT224k',
        # 'https://weibo.com/7757466328/Mvcsx8yfl',
        # 'https://weibo.com/7757466328/MuUoenuHr',
        # 'https://weibo.com/7757466328/MuTZT6K5j',
        # 'https://weibo.com/7757466328/MuTBwrJ8M',
        # 'https://weibo.com/7757466328/MurUzs9zx'
    ]


    for i in range(2) :
        # 블로그나 비디오 리스트 개수를 적는다. 0~비디오개수(-1)
        random_video = random.randint(0,0)
        driver.get(videos[random_video])
        print("Running the Video for {} time".format(i))
        sleep_time = random.randint(10,30)
        time.sleep(sleep_time)
        driver.delete_all_cookies()
        # driver.quit() 





# print()




# import requests
# ip = requests.get("https://api.ipify.org").text

# print(f"IP체인지\nIP:\t{ip}")

# nordvpn()