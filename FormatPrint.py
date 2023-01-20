from selenium import webdriver
from openpyxl import Workbook
from selenium.webdriver.common.by import By


class Scraper:
    def __init__(self):
        # Initialize Selenium webdriver

        from selenium.webdriver.chrome.service import Service
        from selenium import webdriver
        S = Service("D:\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=S)


    def scrape_page(self, url):
        # Navigate to website
        self.driver.get(url)

        # Find element and get its text
        element = self.driver.find_element(By.XPATH,"//input[@id='leadnamehome']")
        #element = self.driver.find_element(By.XPATH,"//div[@id='some-id']")
        text = element.text



        # Print the text
        print(text)

        # Create a list to store print messages
        messages = []
        print(messages)

        # Store print messages in the list
        messages.append(text)

        # Create a new Excel workbook
        wb = Workbook()

        # Select active sheet
        ws = wb.active

        # Write messages to cells
        for row in range(1, len(messages) + 1):
            ws.cell(row=row, column=1, value=messages[row-1])

        # Save the workbook
        wb.save("print_messages.xlsx")

    def close_driver(self):
        # Close Selenium webdriver
        self.driver.quit()

# Usage
scraper = Scraper()
scraper.scrape_page("https://hexahealth.com")
scraper.close_driver()
