import keyboard
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://www.google.com/")
driver.maximize_window()

parent = driver.current_window_handle
print(parent)
action = ActionChains(driver)

Images = driver.find_element_by_xpath("//a[text()='Images']")
action.context_click(Images).perform()
keyboard.press("t")

allhandles = driver.window_handles

for handle in allhandles:
    if handle!=parent:
        driver.switch_to.window(handle)

