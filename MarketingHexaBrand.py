#import time
#import requests
#import response as response
#from selenium import webdriver
#import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


from selenium import webdriver
#import random

#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.support.wait import WebDriverWait

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)
driver.maximize_window()
url = driver.get("https://www.hexahealth.com/marketing/brand/hexa")




driver.find_element(By.XPATH,"//input[@id='rYes']").click()
driver.find_element(By.XPATH,"//input[@id='contactnumhomem']").send_keys("1000000100")
citysel = Select(driver.find_element(By.XPATH,"//select[@id='leadcitybrand']"))
#citysel.select_by_visible_text("Bengaluru")
citysel.select_by_index(2)
Treatmentsel = Select(driver.find_element(By.XPATH,"//select[@id='treamentconditionbrand']")).select_by_index(2)

