import random
import time

from selenium.webdriver.support.wait import WebDriverWait



from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)

# Generate a list of URLs to visit randomly
urls = ['https://www.hexahealth.com', 'https://www.hexahealth.com/marketing/lasik-bangalore',
        'https://www.hexahealth.com/campaigns/liver-transplant']

# Create an instance of the Chrome web driver
#driver = webdriver.Chrome('./chromedriver')

# Select a random URL from the list
url = random.choice(urls)

# Navigate to the selected URL
driver.get(url)
driver.maximize_window()
print(url)



if url == "https://www.hexahealth.com":
        driver.find_element(By.XPATH, "//input[@id='txtArticls']").send_keys("Apollo Hospital")
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Apollo Hospital, Noida")))
        driver.find_element(By.LINK_TEXT,"Apollo Hospital, Noida").click()
        BannerMessage = driver.find_element(By.XPATH,"//h1[@class='banner-title mb-3']") .text
        assert "Apollo Hospital, Noida" in BannerMessage

        #driver.get(url)
        # Lets open https://www.bing.com/ in the second tab
        #driver.execute_script("window.open('about:blank','secondtab');")
        #driver.switch_to.window("secondtab")




elif url == "https://www.hexahealth.com/marketing/lasik-bangalore":
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//*[@id='leadname5']").send_keys("Test Name Marketing Automate")
        driver.find_element(By.XPATH, "//*[@id='contactnum5']").send_keys("1000000876")
        driver.find_element(By.XPATH, "//*[@id='LeadSubmit']").click()
        time.sleep(5)
        driver.back()
        SurgeryCost = driver.find_element(By.XPATH, "//*[@id='surgerytBtn']/span")
        driver.execute_script("arguments[0].click();", SurgeryCost)
        driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("GoodLucktest")
        driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000004312")
        driver.find_element(By.XPATH, "//*[@id='LeadSubmit2']").click()
        time.sleep(5)
        driver.back()
        driver.refresh()
        # Cross = driver.find_element(By.XPATH,"//*[@id='DivCostInsurance']/button")
        # driver.execute_script("arguments[0].click();", Cross)
        # Verify the Check Insurance Coveragpye Link
        Insurance = driver.find_element(By.XPATH, "//*[@id='insurancetBtn']/span/strong")
        driver.execute_script("arguments[0].click();", Insurance)
        driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("Test Insurance check sanity")
        driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000082")
        driver.find_element(By.XPATH, "//*[@id='LeadSubmit2']").click()
        time.sleep(5)
        driver.back()
        driver.refresh()








elif url == "https://www.hexahealth.com/campaigns/liver-transplant":
        pass


else:
        print("sorry better luck next Time")

#driver.close()




