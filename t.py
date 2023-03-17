from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://instagram.com')

time.sleep(3)
e = driver.find_element(By.NAME, 'username')
e.send_keys('test.test8850')
e = driver.find_element(By.NAME, 'password')
e.send_keys('link2020')
e.send_keys(Keys.ENTER)
time.sleep(5)

print()

