##Check Hit
from selenium.webdriver.common.by import By


class MarketingDoctorPage:

    def __init__(self):
        import pandas as pd
        import random
        from selenium.webdriver.chrome.service import Service
        from selenium import webdriver
        import time
        from selenium.webdriver.common.by import By

        # read the list of URLs from the Excel sheet
        df = pd.read_excel("C:\\Users\\91928\\PycharmProjects\\MultiUrlsFileDoctor.xlsx", sheet_name='Sheet1')

        # select a random sample of URLs
        self.urls = df.sample(3, replace=False)['URL']

        # open each URL with Selenium and run code for it
        S = Service("D:\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=S)

    def DoctorVariant(self):
        for url in self.urls:
            self.driver.get(url)
            print([url])
            try:
                self.driver.maximize_window()
                self.driver.implicitly_wait(5)
                self.driver.find_element(By.XPATH, "//input[@id='leadname5']").send_keys("Test GJ Doctor Variant")
                self.driver.find_element(By.XPATH, "//input[@id='contactnum5']").send_keys("1000000100")
                self.driver.find_element(By.XPATH, "//button[@id='LeadSubmit']").click()
                print("Passed")
            except:
                print("Failed")

            finally:
                print("This is Doctor Variant Marketing Pages")

        self.driver.quit()


##The two lines of code market_obj = MarketingPage() and market_obj.CostVariant()
# are creating an instance of the MarketingPage class and calling the CostVariant()
# method on that instance, respectively.
doctor_obj = MarketingDoctorPage()
doctor_obj.DoctorVariant()
