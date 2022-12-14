from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium .webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.support.wait import WebDriverWait

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


driver.execute("window.scrollTo(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("Screen.png")

