import time

from selenium.webdriver.common.by import By


class MarketingDoctorPage1:

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

    def CheckInsuranceCoverage1(self):
        self.driver.implicitly_wait(5)
        for url in self.urls:
            self.driver.get(url)
            print([url])
            try:
                self.driver.maximize_window()
                self.driver.execute_script("window.scrollTo(0, 2000)")
                time.sleep(2)
                Insurance = self.driver.find_element(By.XPATH, "//*[@id='insurancetBtn']/span")
                self.driver.execute_script("arguments[0].click();", Insurance)
                self.driver.find_element(By.XPATH, "//input[@id='leadname2']").send_keys("Test GJ Normal Marketing ")
                self.driver.find_element(By.XPATH, "//input[@id='contactnum2']").send_keys("1000000100")
                self.driver.find_element(By.XPATH, "//button[@id='LeadSubmit2']").click()
                self.driver.back()
                print("CheckInsuranceCoverage Passed")
            except:
                print("CheckInsuranceCoverage Failed")

            finally:
                print("This is CheckInsuranceCoverage Normal Marketing Pages")

        self.driver.quit()


insurance1_obj = MarketingDoctorPage1()
insurance1_obj.CheckInsuranceCoverage1()

