from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SecondaryPage(Page):
    FILTER_BUTTON = (By.CSS_SELECTOR, '[class="filter-button"]')
    WANT_TO_SELL_BUTTON = (By.CSS_SELECTOR, '[wized="ListingTypeSell"]')
    APPLY_FILTER_BUTTON = (By.CSS_SELECTOR, '[wized="applyFilterButtonMLS"]')
    FOR_SALE_TAG = (By.CSS_SELECTOR, '[wized="saleTagMLS"]')
    CARDS = (By.CSS_SELECTOR, '[wized="listingCardMLS"]')

    def verify_url(self, expected_url):
        self.verify_expected_url(expected_url)

    def click_button_filter(self):
        self.click(*self.FILTER_BUTTON)
        self.click(*self.WANT_TO_SELL_BUTTON)
        self.click(*self.APPLY_FILTER_BUTTON)
        sleep(5)

    def verify_cards_tag(self):
        count_for_sale_tag = self.lens(*self.FOR_SALE_TAG)
        count_cards = self.lens(*self.CARDS)
        assert  count_for_sale_tag == count_cards
        print(f'The number of "for sale tag" is {count_for_sale_tag} it matches the "number of cards" {count_cards}')


