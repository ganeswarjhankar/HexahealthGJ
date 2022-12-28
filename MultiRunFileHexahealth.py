#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from selenium .webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions, wait
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
option1 = Options()
option1.add_argument("---disable-Notifications")

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)

def HexahealthSanity():
    # Code to be executed in the first tab

    URL1 =driver.get("https://hexahealth.com")


    # Perform some actions in the first tab

    driver.implicitly_wait(12)
    driver.maximize_window()
############################First fold Form######################################################

    driver.find_element(By.LINK_TEXT,("Get a free second opinion from top surgeons! Book an appointment »")).click()


    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@id='leadname2']").send_keys("Patient test Auto Name check")

    driver.find_element(By.XPATH,"//input[@id='contactnum2']").send_keys("1000006233")
    driver.find_element(By.XPATH,"//input[@name='leadcity2']").send_keys("Delhi")
    driver.find_element(By.XPATH,"//input[@name='treamentcondition1']").send_keys("ACL Reconstruction Surgery ")
    driver.find_element(By.XPATH,"//textarea[@id='leadquery']").send_keys("test Auto check")

    driver.find_element(By.XPATH,"//button[@id='LeadSubmitNewHome']").click()

    driver.find_element(By.XPATH,"//button[@id='closemodal']").click()
    time.sleep(3)
    driver.back()
###############################2nd Fold Form#########################################
    driver.find_element(By.XPATH,"//input[@id='leadnamehome']").send_keys("Test GJ Auto Check" )
    driver.find_element(By.XPATH,"//input[@id='contactnumhome']").send_keys("1000007968")

    driver.find_element(By.XPATH,"//input[@id='leadcityhome']").send_keys("Bengaluru")
    driver.find_element(By.XPATH,"//input[@name='treamentcondition']").send_keys("Abdominal Myomectomy ")

    driver.find_element(By.XPATH,"//textarea[@id='leadqueryhome']").send_keys("test GJ AUTO Form 2")

    button = driver.find_element(By.XPATH,"//button[@id='LeadSubmitNewHome1']")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    driver.back()


    driver.find_element(By.XPATH,"//input[@id='contactnum1']").send_keys("1000009848")
    Callbutton = driver.find_element(By.XPATH,"//button[@id='LeadSubmit1']")
    driver.execute_script("arguments[0].click();", Callbutton)
    time.sleep(2)

    ThankYou = driver.find_element(By.XPATH,"//h1[@class='thankyou-title']").text
    print("Passed","CallButton")
    driver.refresh()
    #driver.close()
########################################End of Code 1############################################

def MarketingSanity():

    URL2 = driver.get("https://www.hexahealth.com/marketing/lasik-bangalore")


    driver.maximize_window()

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





def LTsanity():

    # Code to be executed in the third tab






    URL3 = driver.get("https://hexahealth.com/campaigns/liver-transplant")

    # driver.implicitly_wait(3)
    driver.maximize_window()


    driver.implicitly_wait(5)

    driver.maximize_window()
    # Verify the Free consultation button
    driver.find_element(By.XPATH, "//*[@id='bkapntconslt']").click()
    driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("Fold Test LT Page ")
    driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000031")
    driver.find_element(By.XPATH, "//*[@id='LeadSubmitNewHome']").click()

    time.sleep(5)
    driver.back()
    driver.refresh()




    time.sleep(3)


    ##################### Verify the surgery cost and check the Forms

    SurgeryCost = driver.find_element(By.XPATH, "//*[@id='surgerytBtn']/span")
    driver.execute_script("arguments[0].click();", SurgeryCost)

    # try:
    driver.find_element(By.XPATH, "//*[@id='leadnameSurgery']").send_keys("GoodLucktest Surgery")
    driver.find_element(By.XPATH, "//*[@id='contactnumSurgery']").send_keys("1000000043")
    driver.find_element(By.XPATH, "//*[@id='leadSubmiCalculateSurgery']").click()
    # except:
    # driver.find_element(By.XPATH,"//*[@id='closemodal']").click()

    time.sleep(5)
    driver.back()
    driver.refresh()

    ################################Verify the Check Insurance Coverage Link##########

    InsuranceLT = driver.find_element(By.XPATH, "//*[@id='insurancetBtn']/span")

    driver.execute_script("arguments[0].click();", InsuranceLT)

    # try:
    driver.find_element(By.XPATH, "//*[@id='leadnameSurgery']").send_keys("Test Insurance check sanity")
    driver.find_element(By.XPATH, "//*[@id='contactnumSurgery']").send_keys("1000000082")
    SurgeryClick = driver.find_element(By.XPATH, "//*[@id='leadSubmiCalculateSurgery']").click()
    print(SurgeryClick)
    # except:
    # driver.find_element(By.XPATH,"//*[@id='closemodal']").click()
    time.sleep(5)
    driver.back()
    driver.refresh()


codes = [HexahealthSanity, MarketingSanity, LTsanity]

for code in codes:
    # Open a new tab
    driver.execute_script("window.open('about:blank', '_blank');")

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])

    # Run the code in the new tab
    code()

    # Close the tab
    driver.close()

    # Switch back to the original tab
    driver.switch_to.window(driver.window_handles[0])

driver.close()
