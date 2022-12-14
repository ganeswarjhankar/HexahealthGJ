from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)


URL=driver.get("https://www.hexahealth.com/")
driver.implicitly_wait(12)
driver.maximize_window()
############################First fold Form######################################################
driver.find_element(By.LINK_TEXT,("Get a free second opinion from top surgeons! Book an appointment »")).click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='leadname2']").send_keys("Patient test Auto Name check")

driver.find_element(By.XPATH,"//input[@id='contactnum2']").send_keys("1000006233")
driver.find_element(By.XPATH,"//input[@name='leadcity2']").send_keys("Delhi")
driver.find_element(By.XPATH,"//input[@name='treamentcondition1']").send_keys("ACL Reconstruction Surgery ")
#driver.find_element(By.XPATH,"//textarea[@xpath='1']")
#wait = WebDriverWait(driver,10)

#wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Delhi - NCR")))
#driver.find_element(By.LINK_TEXT,"Delhi - NCR").click()

#City = Select(driver.find_element(By.XPATH,"//input[@name='leadcity2']"))
#City = Select(driver.find_element(By.XPATH,"//select[@id='leadcity2']"))
#City.select_by_visible_text( "Delhi - NCR")
#City.select_by_index(1)
driver.find_element(By.XPATH,"//textarea[@id='leadquery']").send_keys("test Auto check")

driver.find_element(By.XPATH,"//button[@id='LeadSubmitNewHome']").click()

driver.find_element(By.XPATH,"//button[@id='closemodal']").click()
time.sleep(3)
driver.back()
###############################2nd Fold Form#########################################
driver.find_element(By.XPATH,"//input[@id='leadnamehome']").send_keys("Test GJ Auto Check" )
driver.find_element(By.XPATH,"//input[@id='contactnumhome']").send_keys("1000007968")
#City2 = Select(driver.find_element(By.XPATH,"//select[@id='leadcityhome']"))
#City2.select_by_visible_text("Delhi - NCR")
driver.find_element(By.XPATH,"//input[@id='leadcityhome']").send_keys("Bengaluru")
driver.find_element(By.XPATH,"//input[@name='treamentcondition']").send_keys("Abdominal Myomectomy ")

driver.find_element(By.XPATH,"//textarea[@id='leadqueryhome']").send_keys("test GJ AUTO Form 2")

#driver.find_element(By.XPATH,"//i[@class='las la-bars mobile-navigation']").click()
#driver.find_element(By.XPATH,"//a[@id='parentheader_2']").click()
button = driver.find_element(By.XPATH,"//button[@id='LeadSubmitNewHome1']")
driver.execute_script("arguments[0].click();", button)
time.sleep(5)
driver.back()


driver.find_element(By.XPATH,"//input[@id='contactnum1']").send_keys("1000009848")
Callbutton = driver.find_element(By.XPATH,"//button[@id='LeadSubmit1']")
driver.execute_script("arguments[0].click();", Callbutton)
time.sleep(2)
#driver.back()
ThankYou = driver.find_element(By.XPATH,"//h1[@class='thankyou-title']").text
print("Passed","CallButton")
driver.refresh()




