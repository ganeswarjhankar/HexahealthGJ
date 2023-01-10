from selenium.webdriver.common.by import By


class MarketingPage:

    def __init__(self):
        import pandas as pd
        import random
        from selenium.webdriver.chrome.service import Service
        from selenium import webdriver
        import time
        from selenium.webdriver.common.by import By

        # read the list of URLs from the Excel sheet
        df = pd.read_excel('C:\\Users\\91928\\PycharmProjects\\MultiUrlsFileCost.xlsx', sheet_name='Sheet1')

        # select a random sample of URLs
        self.urls = df.sample(3, replace=False)['URL']

        # open each URL with Selenium and run code for it
        S = Service("D:\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=S)

    def CostVariant(self):
        for url in self.urls:
            self.driver.get(url)
            print([url])
            try:
                self.driver.maximize_window()
                self.driver.implicitly_wait(5)
                self.driver.find_element(By.XPATH, "//input[@id='rNo']").click()
                self.driver.find_element(By.XPATH, "//input[@id='contactnumhomem']").send_keys("1000000100")
                self.driver.find_element(By.XPATH, "//button[@id='LeadSubmitCostPageMaster']").click()
                print("Passed")
            except:
                print("Failed")

            finally:
                print("All the marketing pages are above")

        self.driver.quit()


##The two lines of code market_obj = MarketingPage() and market_obj.CostVariant()
# are creating an instance of the MarketingPage class and calling the CostVariant()
# method on that instance, respectively.
market_obj = MarketingPage()
market_obj.CostVariant()
