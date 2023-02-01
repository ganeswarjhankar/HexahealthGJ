##WhatApp
import time

import requests
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
        df = pd.read_excel('C:\\Users\\91928\\PycharmProjects\\MarketingWhatApp.xlsx', sheet_name='Sheet1')

        # select a random sample of URLs
        self.urls = df.sample(3, replace=False)['URL']

        # open each URL with Selenium and run code for it
        S = Service("D:\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=S)

    def DisplayVariant(self):
        for url in self.urls:
            self.driver.get(url)
            print([url])
            try:
                self.driver.maximize_window()

                self.driver.implicitly_wait(5)
                self.driver.find_element(By.XPATH,"//*[@id='whtsapHeaderBtn']").click()
                self.driver.implicitly_wait(2)
                #self.driver.switch_to.window(self.driver.window_handles[2])
                msg = self.driver.find_element(By.XPATH,"//p[@class='_9vd5']")
                self.driver.implicitly_wait(2)
                print(msg.text)

                # Get the current URL
                current_url = self.driver.current_url
                print(current_url)
                # Verify that the current URL contains the expected value
                response = requests.get(current_url)
                if 'api.' in current_url:
                    if response.status_code == 200:
                        print("Status Code 200 Ok")
                    else:
                        print("Failed")


                else:
                    print('Verification failed as the URl Not containing "api"')

                # response = requests.get(current_url)

                time.sleep(5)
                self.driver.refresh()
                self.driver.back()

                print("Passed")
            except:
                print("Failed")

            #finally:
                #print("This is Cost Variant Marketing Pages")

        self.driver.quit()

    #def CostVariant2(self):





##The two lines of code market_obj = MarketingPage() and market_obj.CostVariant()
# are creating an instance of the MarketingPage class and calling the CostVariant()
# method on that instance, respectively.
market_obj1 = MarketingPage()
market_obj1.DisplayVariant()

#market_obj2 = MarketingPage()
#market_obj2.CostVariant2()


