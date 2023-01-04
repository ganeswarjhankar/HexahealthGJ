import time
import requests
#import response as response
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service



S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)
driver.maximize_window()
url = driver.get("https://www.hexahealth.com/marketing/display/laser-fissure-bangalore")


# Locate the button element
#buttons = driver.find_elements(By.XPATH,"//*[@id='whtsapHeaderBtn']/span/b")
buttons = driver.find_element(By.XPATH,"//*[@id='whtsapHeaderBtn']/span/b").click()
#buttons = driver.find_elements(By.CSS_SELECTOR,'WhatsApp Expert')






    # code to execute on each page goes here

    # Get the current URL
current_url = driver.current_url
print(current_url)
# Verify that the current URL contains the expected value
response = requests.get(current_url)
if 'api.' in current_url:
    if response.status_code == 200:
        print("Status Code 200 Ok")
    else:
        print("Failed")

    print('Verification successful')

else:
    print('Verification failed as the URl Not containing "api"')

#response = requests.get(current_url)

time.sleep(3)
#driver.back()


buttons = driver.find_elements(By.XPATH,"//*[@id='whtsapHeaderBtn']/span/b")

