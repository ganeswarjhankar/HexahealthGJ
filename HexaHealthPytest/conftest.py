import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    S = Service("D:\\chromedriver.exe")
    driver = webdriver.Chrome(service=S)
    URL = driver.get("https://www.hexahealth.com/")
    driver.maximize_window()
    """Connecting with the local driver with the test_hexahealth Class (cls) Driver"""
    request.cls.driver = driver
    yield
    driver.close()








