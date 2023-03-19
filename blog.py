from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

from selenium.webdriver.chrome.options import Options

option = webdriver.ChromeOptions()
option.add_argument(f'/home/futureplayer/.config/google-chrome/Default')


driver = webdriver.Chrome('chromedriver.exe', chrome_options=option)
driver.get('https://nid.naver.com/nidlogin.login?svctype=262144&url=https%3A%2F%2Fm.naver.com%2Fna%2F')


time.sleep(4)

pyperclip.copy('mirryne')
time.sleep(3)
driver.find_element(By.NAME,'id')
e.send_keys(Keys.CONTROL,'v')
# e.send_keys('mirryne')


time.sleep(3)

pyperclip.copy('seungmin78!')
time.sleep(3)
driver.find_element(By.NAME,'pw')
e.send_keys(Keys.CONTROL,'v')

time.sleep(3)
e.send_keys(Keys.ENTER)
