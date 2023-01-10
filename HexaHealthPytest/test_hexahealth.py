from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from selenium .webdriver.common.by import By
import time


from selenium.webdriver.chrome.options import Options

from HexaUtilities.HexaBaseClass import HexaBaseClass

option1 = Options()
option1.add_argument("---disable-Notifications")

"""#@pytest.mark.usefixtures("setup")  Moved to the HexaBase.py file this line"""
"""HexahealthPage class is the child class and hexabaseClass is the Parent class (Inheritance property is implemented ) Setup class(browser invoke)"""
class HexahealthPage(HexaBaseClass):

    def HexaHomePage(self):
        self.driver.find_element(By.XPATH, "//textarea[@id='leadquery']").send_keys("test Auto check")

        self.driver.find_element(By.XPATH, "//button[@id='LeadSubmitNewHome']").click()

        self.driver.find_element(By.XPATH, "//button[@id='closemodal']").click()
        time.sleep(3)
        self.driver.back()

        self.driver.find_element(By.XPATH, "//input[@id='leadnamehome']").send_keys("Test GJ Auto Check")
        self.driver.find_element(By.XPATH, "//input[@id='contactnumhome']").send_keys("1000007968")
        self.driver.find_element(By.XPATH, "//input[@id='leadcityhome']").send_keys("Bengaluru")
        self.driver.find_element(By.XPATH, "//input[@name='treamentcondition']").send_keys("Abdominal Myomectomy ")

        self.driver.find_element(By.XPATH, "//textarea[@id='leadqueryhome']").send_keys("test GJ AUTO Form 2")

        button = self.driver.find_element(By.XPATH, "//button[@id='LeadSubmitNewHome1']")
        self.driver.execute_script("arguments[0].click();", button)





