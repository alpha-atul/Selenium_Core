from idlelib.config_key import FUNCTION_KEYS
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.youtube.com/")
sleep(3)
driver.get(driver.current_url)
#driver.switch_to.frame(0)
#driver.find_element_by_xpath("//yt-formatted-string[text()='Not now']").click()


#REFRESH COMMAND
#driver.refresh()
#sleep(3)

#SEND KEYS
#driver.find_element_by_xpath("//yt-formatted-string[text()='Trending']").send_keys(Keys.F5)
#sleep(3)
driver.quit()