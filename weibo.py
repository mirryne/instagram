from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

#Weibo traffic

while True :
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--incognito")

    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome('chromedriver.exe')

    time.sleep(5)

    videos= [
         'https://weibo.com/7757466328/MtTfPvrWp',
         'https://weibo.com/7757466328/MvdfeohpP',
         'https://weibo.com/7757466328/MvcQT224k',
         'https://weibo.com/7757466328/Mvcsx8yfl',
         'https://weibo.com/7757466328/MuUoenuHr',
         'https://weibo.com/7757466328/MuTZT6K5j',
         'https://weibo.com/7757466328/MuTBwrJ8M',
         'https://weibo.com/7757466328/MurUzs9zx'
         ]


for i in range(50000) :
    # 블로그나 비디오 리스트 개수를 적는다. 0~비디오개수(-1)
    random_video = random.randint(0,2)
    driver.get(videos[random_video])
    print("Running the Video for {} time".format(i))
    sleep_time = random.randint(10,20)
    time.sleep(sleep_time)
    driver.delete_all_cookies()
    
