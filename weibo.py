from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from expressvpn import wrapper
from expressvpn.wrapper import random_connect
import logging
import time
import random

class BannedException(Exception):
    pass



def main():
    while True:
        try:
            scrape()
        except BannedException as be:
            logging.info('BANNED EXCEPTION in __MAIN__')
            logging.info(be)
            logging.info('Lets change our PUBLIC IP GUYS!')
            change_ip()
        except Exception as e:
            logging.error('Exception raised.')
            logging.error(e)


def change_ip():
    max_attempts = 10
    attempts = 0
    while True:
        attempts += 1
        try:
            logging.info('GETTING NEW IP')
            wrapper.random_connect()
            logging.info('SUCCESS')
            return
        except Exception as e:
            if attempts > max_attempts:
                logging.error('Max attempts reached for VPN. Check its configuration.')
                logging.error('Browse https://github.com/philipperemy/expressvpn-python.')
                logging.error('Program will exit.')
                exit(1)
            logging.error(e)
            logging.error('Skipping exception.')


#Weibo traffic

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")

# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome('chromedriver.exe')

video = [
    'https://weibo.com/7757466328/MtTfPvrWp',
    'https://weibo.com/7757466328/MvdfeohpP',
    'https://weibo.com/7757466328/MvcQT224k',
    'https://weibo.com/7757466328/Mvcsx8yfl',
    'https://weibo.com/7757466328/MuUoenuHr',
    'https://weibo.com/7757466328/MuTZT6K5j',
    'https://weibo.com/7757466328/MuTBwrJ8M',
    'https://weibo.com/7757466328/MurUzs9zx'
]
# 조회수(2023/3/2기준) = 443, 279, 183, 128, 107


# random_video = random.random(0,4)

for i in range(2) :
    random_connect()
    driver.get('chrome://extensions')
    print("Running the Video for {} time".format(i))
    random_video = random.randint(0,8)
    driver.get(video[random_video])
    sleep_time = random.randint(10,20)
    time.sleep(sleep_time)
    driver.delete_all_cookies()
    

driver.quit()


# https://www.expressvpn.com/support/vpn-setup/app-for-windows/
