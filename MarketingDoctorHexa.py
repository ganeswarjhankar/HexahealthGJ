import time
#import requests
#import response as response
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service



S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)
driver.maximize_window()
url = driver.get("https://www.hexahealth.com/marketing/doctor/laser-fissure-bangalore")


driver.find_element(By.XPATH,"//input[@id='leadname5']").send_keys("Test Doctor Marketing lead form 1")
driver.find_element(By.XPATH,"//input[@id='contactnum5']").send_keys("1000000100")

button = driver.find_element(By.XPATH,"//button[@id='LeadSubmit']")
driver.execute_script("arguments[0].click();", button)
time.sleep(5)
CurrentUrl1 = driver.current_url
print(CurrentUrl1)
time.sleep(2)
driver.back()
driver.refresh()

BookFreeAppointment = driver.find_element (By.XPATH,"/html/body/div[1]/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[1]/div[2]")
driver.execute_script("arguments[0].click();", BookFreeAppointment)




