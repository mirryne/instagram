
while True:
    import pyautogui
    import time
    import random
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
 
    driver = webdriver.Chrome('chromedriver.exe')
    driver.set_window_size(400,664)
    driver.get('https://m.naver.com')  

    direction = random.choice([-1, 1])  # randomly choose scroll direction
    distance = random.randint(50, 200)  # randomly choose scroll distance
    pyautogui.scroll(distance * direction)  # scroll up or down by chosen distance
    time.sleep(random.uniform(0.5, 1.5))  # wait for a random time between 0.5 and 1.5 seconds

    