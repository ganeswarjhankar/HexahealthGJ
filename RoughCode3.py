#import time
#import requests
#import response as response
#from selenium import webdriver
import time

from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


from selenium import webdriver
import random

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)
driver.maximize_window()
url = driver.get("https://www.hexahealth.com/marketing/doctor/laser-fissure-bangalore")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 1000);")
time.sleep(2)
# find all the buttons with the same name
buttons = driver.find_elements(By.XPATH,"//div[@class='doctor']/div/a")


time.sleep(2)

# select a single random button
selected_button = random.choice(buttons)
print(selected_button)
time.sleep(2)

if selected_button.is_displayed():
    # click the selected button
    selected_button.click()


else:
    print("Button is not displayed")
time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("TestDoctorMarketingRandom")
driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000100")
element = driver.find_element(By.XPATH, "//*[@id='LeadSubmit2']")
driver.execute_script("arguments[0].click()", element)


#driver.find_element(By.XPATH,"//*[@id='leadname2']").send_keys("TestDoctorMarketingRandom")
#driver.find_element(By.XPATH,"//*[@id='contactnum2']").send_keys("1000000100")
#driver.find_element(By.XPATH,"//*[@id='LeadSubmit2']").click()

