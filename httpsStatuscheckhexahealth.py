from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium .webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium import webdriver
import requests

import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
option1 = Options()
option1.add_argument("---disable-Notifications")

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)


driver.get("https://www.hexahealth.com/marketing/display/laser-fissure-bangalore")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Use Selenium to navigate to the webpage
driver.get("http://www.example.com")

# Wait for the webpage to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "some-element-id")))

# Get the URL of the current webpage
url = driver.current_url

# Send a HTTP request to the URL and store the response
response = requests.get(url)

# Check the status code of the response
if response.status_code == 200:
    print("The webpage is available and returned a 200 OK status code.")
else:
    print("The webpage is not available or returned a different status code.")








