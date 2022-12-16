from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)



# Create a list of URLs
urls = [
    "https://www.example.com/1",
    "https://www.example.com/2",
    "https://www.example.com/3",
    "https://www.example.com/4",
    "https://www.example.com/5"
]

# Create a new Chrome web browser instance
driver = webdriver.Chrome()

# Open the first URL in a new tab
driver.get(urls[0])
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.SHIFT + Keys.RETURN)

# Open the second URL in a new tab
driver.get(urls[1])
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.SHIFT + Keys.RETURN)

# Switch to the first tab
driver.switch_to.window(driver.window_handles[0])

# Perform actions on the first tab

