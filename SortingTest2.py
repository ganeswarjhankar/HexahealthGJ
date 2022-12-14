from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium .webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.support.wait import WebDriverWait

S=Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)
driver.get("https://rahulshettyacademy.com/angularpractice/shop")



#click on column header

#collect all veggie list => BrowserSortveggie list
#Sort this veggie list => new sorted list
#veggieList == newSortedList



driver.find_element(By.XPATH,"//a[contains(@href,'shop')]").click()
