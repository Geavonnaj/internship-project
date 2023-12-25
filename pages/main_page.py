from selenium.webdriver.common.by import By


from pages.base_page import Page
from time import sleep


class MainPage(Page):
    SECONDARY_BUTTON = (By.CSS_SELECTOR, 'a[href="/secondary-listings"]')

    def click_secondary_button(self):
        self.click(*self.SECONDARY_BUTTON)
        sleep(5)
