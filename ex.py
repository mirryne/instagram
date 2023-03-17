from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# first brower
# pbn1 : faithfullylgbt.com 
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.faithfullylgbt.com/wp-admin')

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2025!!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.faithfullylgbt.com/')


e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

print()