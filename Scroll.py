from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


import time

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)


URL=driver.get("https://www.hexahealth.com/")
print("URL")
driver.maximize_window()
#scroll down for Pixel Method

#driver.execute_script("window.scrollBy(0,3100)","")

Appointment = driver.find_element(By.LINK_TEXT,("Get a free second opinion from top surgeons! Book an appointment »")).click()

driver.switch_to.window("Free Appointment")

driver.find_element(By.ID,"closemodal").click()
#print(driver.find_element(By.ID,"appointmodal").text)



#print(driver.find_element(By.ID,"appointmodal").text)


#print(driver.find_element(By.TAG_NAME,"Free Appointment").text)


driver.find_element(By.XPATH,"//*[@id='leadname2]").send_keys("Check")
#driver.switch_to.window(windowsOpened[0])
#driver.find_element(By.TAG_NAME, "h3").text
#assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text





#driver.find_element(By.XPATH,"//body/div[@id='appointmodal']/div[1]/div[1]/div[1]/button[1]/span[1]").click()
#print("Appointment")

#a#ction.move_to_element(By.XPATH,"//*[@id='closemodal']").click().perform()


#driver.find_element(By.XPATH,"//*[@id='leadname2']").send_keys("Form1_PatientName")
#driver.find_element(By.ID,"contactnum2").send_keys("7896544568")
#print(driver.find_element(By.ID,"appointModalLabel").text)

#driver.switch_to.frame(driver.find_element(By.XPATH,"//*[@id='appointmodal']/div/div/div[2]"))
#driver.find_element(By.ID,"leadquery").send_keys("Form1_PatientName is  test")

#driver.find_element(By.XPATH,"//*[@id='closemodal']").click()

#time.sleep(5)



#Scroll down page till the element is visible
#Consultation = driver.find_element(By.CLASS_NAME,"consultation-form")
#driver.execute_script("arguments[0].scrollIntoView();",Consultation)
#driver.find_element(By.CLASS_NAME,"form-control").send_keys("TestCheck")
#driver.find_element(By.CSS_SELECTOR,"input[id='contactnumhome']").send_keys("9438857617")
#driver.find_element(By.XPATH,"//*[@id='leadcityhome']/option[2]").click()
#driver.find_element(By.XPATH,"//*[@id='leadqueryhome']").send_keys("This is a Good Query test By GJ")

#time.sleep(5)
#scroll
#BookNow = driver.find_element(By.ID,"LeadSubmitNewHome1")
#driver.execute_script("arguments[0].click();",BookNow)
#time.sleep(5)
#driver.back()

#driver.find_element(By.ID,"LeadSubmitNewHome1").click()

#Thank you page Validation element and attributes
#driver.find_element(By.XPATH,"/html/body/div/div/div/div/a[1]").click()
#driver.find_element(By.CLASS_NAME,"call-toll").click()

#backward move to the page

#Whatsapp button check (Optional Method)
##driver.find_element(By.XPATH,"/html/body/div/div/div/div/a[2]/span").click()




#DropDown = Select(driver.find_element(By.ID,""))

#time.sleep(5)
#Consultation1 = driver.find_element(By.CLASS_NAME,"btn-round-primary")
#driver.execute_script("arguments[0].scrollIntoView();",Consultation1)

#driver.find_element(By.CSS_SELECTOR,"input[id='contactnum1']").send_keys("9438857617")
#driver.find_element(By.XPATH,"//*[@id='LeadSubmit1']")


#Delhi=driver.find_element(By.CSS_SELECTOR,"input[text=' Delhi - NCR']")

#time.sleep(5)
#driver.find_element(By.CLASS_NAME,"btn-round-primary").click()
#driver.close()
#New Tab Open up Hexahealth.com
