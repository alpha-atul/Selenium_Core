from selenium import webdriver
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.braingle.com/")

driver.find_element_by_id("cell_games").click()
wait = WebDriverWait(driver,30)
ele = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/games/wtb/']")), "Checking if element is present")
#ele = driver.find_element_by_css_selector("a[href='/games/wtb/']")
ele.send_keys("")
main = driver.save_screenshot("main_page.png")
loc = ele.location
size = ele.size

x = loc['x']
y = loc['y']
width = x+size['width']
height = y+size['height']

im = Image.open('main_page.png')
im = im.crop((int(x), int(y), int(width), int(height)))
im.save('cropped_image.png')

driver.quit()