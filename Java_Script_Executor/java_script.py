from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demo.actitime.com/")
driver.implicitly_wait(30)

#ele = driver.find_element_by_id("demoCredentials")
#driver.execute_script("alert('Welcome to Pune')")
#sleep(3)
#textofEle = driver.execute_script("return document.getElementById('demoCredentials').textContent")
#print(textofEle)
domainName = driver.execute_script("return document.domain")
print("Doamin Name: ",domainName)

title = driver.execute_script("return document.title")
print("Page Title is: ",title)

URL = driver.execute_script("return document.URL")
print("URL is: ", URL)

driver.quit()
