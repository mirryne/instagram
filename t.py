from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

#Weibo traffic

driver = webdriver.Chrome('chromedriver.exe')
time.sleep(5)
driver.get('https://weibo.com/')
#로딩완료할때까지 기다리기   
time.sleep(20)
e = driver.find_element(By.LINK_TEXT,'首页').click()
# e.send_keys('林克整形外科')