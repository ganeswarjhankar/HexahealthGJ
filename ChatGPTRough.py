# Necessary webdrivers ned to be imported
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)

from selenium import webdriver

# List of URLs to open
urls = ['https://www.example.com/page1', 'https://www.example.com/page2', 'https://www.example.com/page3']


# Start a web browser
# driver = webdriver.Firefox()

# Loop through the list of URLs


def run_test_script(driver):
    Element1 = driver.find_element(By.XPATH, "/html/body/div/h1")
    Element1.click()



for url in urls:
    # Open the URL
    driver.get(url)
    # Run the test script for this URL
    run_test_script(driver)


    # Perform any desired actions on the page
    # ...

# Close the web browser
driver.quit()
