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
url = driver.get("https://www.hexahealth.com/marketing/doctor/laser-fissure-bangalore")

products = driver.find_elements(By.XPATH,"//div[@class='doctor']")
for product in products:
    product.find_element(By.XPATH,"div/a").click()