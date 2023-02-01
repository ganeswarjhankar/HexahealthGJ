################Search any Entity for sanity ###########################################
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

# import time

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)

driver.get("https://www.hexahealth.com/")
driver.implicitly_wait(5)
driver.maximize_window()

# SearchBox = driver.find_element(By.XPATH,"//input[@id='txtArticls']").send_keys("Anu")


driver.find_element(By.XPATH, "//input[@id='txtArticls']").send_keys("Apollo Hospital, Noida")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Apollo Hospital, Noida")))
driver.find_element(By.LINK_TEXT,"Apollo Hospital, Noida").click()


#BannerMessage = driver.find_element(By.XPATH,"//h1[@class='banner-title mb-3']") .text

#assert "Apollo Hospital, Noida" in BannerMessage
handles = driver.window_handles
print(handles)


driver.switch_to.window(handles[0])
driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/div[4]/div/a[1]/i").click()

driver.find_element(By.XPATH,"//*[@id='leadnamehome2']").send_keys("Test GJ Patient Name")
driver.find_element(By.XPATH,"//*[@id='contactnumhome2']").send_keys("1000000100")
driver.find_element(By.XPATH,"//*[@id='treatmentcondition2']").send_keys("Laparoscopy")
driver.find_element(By.XPATH,"//*[@id='LeadSubmitHospital2']").click()
Handles2 = driver.window_handles[0]
print(Handles2)
ThankYou = driver.find_element(By.XPATH,"/html/body/div/div/div/h1").text
print("Thank You screen")
driver.back()
time.sleep(2)
driver.refresh()













#driver.switch_to.active_element.find_element(By.LINK_TEXT," Book Appointment ").click()


