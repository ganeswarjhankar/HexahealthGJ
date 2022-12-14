################Search any Entity for sanity ###########################################

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


driver.find_element(By.XPATH, "//input[@id='txtArticls']").send_keys("Apollo Hospital")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Apollo Hospital, Noida")))
driver.find_element(By.LINK_TEXT,"Apollo Hospital, Noida").click()

BannerMessage = driver.find_element(By.XPATH,"//h1[@class='banner-title mb-3']") .text

assert "Apollo Hospital, Noida" in BannerMessage
