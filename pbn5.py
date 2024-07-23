from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time




# driver = webdriver.Chrome('chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://avenuewestdev.com/wp-admin')

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!$!')

e = driver.find_element(By.NAME, 'wp-submit').click()


# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://avenuewestdev.com/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()
e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()


# ============================

# pbn : tampervue.com
driver.execute_script("window.open('https://tampervue.com/wp-admin');")
driver.switch_to.window(driver.window_handles[1])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2023$$')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://tampervue.com/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()
e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()



# ============================


# pbn : amatnieki.com
driver.execute_script("window.open('https://amatnieki.com/wp-admin');")
driver.switch_to.window(driver.window_handles[2])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2023$$')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://amatnieki.com/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()
e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()


# ============================

# pbn : nidaelektronik.com
driver.execute_script("window.open('https://nidaelektronik.com/wp-admin');")
driver.switch_to.window(driver.window_handles[3])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2023$$')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://nidaelektronik.com/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()
e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()


# ============================

# pbn : longislandbaroqueensemble.com
driver.execute_script("window.open('https://longislandbaroqueensemble.com/wp-admin');")
driver.switch_to.window(driver.window_handles[4])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2023$$')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://longislandbaroqueensemble.com/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()
e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()


# ============================
# pbn : droneflynewengland.com
driver.execute_script("window.open('https://www.droneflynewengland.com/wp-admin');")
driver.switch_to.window(driver.window_handles[5])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2025$$')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.droneflynewengland.com/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()
e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================
# pbn : allhotlesbians.com
driver.execute_script("window.open('https://www.allhotlesbians.com/wp-admin');")
driver.switch_to.window(driver.window_handles[6])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2023$$')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.allhotlesbians.com/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()
e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================
# ============================
# pbn : bursaeskortbayan.net
driver.execute_script("window.open('https://www.bursaeskortbayan.net/wp-admin');")
driver.switch_to.window(driver.window_handles[7])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2025$$')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.bursaeskortbayan.net/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()
e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================
# ============================
# pbn : alanyailanlar.com
driver.execute_script("window.open('https://www.alanyailanlar.com/wp-admin');")
driver.switch_to.window(driver.window_handles[8])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2025$$')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.alanyailanlar.com/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()
e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================
# ============================
# pbn : zenannuaire.com
driver.execute_script("window.open('http://www.zenannuaire.com/wp-admin');")
driver.switch_to.window(driver.window_handles[9])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2025$$')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.zenannuaire.com/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()
e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================

# pbn : hushcolours.com
driver.execute_script("window.open('https://www.hushcolours.com/wp-admin');")
driver.switch_to.window(driver.window_handles[10])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2025$$')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.hushcolours.com/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()
e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================

# ============================

# pbn : fishforsale.org
driver.execute_script("window.open('https://www.fishforsale.org/wp-admin');")
driver.switch_to.window(driver.window_handles[11])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2025$$')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.fishforsale.org/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()
e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================



# pbn : sachekimi.com
driver.execute_script("window.open('https://www.sachekimi.com/wp-admin');")
driver.switch_to.window(driver.window_handles[12])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2025$$')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.sachekimi.com/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()
e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================


# pbn : brightluxbiz.com
driver.execute_script("window.open('https://www.brightluxbiz.com/wp-admin');")
driver.switch_to.window(driver.window_handles[13])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2025$$')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.brightluxbiz.com/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()
e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================





# ============================

driver.switch_to_window(driver.window_handles[0])
# ============================

print()