from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# pbn : annapaterson.com
# driver = webdriver.Chrome('chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.annapaterson.com/wp-admin')


time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2025$$')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.annapaterson.com/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()
e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================

# pbn : kankedort.net
driver.execute_script("window.open('https://www.kankedort.net/wp-admin');")
driver.switch_to.window(driver.window_handles[1])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2025$$')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.kankedort.net/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()
e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()


# ============================

# pbn : focuseek.com
driver.execute_script("window.open('https://www.focuseek.com/wp-admin');")
driver.switch_to.window(driver.window_handles[2])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2025$$')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.focuseek.com/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()
e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================

driver.switch_to_window(driver.window_handles[0])
# ============================

print()
