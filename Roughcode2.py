#import time
#import requests
#import response as response
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import random


S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)
driver.maximize_window()
url = driver.get("https://www.hexahealth.com/marketing/doctor/laser-fissure-bangalore")




# Find all the buttons with the same name
buttons = driver.find_elements(By.NAME,"Book Free Appointment")

# Generate a random number between 0 and the number of buttons
index = random.randint(0, len(buttons)-1)

# Click the button at the randomly selected index
buttons[index].click()
