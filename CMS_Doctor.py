from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium .webdriver.common.by import By

import time
S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)

class DoctorCms:

    def login(self,):
        driver.get("http://cms2.ap-south-1.elasticbeanstalk.com/auth/login")
        driver.find_element(By.XPATH,"//input[@placeholder='Enter Email']").send_keys("Ganeshwar.admin@hexahealth.com")
        driver.find_element(By.XPATH,"//input[@placeholder='Enter Password']").send_keys("Ganeswar0")
        driver.find_element(By.CSS_SELECTOR,"LOGIN").click()




    def Doctor(self,LoginPage):



      #URL=driver.get("http://cms2.ap-south-1.elasticbeanstalk.com/app/doctordetails")

