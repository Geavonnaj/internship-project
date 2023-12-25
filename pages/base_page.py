from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Page:
    def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
            self.driver.get(url)

    def click(self, *locator):
            self.driver.find_element(*locator).click()

    def input(self, text, *locator):
            self.driver.find_element(*locator).send_keys(text)

    def find_element(self, *locator):
           return self.driver.find_element(*locator)

    def verify_expected_url(self, expected_url):
            self.wait.until(
                ec.url_contains(expected_url),
                message=f'Expected {expected_url} not in url')

    def lens(self, *locator):
          number_of_elements = self.driver.find_elements(*locator)
          return len(number_of_elements)


