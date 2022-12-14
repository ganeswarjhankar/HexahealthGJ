from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.action_chains import ActionChains
import time

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)


URL=driver.get("https://www.")