from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.musicaesmeraldas.org/wp-admin')

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2022!!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.musicaesmeraldas.org/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn2 : artikelstrategi.com 
driver.execute_script("window.open('http://artikelstrategi.com/wp-admin');")
driver.switch_to.window(driver.window_handles[1])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2022!!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://artikelstrategi.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()


# ============================


# pbn3 : ashikaga5s.info
driver.execute_script("window.open('http://ashikaga5s.info/wp-admin');")
driver.switch_to.window(driver.window_handles[2])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2022!!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://ashikaga5s.info/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn4 : chokonikki.com
driver.execute_script("window.open('https://chokonikki.com/wp-admin');")
driver.switch_to.window(driver.window_handles[3])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('LINK2022!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://chokonikki.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn5 : sanmiru.com
driver.execute_script("window.open('https://sanmiru.com/wp-admin');")
driver.switch_to.window(driver.window_handles[4])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('LINK2022!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://sanmiru.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn6 : meyerscustomsupply.com
driver.execute_script("window.open('https://www.meyerscustomsupply.com/wp-admin');")
driver.switch_to.window(driver.window_handles[5])

time.sleep(5)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2022!!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.meyerscustomsupply.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn7 : text-speech.com
driver.execute_script("window.open('https://text-speech.com/wp-admin');")
driver.switch_to.window(driver.window_handles[6])

time.sleep(5)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2022!!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://text-speech.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# # pbn8 : girls-liner.com
# driver.execute_script("window.open('https://girls-liner.com/wp-admin');")
# driver.switch_to.window(driver.window_handles[7])

# time.sleep(3)
# e = driver.find_element(By.NAME, 'log')
# e.send_keys('linkpsclinic')

# time.sleep(1)
# e = driver.find_element(By.NAME, 'pwd')
# e.send_keys('Link2022!!!')

# e = driver.find_element(By.NAME, 'wp-submit').click()

# # time.sleep(1)
# # e = driver.find_element_by_id('menu-pages').click()

# driver.get('https://girls-liner.com/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()

# # ============================

# # pbn9 : vslexecutivesummary.com
# driver.execute_script("window.open('https://vslexecutivesummary.com/wp-admin');")
# driver.switch_to.window(driver.window_handles[8])

# time.sleep(3)
# e = driver.find_element(By.NAME, 'log')
# e.send_keys('linkpsclinic')

# time.sleep(1)
# e = driver.find_element(By.NAME, 'pwd')
# e.send_keys('Link2022!!!')

# e = driver.find_element(By.NAME, 'wp-submit').click()

# # time.sleep(1)
# # e = driver.find_element_by_id('menu-pages').click()

# driver.get('https://vslexecutivesummary.com/')

# e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn10 : satomoni.com
driver.execute_script("window.open('http://satomoni.com/wp-admin');")
driver.switch_to.window(driver.window_handles[7])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic@gmail.com')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2022!!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://satomoni.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn11 : guncelbahis.net
driver.execute_script("window.open('https://guncelbahis.net/wp-admin');")
driver.switch_to.window(driver.window_handles[8])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('LINK2023!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://guncelbahis.net/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn12 : escortistanbull.com
driver.execute_script("window.open('https://escortistanbull.com/wp-admin');")
driver.switch_to.window(driver.window_handles[9])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2023!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://escortistanbull.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn13 : storybookmedia.net
driver.execute_script("window.open('http://storybookmedia.net/wp-admin');")
driver.switch_to.window(driver.window_handles[10])

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

# pbn14 : mizunos.us
driver.execute_script("window.open('http://www.mizunos.us/wp-admin');")
driver.switch_to.window(driver.window_handles[11])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkps2807')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.mizunos.us/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================


# pbn15 : shottowerpod.com
driver.execute_script("window.open('http://shottowerpod.com/wp-admin');")
driver.switch_to.window(driver.window_handles[12])

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
driver.switch_to.window(driver.window_handles[13])

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

# pbn17 : bsa-alameda.org
driver.execute_script("window.open('http://www.bsa-alameda.org/wp-admin');")
driver.switch_to.window(driver.window_handles[14])

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
driver.switch_to_window(driver.window_handles[0])
# ============================

