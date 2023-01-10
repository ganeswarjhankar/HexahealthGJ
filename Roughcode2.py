import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John Smith', 'Jane Doe', 'Bob Johnson'],
        'Age': [35, 28, 45],
        'City': ['New York', 'San Francisco', 'Chicago']}
df = pd.DataFrame(data)

# Create an Excel file from the DataFrame
df.to_excel('data.xlsx', index=False)

"""Automate to click and download the file that has been created as DataFrame"""

from selenium import webdriver

# Start a web driver and navigate to the download page
driver = webdriver.Firefox()
driver.get('http://yourwebsite.com/download/data.xlsx')

# Locate the download link and click it
link = driver.find_element_by_link_text('Download data.xlsx')
link.click()

# Wait for the download to complete
# ...

# Close the browser and webdriver
driver.quit()

"""Wait for the file to download"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "some_id")))
