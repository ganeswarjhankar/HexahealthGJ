from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium .webdriver.common.by import By
S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)
driver.get("https://rahulshettyacademy.com/angularpractice/shop")
driver.maximize_window()

#shop url
driver.find_element(By.XPATH,"//a[contains(@href,'shop')]").click()

products = driver.find_elements(By.XPATH,"//app-card[@class='col-lg-3 col-md-6 mb-3']")
for product in products:
    productName = product.find_element(By.XPATH,"div/div/h4/a").text
    if productName =="Blackberry":
        product.find_element(By.XPATH,"/div/button").click()

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()






#Blackberry check with multiple elements

##click on confirm

