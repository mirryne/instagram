from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
import time
import random

driver = webdriver.Chrome('chromedriver.exe')
driver.set_window_size(400,664)
driver.get('https://m.weibo.cn/u/7757466328?uid=7757466328&t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%9E%97%E5%85%8B%E6%95%B4%E5%BD%A2%E5%A4%96%E7%A7%91')  
time.sleep(3)

import pyautogui

print(pyautogui.position())
pyautogui.moveTo(x=335,y=611)
pyautogui.click()

time.sleep(4)
# e = driver.find_element(By.LINK_TEXT,'全文').click();
# # e = driver.find_elements_by_css_selector("a[href*"='/status/4871239137495577]')
# # e.click()
# time.sleep(5)


