#####this code will only work if all teh urls have the same locators#############

import pandas as pd
import random
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# read the list of URLs from the Excel sheet
df = pd.read_excel('C:\\Users\\91928\\PycharmProjects\\MultiUrlsFile.xlsx', sheet_name='Sheet1')

# select a random sample of URLs
urls = df.sample(3,replace= False)['URL']

# open each URL with Selenium and run code for it
S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)

for url in urls:
    driver.get(url)
    print([url])

    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.find_element(By.XPATH, "//*[@id='leadname5']").send_keys("Test Name Marketing Automate")
    driver.find_element(By.XPATH, "//*[@id='contactnum5']").send_keys("1000000876")
    FirstForm =  driver.find_element(By.XPATH, "//*[@id='LeadSubmit']").click()
    print("passed:")
    time.sleep(5)
    driver.back()
    #################Surgery fold######################################################
    time.sleep(3)
    SurgeryCost = driver.find_element(By.XPATH, "//*[@id='surgerytBtn']/span")
    driver.execute_script("arguments[0].click();", SurgeryCost)
    driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("GoodLucktest")
    driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000004312")
    SurgeryClick = driver.find_element(By.XPATH, "//*[@id='LeadSubmit2']").click()
    print("Passed:")

    time.sleep(5)
    driver.back()
    driver.refresh()

    ##################################insurance Fold##################################################
    Insurance = driver.find_element(By.XPATH, "//*[@id='insurancetBtn']/span")
    driver.execute_script("arguments[0].click();", Insurance)
    driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("Test Insurance check sanity")
    driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000082")
    InsuranceClick = driver.find_element(By.XPATH, "//*[@id='LeadSubmit2']").click()
    print("passed:")
    time.sleep(5)
    driver.back()
    driver.refresh()

    ##################Call Suport BUtton Lead###################

    driver.find_element(By.XPATH, "//*[@id='contactnum1']").send_keys("1000000082")
    CallButton = driver.find_element(By.XPATH, "//*[@id='LeadSubmit1_marketing']")

    driver.execute_script("arguments[0].click();", CallButton)
    print("passed:")
    time.sleep(3)


driver.quit()
