#time
import time
#--Selenium webdriver
from selenium import webdriver
#Headless
#from selenium.webdriver.Chrome.options import Options
#options = webdriver.ChromeOptions()
#---#chrome_options = webdriver.ChromeOptions()
#-----#chrome_options.add_argument("headless")



#--Chrome Browser
from selenium.webdriver.chrome.service import Service
from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select

##----Explicit wait imports--##

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)
#####-------##options=chrome_options
#driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.get("https://rahulshettyacademy.com/angularpractice/")

#implicit wait need to be used\
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"/html/body/app-root/app-navbar/div/nav/ul/li[2]/a").click()

Phonelist = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for x in Phonelist:
    blackberry = x.find_element(By.XPATH,"div/h4/a").text
    if blackberry=="Blackberry":
        x.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"/html/body/app-root/app-shop/nav/div/div/ul/li").click()
driver.find_element(By.XPATH,"/html/body/app-root/app-shop/div/div/div/table/tbody/tr[3]/td[5]/button").click()

driver.find_element(By.XPATH,"/html/body/app-root/app-shop/div/app-checkout/div/div[1]/input").send_keys("ind")

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()

driver.find_element(By.XPATH,"/html/body/app-root/app-shop/div/app-checkout/div/div[2]/label").click()
driver.find_element(By.XPATH,"/html/body/app-root/app-shop/div/app-checkout/div/form/input").click()
SuccessText = driver.find_element(By.XPATH,"/html/body/app-root/app-shop/div/app-checkout/div[2]/div").text

assert "Success! Thank you!" in SuccessText




