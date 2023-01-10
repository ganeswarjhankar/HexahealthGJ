"""this code will only work if all the urls have the same locators"""
"""Cost variant of the marketing pages """

"""All the marketing files are placed in the Excel Files and pick any random files and print it"""

import pandas as pd
import random
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# read the list of URLs from the Excel sheet
df = pd.read_excel('C:\\Users\\91928\\PycharmProjects\\MultiUrlsFileCost.xlsx', sheet_name='Sheet1')

# select a random sample of URLs
urls = df.sample(3, replace=False)['URL']

# open each URL with Selenium and run code for it
S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)

for url in urls:
    driver.get(url)
    print([url])
    try:
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//input[@id='rNo']").click()
        driver.find_element(By.XPATH, "//input[@id='contactnumhomem']").send_keys("1000000100")
        driver.find_element(By.XPATH, "//button[@id='LeadSubmitCostPageMaster']").click()
        print("Passed")
    except:
        print("Failed")

    finally:
        print("All the marketing pages are above")


driver.quit()
