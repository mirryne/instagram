from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# first brower
# pbn1 : faithfullylgbt.com 
# driver = webdriver.Chrome('chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Firefox()
driver.get('https://www.faithfullylgbt.com/wp-admin')

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2025!!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.faithfullylgbt.com/')

e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()
# ============================


# pbn2 : wausanebraska.com
# driver = webdriver.Chrome('chromedriver.exe')
# driver.switch_to.window(driver.window_handles[1])
driver.execute_script("window.open('https://www.wausanebraska.com/wp-admin');")
driver.switch_to.window(driver.window_handles[1])
# driver.get('https://www.wausanebraska.com/wp-admin'""

time.sleep(5)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.wausanebraska.com/')

e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================


# pbn3 : bucheboard.com
# driver = webdriver.Chrome('chromedriver.exe')
driver.execute_script("window.open('http://www.bucheboard.com/wp-admin');")
driver.switch_to.window(driver.window_handles[2])
# driver.get('http://www.bucheboard.com/wp-admin')

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.bucheboard.com/')

e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================

# pbn4 : trabajarporinternet.net
driver.execute_script("window.open('https://trabajarporinternet.net/wp-admin');")
driver.switch_to.window(driver.window_handles[3])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://trabajarporinternet.net/')

e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================

# pbn5 : regiondemurciasi.com
driver.execute_script("window.open('http://www.regiondemurciasi.com/wp-admin');")
driver.switch_to.window(driver.window_handles[4])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.regiondemurciasi.com/')

e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================

# pbn6 : blukoi.com
driver.execute_script("window.open('https://www.blukoi.com/wp-admin');")
driver.switch_to.window(driver.window_handles[5])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.blukoi.com/')

e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================

# pbn7 : brightcalmblue.com
driver.execute_script("window.open('https://brightcalmblue.com/wp-admin');")
driver.switch_to.window(driver.window_handles[6])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://brightcalmblue.com/')

e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================

# pbn8 : seeninside.net
driver.execute_script("window.open('http://www.seeninside.net/wp-admin');")
driver.switch_to.window(driver.window_handles[7])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.seeninside.net/')

e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================

# pbn9 : 2021ouzhoubei.net
driver.execute_script("window.open('http://www.2021ouzhoubei.net/wp-admin');")
driver.switch_to.window(driver.window_handles[8])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.2021ouzhoubei.net/')

e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================

# pbn10 : ouzhoubei2021.net
driver.execute_script("window.open('http://www.ouzhoubei2021.net/wp-admin');")
driver.switch_to.window(driver.window_handles[9])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.ouzhoubei2021.net/')

e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================

# pbn11 : makeadifferenceworldwide.org
driver.execute_script("window.open('http://www.makeadifferenceworldwide.org/wp-admin');")
driver.switch_to.window(driver.window_handles[10])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.makeadifferenceworldwide.org/')

e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================

# pbn12 : kamagra-online24.com
driver.execute_script("window.open('http://kamagra-online24.com/wp-admin');")
driver.switch_to.window(driver.window_handles[11])

time.sleep(10)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://kamagra-online24.com/')

e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================

# # pbn13 : 179xizang.com
# driver.execute_script("window.open('http://www.179xizang.com/wp-admin');")
# driver.switch_to.window(driver.window_handles[12])

# time.sleep(5)
# e = driver.find_element(By.NAME, 'log')
# e.send_keys('linkpsclinic')

# time.sleep(1)
# e = driver.find_element(By.NAME, 'pwd')
# e.send_keys('Link2021!')

# e = driver.find_element(By.NAME, 'wp-submit').click()

# # time.sleep(1)
# # e = driver.find_element_by_id('menu-pages').click()

# driver.get('http://www.179xizang.com/')

# e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================

# pbn14 : elitbodrum.com
driver.execute_script("window.open('https://www.elitbodrum.com/wp-admin');")
driver.switch_to.window(driver.window_handles[12])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.elitbodrum.com/')

e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================

# pbn15 : mujer-nueva.com
driver.execute_script("window.open('http://www.mujer-nueva.com/wp-admin');")
driver.switch_to.window(driver.window_handles[13])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://www.mujer-nueva.com/')

e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================

# pbn16 : whcp71.com
driver.execute_script("window.open('http://whcp71.com/wp-admin');")
driver.switch_to.window(driver.window_handles[14])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://whcp71.com/')

e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()

# ============================

# pbn17 : cinematicmod.com
driver.execute_script("window.open('https://cinematicmod.com/wp-admin');")
driver.switch_to.window(driver.window_handles[15])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('2021Link!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://cinematicmod.com/')

e = driver.find_element(By.LINK_TEXT,'Edit with Elementor').click()


# ============================
driver.switch_to_window(driver.window_handles[0])
# ============================



print()