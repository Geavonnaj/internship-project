from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from time import sleep


class SecondaryPage(Page):
    FILTER_BUTTON = (By.CSS_SELECTOR, '[class="filter-button"]')
    WANT_TO_SELL_BUTTON = (By.CSS_SELECTOR, '[wized="ListingTypeSell"]')
    APPLY_FILTER_BUTTON = (By.CSS_SELECTOR, '[wized="applyFilterButtonMLS"]')
    FOR_SALE_TAG = (By.CSS_SELECTOR, '[wized="saleTagMLS"]')
    CARDS = (By.CSS_SELECTOR, '[wized="listingCardMLS"]')

    def verify_url(self, expected_url):
        self.verify_expected_url(expected_url)
        self.driver.implicitly_wait(10)

    def click_button_filter(self):
        button_filter = ec.presence_of_element_located(self.FILTER_BUTTON)
        self.wait.until(button_filter).click()
        button_want_to_sell = ec.presence_of_element_located(self.WANT_TO_SELL_BUTTON)
        self.wait.until(button_want_to_sell).click()
        button_apply = ec.presence_of_element_located(self.APPLY_FILTER_BUTTON)
        self.wait.until(button_apply).click()


        # self.wait.until(ec.presence_of_element_located(self.FILTER_BUTTON)).click()
        # self.wait.until(ec.presence_of_element_located(self.WANT_TO_SELL_BUTTON)).click()
        # self.wait.until(ec.presence_of_element_located(self.APPLY_FILTER_BUTTON)).click()

        # self.click(*self.FILTER_BUTTON)
        # self.click(*self.WANT_TO_SELL_BUTTON)
        # self.click(*self.APPLY_FILTER_BUTTON)

    def verify_cards_tag(self):
        count_for_sale_tag = self.lens(*self.FOR_SALE_TAG)
        count_cards = self.lens(*self.CARDS)
        assert  count_for_sale_tag == count_cards
        print(f'The number of "for sale tag" is {count_for_sale_tag} it matches the "number of cards" {count_cards}')

