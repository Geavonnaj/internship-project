from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from time import sleep

from pages.base_page import Page


class MainPage(Page):
    SECONDARY_BUTTON = (By.CSS_SELECTOR, "a[wized = 'mobileTabGame']")
    #'a[href="/secondary-listings"]')
    MOBILE_SECONDARY = (By.CSS_SELECTOR, '#w-node-e7ffe9f0-8b7e-7431-ac8e-347b28f2a83f-d360c7ea')


    def mobile_testing(self):
        mobile_present = ec.presence_of_element_located(self.MOBILE_SECONDARY)
        self.wait.until(mobile_present).click()
        sleep(5)

    def click_secondary_button(self):
        button_present = ec.presence_of_element_located(self.SECONDARY_BUTTON)
        self.wait.until(button_present).click()




        # self.wait.until(button_present).click()

        # self.click(*self.SECONDARY_BUTTON)

        # self.wait.until(ec.presence_of_element_located(self.SECONDARY_BUTTON)).click()

        # self.click(*self.SECONDARY_BUTTON)


