"""this code will only work if all the urls have the same locators"""
"""File location is mentioned as C:\Users\91928\PycharmProjects """
"""All the marketing files are placed in the Excel Files and pick any random files and print it"""

import pandas as pd
import random
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# read the list of URLs from the Excel sheet
df = pd.read_excel('C:\\Users\\91928\\PycharmProjects\\MultiUrlsFile.xlsx', sheet_name='Sheet1')

# select a random sample of URLs
urls = df.sample(3, replace=False)['URL']

# open each URL with Selenium and run code for it
S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)

for url in urls:
    driver.get(url)
    print([url])

    driver.implicitly_wait(5)
    driver.maximize_window()