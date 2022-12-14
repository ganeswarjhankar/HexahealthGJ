#time
import time
#--Selenium webdriver
from selenium import webdriver
#--Chrome Browser
from selenium.webdriver.chrome.service import Service
from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)
#driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)

#driver.maximize_window()

driver.find_element(By.XPATH,"/html/body/app-root/app-navbar/div/nav/ul/li[2]").click()
#Step 1--make a list of element
Mobilelist = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
#step2:Count the List-element
listcount=len(Mobilelist)
#expected that Listcount must be greater than 0
#assert listcount > 0
#--iterate through the list now
for x in Mobilelist:
    blackberry = x.find_element(By.XPATH,"div/h4/a").text
    if blackberry == "Blackberry":
        x.find_element(By.XPATH,"div/button").click()
else:
    time.sleep(4)
    driver.close()





