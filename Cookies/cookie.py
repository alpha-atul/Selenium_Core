from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.braingle.com/")

Cookie = {'name':'Atul', 'value':'201'}

driver.add_cookie(Cookie)
print("Cookie has been added")
sleep(2)
cookie = driver.get_cookie("Atul")
print(cookie['value'])

driver.quit()