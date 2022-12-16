# Necessary webdrivers ned to be imported
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)
# Get the instance of the webBrowser
# window, here we are using Chrome
#webBrowser = webdriver.Chrome()

# Lets open google.com in the first tab
driver.get('https://www.hexahealth.com')

# Lets open https://www.bing.com/ in the second tab
driver.execute_script("window.open('about:blank','secondtab');")
driver.switch_to.window("secondtab")
driver.get('https://www.hexahealth.com/marketing/lasik-bangalore')

# Lets open https://www.facebook.com/ in the third tab
driver.execute_script("window.open('about:blank','thirdtab');")
driver.switch_to.window("thirdtab")
driver.get('https://www.hexahealth.com/campaigns/liver-transplant')



