from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium import webdriver
import requests

import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

option1 = Options()
option1.add_argument("---disable-Notifications")

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)
print(driver)

#def StatusCodeCheck():

driver.maximize_window()

driver.get("https://www.hexahealth.com/marketing/display/laser-fissure-bangalore")
url = driver.current_url
print(url)

response = requests.get(url)
print(url)

driver.find_element(By.XPATH,"//*[@id='whtsapHeaderBtn']/span/b").click()

wait1 = WebDriverWait(driver,10)
#wait1.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Delhi - NCR")))

#wait.until(EC.url_matches(r"^https://api\..*\.com$"))
check = wait1.until(expected_conditions.url_contains("https://www.api."))
print(check)


if response.status_code == 200:
    print("Status Code 200 Ok")
else:
    print("Failed")






