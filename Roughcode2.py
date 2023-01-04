#####Random doctor display############
from selenium.webdriver.chrome.service import Service


from selenium import webdriver
from selenium.webdriver.common.by import By

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)
driver.maximize_window()
url = driver.get("https://www.hexahealth.com/marketing/doctor/laser-fissure-bangalore")

Doctors = driver.find_elements(By.XPATH,"//div[@class='item card-block']/div")
BookFreeAppointmentButtons = driver.find_elements(By.XPATH,"//div[@class='item card-block']/div/div/a")
########################################################################################
DoctorsName = driver.find_elements(By.XPATH,"//div[@class='item card-block']/div/div/h3")
count1 = len(Doctors)
#count2 = len(DoctorsName)

#print(count2)
#print(DoctorsName.text)
#############################################to print all the names of the Doctor in the marketing Doctor Page
for perDoctorsName in DoctorsName:
    print(perDoctorsName.text)
######################################################################################

##############select any one doctor name and execute the process############################
#for BookSingleAppointment in Doctors:
#    BookSingleAppointment.find_element(By.XPATH,"div/a").click()













