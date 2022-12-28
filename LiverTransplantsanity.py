from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support import expected_conditions, wait

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)

URL=driver.get("https://hexahealth.com/campaigns/liver-transplant")
#driver.implicitly_wait(3)
driver.maximize_window()
#if driver.find_element(By.LINK_TEXT,"WhatsApp Expert"):
    #print("Whatsapp Found")


driver.implicitly_wait(5)

driver.maximize_window()
#Verify the Free consultation button

driver.find_element(By.XPATH, "//*[@id='bkapntconslt']").click()

driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("Fold Test LT Page ")
driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000031")
driver.find_element(By.XPATH, "//*[@id='LeadSubmitNewHome']").click()
# Time Sleep
time.sleep(5)
driver.back()
driver.refresh()





# Verify the whatsApp Button
#WhatsApp = driver.find_element(By.XPATH,"//*[@id='whstpconslt']").click()
#WhatsApp.click()
#time.sleep(3)
#driver.back()

#appointment = driver.find_element(By.LINK_TEXT,"Book Appointment")
#driver.execute_script("arguments[0].click();",appointment)

time.sleep(3)



# Sleep the process

# Back the Page
#driver.back()

##################### Verify the surgery cost and check the Forms

SurgeryCost = driver.find_element(By.XPATH,"//*[@id='surgerytBtn']/span")
driver.execute_script("arguments[0].click();", SurgeryCost)

#try:
driver.find_element(By.XPATH,"//*[@id='leadnameSurgery']").send_keys("GoodLucktest Surgery")
driver.find_element(By.XPATH,"//*[@id='contactnumSurgery']").send_keys("1000000043")
driver.find_element(By.XPATH,"//*[@id='leadSubmiCalculateSurgery']").click()
#except:
    #driver.find_element(By.XPATH,"//*[@id='closemodal']").click()

time.sleep(5)
driver.back()
driver.refresh()
#Cross = driver.find_element(By.XPATH,"//*[@id='DivCostInsurance']/button")
#driver.execute_script("arguments[0].click();", Cross)

################################Verify the Check Insurance Coverage Link##########

InsuranceLT = driver.find_element(By.XPATH,"//*[@id='insurancetBtn']/span")

driver.execute_script("arguments[0].click();",InsuranceLT)


#try:
driver.find_element(By.XPATH,"//*[@id='leadnameSurgery']").send_keys("Test Insurance check sanity")
driver.find_element(By.XPATH,"//*[@id='contactnumSurgery']").send_keys("1000000082")
driver.find_element(By.XPATH,"//*[@id='leadSubmiCalculateSurgery']").click()
#except:
    #driver.find_element(By.XPATH,"//*[@id='closemodal']").click()
time.sleep(5)
driver.back()
driver.refresh()



















