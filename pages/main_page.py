from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from time import sleep

from pages.base_page import Page


class MainPage(Page):
    SECONDARY_BUTTON = (By.CSS_SELECTOR, 'a[href="/secondary-listings"]')

    def click_secondary_button(self):
        button_present = ec.presence_of_element_located(self.SECONDARY_BUTTON)
        self.wait.until(button_present).click()
        sleep(5)


        # self.wait.until(button_present).click()

        # self.click(*self.SECONDARY_BUTTON)

        # self.wait.until(ec.presence_of_element_located(self.SECONDARY_BUTTON)).click()

        # self.click(*self.SECONDARY_BUTTON)


