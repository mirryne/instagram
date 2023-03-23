from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

#baidu dongtai traffic

while True :
 
    chrome_options = Options()
    chrome_options.add_argument('incognito')
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(400,900)

    time.sleep(5)
    driver.get('https://m.baidu.com/sf/vsearch?pd=realtime_ugc&word=%E6%9E%97%E5%85%8B%E6%95%B4%E5%BD%A2%E5%A4%96%E7%A7%91&tn=vsearch&sa=vs_realtime_ugc&lid=9877731058785431497&ms=1&atn=list&ruidx=0&ruus=NXA2WDA0ODIzMTQ3Nzc5NjQ1MDk4OTA5XzE2Nzk1NDA1NDU%3D#4823147779645098909')
   
    time.sleep(10)

    import pyautogui
    import random

    # 첫번째 위치
    pos1 = (381, 339)

    # 두번째 위치
    pos2 = (877, 669)

    # 무작위 위치 선택
    pos = random.choice([pos1, pos2])

    # print(pyautogui.position()) 로 커서의 위치값을 알 수 있다.

    pyautogui.moveTo(pos)
    pyautogui.click()

    time.sleep(4)

    driver.delete_all_cookies()
    
