from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from webevent_listeners.MyListeners import MyListeners

driver = webdriver.Chrome()
eDriver = EventFiringWebDriver(driver, MyListeners())
eDriver.implicitly_wait(30)
eDriver.maximize_window()
eDriver.get("https://www.seleniumhq.org/download/")

eDriver.find_element_by_xpath("//span[contains(text(),'Safety Features')]").click()

eDriver.close()