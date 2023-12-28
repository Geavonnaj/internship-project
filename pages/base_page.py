from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Page:
    def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 20)

    def open_url(self, url):
            self.driver.get(url)

    def clicks(self, *locator):
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

    def wait_for_element_click(self, *locator):
        self.wait.until(
            ec.element_to_be_clickable(locator),
            message=f'Element by {locator} not clickable'
        ).click()
