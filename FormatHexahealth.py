import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
option1 = Options()
option1.add_argument("---disable-Notifications")

class MarketingPage:

    def __init__(self):
        from selenium.webdriver.chrome.service import Service
        from selenium import webdriver





        # open each URL with Selenium and run code for it

        S = Service("D:\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=S)
        self.driver.get("https://hexahealth.com")






    def HexaFold1(self):



        try:
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            time.sleep(5)
            self.driver.find_element(By.LINK_TEXT,("Get a FREE Second Opinion from Top Surgeons! Book an Appointment »")).click()

            self.driver.find_element(By.XPATH, "//input[@id='leadname2']").send_keys("Patient test Auto Name check")

            self.driver.find_element(By.XPATH, "//input[@id='contactnum2']").send_keys("1000000100")
            self.driver.find_element(By.XPATH, "//input[@name='leadcity2']").send_keys("Delhi")
            self.driver.find_element(By.XPATH, "//input[@name='treamentcondition1']").send_keys(
                "ACL Reconstruction Surgery ")
            self.driver.find_element(By.XPATH, "//textarea[@id='leadquery']").send_keys("test Auto check")

            self.driver.find_element(By.XPATH, "//button[@id='LeadSubmitNewHome']").click()

            self.driver.find_element(By.XPATH, "//button[@id='closemodal']").click()
            time.sleep(3)
            self.driver.back()
            print('HexaFold1 is Passed')


        except:
                print("HexaFold1  Failed")
        finally:
            print("HexaFold1 all Passed")









        self.driver.quit()

    def HexaFold2(self):

        try:
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            self.driver.find_element(By.XPATH, "//input[@id='leadnamehome']").send_keys("Test GJ Auto Check")
            self.driver.find_element(By.XPATH, "//input[@id='contactnumhome']").send_keys("1000007968")
            # City2 = Select(driver.find_element(By.XPATH,"//select[@id='leadcityhome']"))
            # City2.select_by_visible_text("Delhi - NCR")
            self.driver.find_element(By.XPATH, "//input[@id='leadcityhome']").send_keys("Bengaluru")
            self.driver.find_element(By.XPATH, "//input[@name='treamentcondition']").send_keys("Abdominal Myomectomy ")

            self.driver.find_element(By.XPATH, "//textarea[@id='leadqueryhome']").send_keys("test GJ AUTO Form 2")
            button =self.driver.find_element(By.XPATH, "//button[@id='LeadSubmitNewHome1']")
            self.driver.execute_script("arguments[0].click();", button)
            time.sleep(5)
            self.driver.back()
            print("HexaFold 2 Form  Passed")



        except:
            print("HexaFold 2 Form")

        self.driver.quit()

    def Cmercury(self):
        self.driver.maximize_window()
        self.driver.close()


        pass




##The two lines of code market_obj = MarketingPage() and market_obj.CostVariant()
# are creating an instance of the MarketingPage class and calling the CostVariant()
# method on that instance, respectively.
HexaHomeFold1_obj = MarketingPage()
HexaHomeFold1_obj.HexaFold1()

HexaHomeFold2_obj = MarketingPage()
HexaHomeFold2_obj.HexaFold2()

HexaMercury_obj= MarketingPage()
HexaMercury_obj.Cmercury()

   