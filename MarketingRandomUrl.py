import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# Generate a list of URLs to visit randomly
urls = ['https://www.hexahealth.com/', 'https://www.hexahealth.com/campaigns/liver-transplant', 'https://www.hexahealth.com/marketing/lasik-bangalore']


# Create an instance of the Chrome web driver
S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)

#driver = webdriver.Chrome('./chromedriver')
# Iterate over the list of URLs and visit them randomly
for url in urls:
    # Select a random URL from the list
    url = random.choice(urls)

    print(url)
    # Navigate to the selected URL
    driver.get(url)

#driver.close()
