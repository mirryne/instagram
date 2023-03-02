from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time




driver = webdriver.Chrome('chromedriver.exe')
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

# ============================

# pbn2 : adanaescortderin.com
driver.execute_script("window.open('https://www.adanaescortderin.com/wp-admin');")
driver.switch_to.window(driver.window_handles[1])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2025!!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.adanaescortderin.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()


# ============================


# pbn3 : 365d365e.com
driver.execute_script("window.open('https://365d365e.com/wp-admin');")
driver.switch_to.window(driver.window_handles[2])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!$!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://365d365e.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn4 : evdc.info
driver.execute_script("window.open('https://www.evdc.info/wp-admin');")
driver.switch_to.window(driver.window_handles[3])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!$!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.evdc.info/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn5 : fondospantallagratis.com
driver.execute_script("window.open('https://www.fondospantallagratis.com/wp-admin');")
driver.switch_to.window(driver.window_handles[4])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('china2023!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.fondospantallagratis.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn6 : averylevinemusic.com
driver.execute_script("window.open('https://www.averylevinemusic.com/wp-admin');")
driver.switch_to.window(driver.window_handles[5])

time.sleep(5)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('china2023!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.averylevinemusic.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn7 : 99couponcodes.com
driver.execute_script("window.open('https://www.99couponcodes.com/wp-admin');")
driver.switch_to.window(driver.window_handles[6])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('china2023!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.99couponcodes.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn8 : 1bed4u.com
driver.execute_script("window.open('http://www.1bed4u.com/wp-admin');")
driver.switch_to.window(driver.window_handles[7])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('china2023!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.1bed4u.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn9 : atcomdce.org
driver.execute_script("window.open('https://atcomdce.org/wp-admin');")
driver.switch_to.window(driver.window_handles[8])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('china2023!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://atcomdce.org/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn10 : allorgdownload.org
driver.execute_script("window.open('https://allorgdownload.org/wp-admin');")
driver.switch_to.window(driver.window_handles[9])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic@gmail.com')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('china2023!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://allorgdownload.org/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn11 : authentiques-asia.com
driver.execute_script("window.open('http://www.authentiques-asia.com/wp-admin');")
driver.switch_to.window(driver.window_handles[10])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('china2023!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.authentiques-asia.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================



# ============================
driver.switch_to_window(driver.window_handles[0])
# ============================