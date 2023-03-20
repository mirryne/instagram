from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

chrome_options = Options()

# chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('incognito')

driver = webdriver.Chrome(options=chrome_options)
    
driver = webdriver.Chrome('chromedriver.exe')
    # driver.set_window_size(400,664)