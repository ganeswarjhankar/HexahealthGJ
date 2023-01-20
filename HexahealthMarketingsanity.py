import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)
#driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.get("https://www.hexahealth.com/marketing/lasik-bangalore")
#driver.maximize_window()
time.sleep(3)

driver.find_element(By.LINK_TEXT,"Book Free Consultation").click()
driver.find_element(By.XPATH,"//input[@id='leadname5']").send_keys("Free Test consultation Marketing")
driver.find_element(By.XPATH,"//input[@id='contactnum5']").send_keys("1000000010")
driver.find_element(By.XPATH,"//*[@id='LeadSubmit']").click()


time.sleep(3)

driver.back()
driver.refresh()

#driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div/i").click()
#time.sleep(3)
# Fold 2 validation and submit form
driver.execute_script("window.scrollTo(1000,document.body.scrollHeight)")
driver.find_element(By.XPATH,"//input[@id='leadnameMobile1']").send_keys("Fold 2  test check marketing")
driver.find_element(By.XPATH,"//input[@id='contactnumobile1']").send_keys("1000000090")
time.sleep(2)

driver.find_element(By.XPATH,"//button[@id='LeadSubmitMobile']").click()
time.sleep(3)

#driver.find_element(By.XPATH,"//i[@class='icon fas fa-calculator']").click()
#driver.find_element(By.XPATH,"//input[@id='leadname2']").send_keys("Test check fold")


#total = driver.find_elements(By.TAG_NAME,"a")
#print("number:",len("total"))

#for link in total:
    #print(link.text)

#driver.find_element(By.LINK_TEXT,"Book Appointment")   .click()


















