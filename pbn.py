from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# first brower
# pbn1 : faithfullylgbt.com 
driver = webdriver.Chrome('chromedriver.exe')
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

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================


# pbn2 : wausanebraska.com
# driver = webdriver.Chrome('chromedriver.exe')
# driver.switch_to.window(driver.window_handles[1])
driver.execute_script("window.open('https://www.wausanebraska.com/wp-admin');")
driver.switch_to.window(driver.window_handles[1])
# driver.get('https://www.wausanebraska.com/wp-admin'""

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://www.wausanebraska.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

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

e = driver.find_element_by_link_text('Edit with Elementor').click()

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

e = driver.find_element_by_link_text('Edit with Elementor').click()

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

e = driver.find_element_by_link_text('Edit with Elementor').click()

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

e = driver.find_element_by_link_text('Edit with Elementor').click()

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

e = driver.find_element_by_link_text('Edit with Elementor').click()

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

e = driver.find_element_by_link_text('Edit with Elementor').click()

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

e = driver.find_element_by_link_text('Edit with Elementor').click()

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

e = driver.find_element_by_link_text('Edit with Elementor').click()

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

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn12 : kamagra-online24.com
driver.execute_script("window.open('http://kamagra-online24.com/wp-admin');")
driver.switch_to.window(driver.window_handles[11])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2021!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('http://kamagra-online24.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn13 : 179xizang.com
driver.execute_script("window.open('http://www.179xizang.com/wp-admin');")
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

driver.get('http://www.179xizang.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn14 : elitbodrum.com
driver.execute_script("window.open('https://www.elitbodrum.com/wp-admin');")
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

driver.get('https://www.elitbodrum.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn15 : mujer-nueva.com
driver.execute_script("window.open('http://www.mujer-nueva.com/wp-admin');")
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

driver.get('http://www.mujer-nueva.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn16 : whcp71.com
driver.execute_script("window.open('http://whcp71.com/wp-admin');")
driver.switch_to.window(driver.window_handles[15])

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

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn17 : cinematicmod.com
driver.execute_script("window.open('https://cinematicmod.com/wp-admin');")
driver.switch_to.window(driver.window_handles[16])

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

e = driver.find_element_by_link_text('Edit with Elementor').click()


# ============================
driver.switch_to_window(driver.window_handles[0])
# ============================





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

time.sleep(3)
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

time.sleep(3)
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

time.sleep(3)
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







# third brower
# pbn1 : musicaesmeraldas.org
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

time.sleep(3)
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

time.sleep(3)
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

# pbn8 : girls-liner.com
driver.execute_script("window.open('https://girls-liner.com/wp-admin');")
driver.switch_to.window(driver.window_handles[7])

time.sleep(3)
e = driver.find_element(By.NAME, 'log')
e.send_keys('linkpsclinic')

time.sleep(1)
e = driver.find_element(By.NAME, 'pwd')
e.send_keys('Link2022!!!')

e = driver.find_element(By.NAME, 'wp-submit').click()

# time.sleep(1)
# e = driver.find_element_by_id('menu-pages').click()

driver.get('https://girls-liner.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn9 : vslexecutivesummary.com
driver.execute_script("window.open('https://vslexecutivesummary.com/wp-admin');")
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

driver.get('https://vslexecutivesummary.com/')

e = driver.find_element_by_link_text('Edit with Elementor').click()

# ============================

# pbn10 : satomoni.com
driver.execute_script("window.open('http://satomoni.com/wp-admin');")
driver.switch_to.window(driver.window_handles[9])

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
driver.switch_to.window(driver.window_handles[10])

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
driver.switch_to.window(driver.window_handles[11])

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
driver.switch_to.window(driver.window_handles[12])

time.sleep(3)
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
driver.switch_to.window(driver.window_handles[13])

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
driver.switch_to.window(driver.window_handles[14])

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
driver.switch_to.window(driver.window_handles[15])

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
driver.switch_to.window(driver.window_handles[16])

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








# fourth brower
# pbn1 : brasserieartisanalearlesienne.com
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

time.sleep(3)
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
