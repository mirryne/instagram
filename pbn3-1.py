from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# pbn17 : bsa-alameda.org
# driver = webdriver.Chrome('chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://www.bsa-alameda.org/wp-admin')



# # pbn17 : bsa-alameda.org
# driver.execute_script("window.open('http://www.bsa-alameda.org/wp-admin');")
# driver.switch_to.window(driver.window_handles[8])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2025!!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.bsa-alameda.org/')

e = driver.find_element_by_link_text('Edit with Elementor').click()


# ============================

# pbn13 : storybookmedia.net
driver.execute_script("window.open('http://storybookmedia.net/wp-admin');")
driver.switch_to.window(driver.window_handles[1])

time.sleep(5)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('LINK2023!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://storybookmedia.net/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# # pbn14 : mizunos.us
# driver.execute_script("window.open('http://www.mizunos.us/wp-admin');")
# driver.switch_to.window(driver.window_handles[10])

# time.sleep(3)
# e = driver.find_element(By.NAME, 'log')
# e.send_keys('linkps2807')

# time.sleep(1)
# e = driver.find_element(By.NAME, 'pwd')
# e.send_keys('Link2021!!')

# e = driver.find_element(By.NAME, 'wp-submit').click()

# # time.sleep(1)
# # e = driver.find_element_by_id('menu-pages').click()

# driver.get('http://www.mizunos.us/')

# e = driver.find_element_by_link_text('편집하기').click()

# ============================


# pbn15 : shottowerpod.com
driver.execute_script("window.open('http://shottowerpod.com/wp-admin');")
driver.switch_to.window(driver.window_handles[2])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2024!!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://shottowerpod.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn16 : sxl-online.com
driver.execute_script("window.open('http://www.sxl-online.com/wp-admin');")
driver.switch_to.window(driver.window_handles[3])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2024!!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.sxl-online.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# # pbn17 : bsa-alameda.org
# driver.execute_script("window.open('http://www.bsa-alameda.org/wp-admin');")
# driver.switch_to.window(driver.window_handles[12])

# time.sleep(3)
# e = driver.find_element(By.NAME, 'log')
# e.send_keys('linkpsclinic')

# time.sleep(1)
# e = driver.find_element(By.NAME, 'pwd')
# e.send_keys('Link2025!!!')

# e = driver.find_element(By.NAME, 'wp-submit').click()

# # time.sleep(1)
# # e = driver.find_element_by_id('menu-pages').click()

# driver.get('http://www.bsa-alameda.org/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================
driver.switch_to_window(driver.window_handles[0])
# ============================

print()