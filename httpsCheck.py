
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert

from selenium .webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.chrome.options import Options
option1 = Options()
option1.add_argument("---disable-Notifications")







S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)
URL=driver.get("https://httpstatus.io/")

driver.implicitly_wait(12)
driver.maximize_window()

#urls = pd.read_excel("C:\\Users\\91928\\PycharmProjects\\MultiUrlsFileDoctor.xlsx", sheet_name='Sheet1')


url = "https://www.hexahealth.com/marketing/doctor/laser-fissure-bangalore"
driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/section[2]/div/form/div[1]/div/p[1]/textarea").send_keys(url)
driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/button").click()


wait = WebDriverWait(driver,10)


wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Check status")))

wait.click()


#driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/section[1]/div/form/div[2]/div/a").click()



#driver.switch_to.default_content()
button = driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/section[1]/div/form/div[2]/div/a")
driver.execute_script("arguments[0].click();", button)

