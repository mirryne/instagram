from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

#Weibo traffic

while True :
 
    chrome_options = Options()
    chrome_options.add_argument('incognito')
    driver = webdriver.Chrome(options=chrome_options)
  
    # driver = webdriver.Chrome('chromedriver.exe')
    driver.set_window_size(400,664)

    time.sleep(5)

    videos= [
         'https://ameblo.jp/linkseikei/entry-12793986350.html',
         'https://ameblo.jp/linkseikei/entry-12793644110.html',
         'https://ameblo.jp/linkseikei/entry-12793060892.html',
         ]


    for i in range(50000) :
        # 블로그나 비디오 리스트 개수를 적는다. 0~비디오개수(-1)
        random_video = random.randint(0,2)
        driver.get(videos[random_video])
        # print("Running the Video for {} time".format(i))
        time.sleep(5)
        # sleep_time = random.randint(10,20)
        # time.sleep(sleep_time)
        driver.delete_all_cookies()
    
