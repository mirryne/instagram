from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time




driver = webdriver.Chrome('chromedriver.exe')
Options.add_argument("--start-maximized")
driver.get('http://www.brasserieartisanalearlesienne.com/wp-admin')

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2025!!!')

e = driver.find_element(By.NAME, 'wp-submit').click()


# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.brasserieartisanalearlesienne.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

options.add_experimental_option("detach", True)