######################################Duplicate Rough Marketing ################################
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium .webdriver.common.by import By

import time
S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)

URL=driver.get("https://www.hexahealth.com/marketing/lasik-bangalore")

driver.maximize_window()


driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='leadname5']").send_keys("Test Name Marketing Automate")
driver.find_element(By.XPATH,"//*[@id='contactnum5']").send_keys("1000000876")
driver.find_element(By.XPATH,"//*[@id='LeadSubmit']").click()
time.sleep(5)
driver.back()
SurgeryCost = driver.find_element(By.XPATH,"//*[@id='surgerytBtn']/span")
driver.execute_script("arguments[0].click();", SurgeryCost)
driver.find_element(By.XPATH,"//*[@id='leadname2']").send_keys("GoodLucktest")
driver.find_element(By.XPATH,"//*[@id='contactnum2']").send_keys("1000004312")
driver.find_element(By.XPATH,"//*[@id='LeadSubmit2']").click()
time.sleep(5)
driver.back()
driver.refresh()
######################### Verify the Check Insurance Coverage Link##################################
Insurance = driver.find_element(By.XPATH,"//*[@id='insurancetBtn']/span/strong")
driver.execute_script("arguments[0].click();", Insurance)
driver.find_element(By.XPATH,"//*[@id='leadname2']").send_keys("Test Insurance check sanity")
driver.find_element(By.XPATH,"//*[@id='contactnum2']").send_keys("1000000082")
driver.find_element(By.XPATH,"//*[@id='LeadSubmit2']").click()
time.sleep(5)
driver.back()

driver.refresh()

time.sleep(5)




####################Verify CallButton##############################
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#CallButton =driver.find_element(By.XPATH,"//input[@id='contactnum1']").send_keys("1000000459")
#driver.execute_script("arguments[0].scrollIntoView();",CallButton)
#CallButton.send_keys("1000000459")
#driver.find_element(By.XPATH,"//button[@id='LeadSubmit1_marketing']").click()
####################Verify CallButton##############################













