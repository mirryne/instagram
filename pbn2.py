
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# second brower
# pbn1 : ccphhistoryaction.org
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://www.ccphhistoryaction.org/wp-admin')

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('2021Link!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.ccphhistoryaction.org/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn2 : bonuslubahisler.com
driver.execute_script("window.open('http://www.bonuslubahisler.com/wp-admin');")
driver.switch_to.window(driver.window_handles[1])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('2021Link!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.bonuslubahisler.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()


# ============================

# pbn3 : jhpf.org
driver.execute_script("window.open('http://www.jhpf.org/wp-admin');")
driver.switch_to.window(driver.window_handles[2])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('2021Link!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.jhpf.org/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn4 : a-kontra.net
driver.execute_script("window.open('http://www.a-kontra.net/wp-admin');")
driver.switch_to.window(driver.window_handles[3])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('2021Link!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.a-kontra.net/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn5 : sozaiwing.com
driver.execute_script("window.open('https://sozaiwing.com/wp-admin');")
driver.switch_to.window(driver.window_handles[4])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('2021Link!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://sozaiwing.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn6 : rotacal.org
driver.execute_script("window.open('http://www.rotacal.org/wp-admin');")
driver.switch_to.window(driver.window_handles[5])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('L2021ink!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.rotacal.org/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn7 : savoymag.net
driver.execute_script("window.open('http://www.savoymag.net/wp-admin');")
driver.switch_to.window(driver.window_handles[6])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('L2021ink!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.savoymag.net/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn8 : innohubkku.com
driver.execute_script("window.open('https://innohubkku.com/wp-admin');")
driver.switch_to.window(driver.window_handles[7])

time.sleep(5)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('L2021ink!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://innohubkku.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn9 : ausbell.com
driver.execute_script("window.open('http://www.ausbell.com/wp-admin');")
driver.switch_to.window(driver.window_handles[8])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2022!!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.ausbell.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn10 : irishtheatrebrussels.com
driver.execute_script("window.open('http://irishtheatrebrussels.com/wp-admin');")
driver.switch_to.window(driver.window_handles[9])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('L2021ink!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://irishtheatrebrussels.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn11 : artistsalleydelray.com
driver.execute_script("window.open('http://artistsalleydelray.com/wp-admin');")
driver.switch_to.window(driver.window_handles[10])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('L2021ink!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://artistsalleydelray.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn12 : iitgaa.org
driver.execute_script("window.open('http://iitgaa.org/wp-admin');")
driver.switch_to.window(driver.window_handles[11])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('L2021ink!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://iitgaa.org/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn13 : ajansuntv.com
driver.execute_script("window.open('https://www.ajansuntv.com/wp-admin');")
driver.switch_to.window(driver.window_handles[12])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('L2021ink!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.ajansuntv.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn14 : motekar.org
driver.execute_script("window.open('http://motekar.org/wp-admin');")
driver.switch_to.window(driver.window_handles[13])

time.sleep(5)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('L2021ink!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://motekar.org/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================


# pbn15 : lgu360.com
driver.execute_script("window.open('http://www.lgu360.com/wp-admin');")
driver.switch_to.window(driver.window_handles[14])

time.sleep(5)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('L2021ink!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.lgu360.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn16 : chinacrystalmatch.com
driver.execute_script("window.open('https://chinacrystalmatch.com/wp-admin');")
driver.switch_to.window(driver.window_handles[15])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('L2021ink!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://chinacrystalmatch.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn17 : dgube.net
driver.execute_script("window.open('http://www.dgube.net/wp-admin');")
driver.switch_to.window(driver.window_handles[16])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('L2021ink!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.dgube.net/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

driver.switch_to_window(driver.window_handles[0])
# ============================
