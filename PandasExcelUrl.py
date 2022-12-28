import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

df = pd.read_excel('C:\\Users\\91928\\PycharmProjects\\MultiUrlsFile.xlsx', sheet_name='Sheet1')

urls = df['URL'].tolist()
print(urls)

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)

for i, url in enumerate(urls):
    driver.get(url)
    if i == 0:
        print("All the Testcases are passed:",url)

        driver.maximize_window()
        driver.find_element(By.LINK_TEXT,
                            ("Get a free second opinion from top surgeons! Book an appointment »")).click()

        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@id='leadname2']").send_keys("Patient test Auto Name check")

        driver.find_element(By.XPATH, "//input[@id='contactnum2']").send_keys("1000006233")
        driver.find_element(By.XPATH, "//input[@name='leadcity2']").send_keys("Delhi")
        driver.find_element(By.XPATH, "//input[@name='treamentcondition1']").send_keys("ACL Reconstruction Surgery ")
        driver.find_element(By.XPATH, "//textarea[@id='leadquery']").send_keys("test Auto check")

        driver.find_element(By.XPATH, "//button[@id='LeadSubmitNewHome']").click()

        driver.find_element(By.XPATH, "//button[@id='closemodal']").click()
        time.sleep(3)
        driver.back()
        ###############################2nd Fold Form#########################################
        driver.find_element(By.XPATH, "//input[@id='leadnamehome']").send_keys("Test GJ Auto Check")
        driver.find_element(By.XPATH, "//input[@id='contactnumhome']").send_keys("1000007968")

        driver.find_element(By.XPATH, "//input[@id='leadcityhome']").send_keys("Bengaluru")
        driver.find_element(By.XPATH, "//input[@name='treamentcondition']").send_keys("Abdominal Myomectomy ")

        driver.find_element(By.XPATH, "//textarea[@id='leadqueryhome']").send_keys("test GJ AUTO Form 2")

        button = driver.find_element(By.XPATH, "//button[@id='LeadSubmitNewHome1']")
        driver.execute_script("arguments[0].click();", button)
        time.sleep(5)
        driver.back()

        driver.find_element(By.XPATH, "//input[@id='contactnum1']").send_keys("1000009848")
        Callbutton = driver.find_element(By.XPATH, "//button[@id='LeadSubmit1']")
        driver.execute_script("arguments[0].click();", Callbutton)
        time.sleep(2)

        ThankYou = driver.find_element(By.XPATH, "//h1[@class='thankyou-title']").text
        print("Passed", "CallButton")
        driver.refresh()

        # code for the first URL
    elif i == 1:
        print("All the Testcases are passed:",url)

        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//*[@id='leadname5']").send_keys("Test Name Marketing Automate")
        driver.find_element(By.XPATH, "//*[@id='contactnum5']").send_keys("1000000876")
        driver.find_element(By.XPATH, "//*[@id='LeadSubmit']").click()
        time.sleep(5)
        driver.back()
        #################Surgery fold######################################################
        SurgeryCost = driver.find_element(By.XPATH, "//*[@id='surgerytBtn']/span")
        driver.execute_script("arguments[0].click();", SurgeryCost)
        driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("GoodLucktest")
        driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000004312")
        driver.find_element(By.XPATH, "//*[@id='LeadSubmit2']").click()
        time.sleep(5)
        driver.back()
        driver.refresh()

        ##################################insurance Fold##################################################
        Insurance = driver.find_element(By.XPATH, "//*[@id='insurancetBtn']/span")
        driver.execute_script("arguments[0].click();", Insurance)
        driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("Test Insurance check sanity")
        driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000082")
        driver.find_element(By.XPATH, "//*[@id='LeadSubmit2']").click()
        time.sleep(5)
        driver.back()
        driver.refresh()

        ##################Call Suport BUtton Lead###################

        driver.find_element(By.XPATH, "//*[@id='contactnum1']").send_keys("1000000082")
        CallButton = driver.find_element(By.XPATH, "//*[@id='LeadSubmit1_marketing']")
        driver.execute_script("arguments[0].click();", CallButton)
        time.sleep(3)

        # code for the second URL




    elif i == 2:
        print("All the Testcases are passed:",url)

        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//*[@id='leadname5']").send_keys("Test Name Marketing Automate")
        driver.find_element(By.XPATH, "//*[@id='contactnum5']").send_keys("1000000876")
        driver.find_element(By.XPATH, "//*[@id='LeadSubmit']").click()
        time.sleep(5)
        driver.back()
        #################Surgery fold######################################################
        SurgeryCost = driver.find_element(By.XPATH, "//*[@id='surgerytBtn']/span")
        driver.execute_script("arguments[0].click();", SurgeryCost)
        driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("GoodLucktest")
        driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000004312")
        driver.find_element(By.XPATH, "//*[@id='LeadSubmit2']").click()
        time.sleep(5)
        driver.back()
        driver.refresh()

        ##################################insurance Fold##################################################
        Insurance = driver.find_element(By.XPATH, "//*[@id='insurancetBtn']/span")
        driver.execute_script("arguments[0].click();", Insurance)
        driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("Test Insurance check sanity")
        driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000082")
        driver.find_element(By.XPATH, "//*[@id='LeadSubmit2']").click()
        time.sleep(5)
        driver.back()
        driver.refresh()

        ##################Call Suport BUtton Lead###################

        driver.find_element(By.XPATH, "//*[@id='contactnum1']").send_keys("1000000082")
        CallButton = driver.find_element(By.XPATH, "//*[@id='LeadSubmit1_marketing']")
        driver.execute_script("arguments[0].click();", CallButton)
        time.sleep(3)





