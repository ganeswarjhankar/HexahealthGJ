from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)
driver.maximize_window()
url = driver.get("https://www.hexahealth.com/marketing/doctor/laser-fissure-bangalore")






# Find the elements
Doctors = driver.find_elements(By.XPATH,"//div[@class='item card-block']/div/div/h3")



import random

from selenium import webdriver

#driver = webdriver.Chrome()
#driver.get("http://www.example.com")

# Find the list of doctors on the page
#doctors = driver.find_elements_by_css_selector("css_selector_for_doctors")

# Sort the list of doctors alphabetically by name
Doctors.sort(key=lambda x: x(By.XPATH,"//div[@class='item card-block']/div/div/h3"))

# Choose a random index from the list of doctors
index = random.randint(0, len(Doctors) - 1)

# Find the "single appointment" button for the doctor at the chosen index
doctor = Doctors[index]
#button = doctor.find_element_by_css_selector("css_selector_for_button")
button = driver.find_elements(By.XPATH,"//div[@class='item card-block']/div/div/a")

# Click on the button
button.click()

# Proceed with the rest of the code here

driver.quit()
