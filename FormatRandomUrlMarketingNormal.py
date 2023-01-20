"""FormalRandomUrlmarketingNormal File"""
import time

from selenium.common.exceptions import WebDriverException, NoSuchWindowException
from selenium.webdriver.common.by import By


class MarketingNormalClass:


    def __init__(self):
        import pandas as pd
        import random
        from selenium.webdriver.chrome.service import Service
        from selenium import webdriver
        import time
        from selenium.webdriver.common.by import By

        # read the list of URLs from the Excel sheet
        df = pd.read_excel("C:\\Users\\91928\\PycharmProjects\\MultiUrlsFileMarketingNormal.xlsx", sheet_name='Sheet1')

        # select a random sample of URLs
        self.urls = df.sample(3, replace=False)['URL']

        # open each URL with Selenium and run code for it
        S = Service("D:\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=S)

    def MarketingNormalForm1(self):
        self.driver.implicitly_wait(5)
        for url in self.urls:
            self.driver.get(url)
            print([url])
            try:
                self.driver.maximize_window()
                self.driver.implicitly_wait(5)
                self.driver.find_element(By.XPATH, "//input[@id='leadname5']").send_keys("Test GJ Normal Marketing ")
                self.driver.find_element(By.XPATH, "//input[@id='contactnum5']").send_keys("1000000100")
                time.sleep(2)
                self.driver.find_element(By.XPATH, "//button[@id='LeadSubmit']").click()
                print("MarketingNormalForm1 is passed")
                #time.sleep(3)
                # self.driver.back()
                # time.sleep(2)
                # self.driver.refresh()





            except KeyboardInterrupt:

                print("MarketingNormalForm1 Failed")
            except WebDriverException:
                print("user Aborted the process")
            except NoSuchWindowException:
                print("User Aborted the process 2")


            finally:
                print("This is Marketing Normal Variant Marketing Pages")

        self.driver.quit()

    def CalculateSurgeryCost(self):
        self.driver.implicitly_wait(5)
        for url in self.urls:
            self.driver.get(url)
            print([url])
            try:
                self.driver.maximize_window()
                time.sleep(2)
                self.driver.implicitly_wait(5)
                self.driver.execute_script("window.scrollTo(0, 2000)")
                time.sleep(2)
                self.driver.find_element(By.XPATH, "//*[@id='surgerytBtn']/span").click()

                self.driver.find_element(By.XPATH, "//input[@id='leadname2']").send_keys("Test GJ Normal Marketing ")
                self.driver.find_element(By.XPATH, "//input[@id='contactnum2']").send_keys("1000000100")
                self.driver.find_element(By.XPATH, "//button[@id='LeadSubmit2']").click()
                time.sleep(2)
                # self.driver.back()
                # self.driver.refresh()
                print("CalculateSurgeryCost Passed")


            except:
                print("CalculateSurgeryCost Failed")

            finally:
                print("This is CalculateSurgeryCost Variant Marketing Pages")

        self.driver.quit()

    def CheckInsuranceCoverage(self):
        self.driver.implicitly_wait(5)
        for url in self.urls:
            self.driver.get(url)
            print([url])
            try:
                self.driver.maximize_window()
                time.sleep(2)
                self.driver.implicitly_wait(5)
                self.driver.execute_script("window.scrollTo(0, 2000)")
                time.sleep(2)
                Insurance = self.driver.find_element(By.XPATH, "//*[@id='insurancetBtn']/span")
                self.driver.execute_script("arguments[0].click();", Insurance)
                self.driver.find_element(By.XPATH, "//input[@id='leadname2']").send_keys("Test GJ Normal Marketing ")
                self.driver.find_element(By.XPATH, "//input[@id='contactnum2']").send_keys("1000000100")
                self.driver.find_element(By.XPATH, "//button[@id='LeadSubmit2']").click()
                time.sleep(2)
                # self.driver.back()
                print("CheckInsuranceCoverage Passed")
            except:
                print("CheckInsuranceCoverage Failed")

            finally:
                print("This is CheckInsuranceCoverage Normal Marketing Pages")

        self.driver.quit()


##The two lines of code market_obj = MarketingPage() and market_obj.CostVariant()
# are creating an instance of the MarketingPage class and calling the CostVariant()
# method on that instance, respectively.
NormalForm1_obj = MarketingNormalClass()
NormalForm1_obj.MarketingNormalForm1()

Normalsurgery_obj = MarketingNormalClass()
Normalsurgery_obj.CalculateSurgeryCost()

Normalinsurance_obj = MarketingNormalClass()
Normalinsurance_obj.CheckInsuranceCoverage()
