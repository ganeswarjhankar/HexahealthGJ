"""This script is regarding the home page hexahealth and search  random letter 3 and make a match , if not found the match search the result again"""
import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)



# Navigate to a website
driver.get("https://hexahealth.com")
driver.maximize_window()
# Find the input field
input_field = driver.find_element(By.XPATH,"//*[@id='txtArticls']")

# Generate three random letters
letters = ''.join(random.choices(string.ascii_letters, k=3))

# Type the random letters into the input field
input_field.send_keys(letters)

# Select the first matching option from the suggestion list
suggestions = driver.find_elements(By.CLASS_NAME,"searchList diseaseCls hideClass")
match_found = False
for suggestion in suggestions:
    if suggestion.text.startswith(letters):
        suggestion.click()
        match_found = True
        break

# If no match is found, search again
if not match_found:
    input_field.send_keys(Keys.RETURN)

# Close the web driver
driver.quit()
