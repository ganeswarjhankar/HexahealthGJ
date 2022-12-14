from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.action_chains import ActionChains

import time
S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)
URL=driver.get("https://rahulshettyacademy.com/angularpractice/shop")
driver.maximize_window()

time.sleep(10)

for x in phonelist:
    Blackberry =  (By.XPATH,"")




driver.find_element(By.XPATH,"/html/body/app-root/app-navbar/div/nav/ul/li[2]/a").click()
driver.find_element(By.XPATH,"/html[1]/body[1]/app-root[1]/app-shop[1]/div[1]/div[1]/div[2]/app-card-list[1]/app-card[3]/div[1]/div[2]/button[1]").click()
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Checkout']").click()




