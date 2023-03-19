from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')

# full screen으로 창(window)를 열고 싶을때 사용함.
driver.maximize_window()

# 창(window)를 원하는 사이즈로 열고 싶을때 사용함
# driver.set_window_size(400,664)

time.sleep(10)

