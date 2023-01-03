#####Script for the "Display" Marketing pages###################


import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

#from MarketingCustomizedHexahealth import response

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)
driver.maximize_window()
url = driver.get("https://www.hexahealth.com/marketing/display/laser-fissure-bangalore")

# Locate the button element
button = driver.find_element(By.XPATH,"//*[@id='whtsapHeaderBtn']/span/b").click()
time.sleep(5)

# Click the button
#button.click()

# Get the current URL
current_url = driver.current_url
print(current_url)
# Verify that the current URL contains the expected value
if 'api.' in current_url:
    print('Verification successful')
else:
    print('Verification failed')

response = requests.get(current_url)


if response.status_code == 200:
    print("Status Code 200 Ok")
else:
    print("Failed")

# Close the browser
driver.quit()
