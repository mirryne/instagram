from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random




#Weibo traffic

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome('chromedriver.exe')

videos = [
    'https://www.youtube.com/watch?v=VaWXU_2-LHU',
    'https://www.youtube.com/watch?v=DFwx3JePND8',
    'https://www.youtube.com/watch?v=9JcQ6aJK26M',
    'https://www.youtube.com/watch?v=S4kq9AIgjRg',
    'https://www.youtube.com/watch?v=WycZYaCVN3Y'
]
# 조회수(2023/3/2기준) = 443, 279, 183, 128, 107


# random_video = random.random(0,4)

for i in range(5) :
    print("Running the Video for {} time".format(i))
    random_video = random.randint(0,4)
    driver.get(videos[random_video])
    sleep_time = random.randint(10,20)
    time.sleep(sleep_time)

driver.quit()



