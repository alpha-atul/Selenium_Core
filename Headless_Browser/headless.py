from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.google.com/")
navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

''' Calculate the performance'''
backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart

print("Back End: %s" % backendPerformance_calc)
print("Front End: %s" % frontendPerformance_calc)

ele = driver.find_element_by_name("q")
ele.send_keys("Maserati")
ele.submit()
list1 = driver.find_elements_by_css_selector("div.r > a")

for item in list1:
    print(item.text)

driver.quit()