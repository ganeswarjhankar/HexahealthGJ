


import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

#from MarketingCustomizedHexahealth import response

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)
driver.maximize_window()
url = driver.get("https://www.hexahealth.com/marketing/display/laser-fissure-bangalore")

# Locate the button element
#button = driver.find_element(By.XPATH,"//*[@id='whtsapHeaderBtn']/span/b").click()
buttons = driver.find_elements(By.CSS_SELECTOR,'WhatsApp Expert')
print(buttons)
time.sleep(5)




# Click each button
for button in buttons:
    button.click()
#print(buttons)
# Close the browser
#driver.quit()


number_li_elems=len(WebDriverWait(browser,30).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "li.clickable_area"))))
for x in range(number_li_elems):
    # you have to get the element by index every time, otherwise you will get StaleElement Exception
    button = browser.find_element_by_css_selector("li.clickable_area:nth-child(" + str(x+1) + ") > div:nth-child(3)")
    button.click()