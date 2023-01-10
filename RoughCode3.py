"""Class , Method  all in one window for example"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class FormFiller:
    def __init__(self):
        self.browser = webdriver.Firefox()

    def fill_form(self, url, form_data):
        self.browser.get(url)
        for field, value in form_data.items():
            elem = self.browser.find_element_by_name(field)
            elem.clear()
            elem.send_keys(value)

    def submit(self):
        elem = self.browser.find_element_by_xpath("//input[@type='submit']")
        elem.send_keys(Keys.RETURN)

    def close_browser(self):
        self.browser.quit()


# Usage example:
form_filler = FormFiller()
form_data = {'name': 'John Doe', 'email': 'johndoe@example.com'}
form_filler.fill_form("http://example.com/form", form_data)
form_filler.submit()
form_filler.close_browser()
