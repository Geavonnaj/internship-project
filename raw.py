from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys



@given('Open main page')
def open_signin_page(context):
    context.driver.get('https://soft.reelly.io/sign-in')
    sleep(10)


@when('Login to the page with {email} and {password}')
def click_and_sign_in(context, email, password):
    email_field = context.driver.find_element(By.ID, 'email-2')
    password_field = context.driver.find_element(By.CSS_SELECTOR, "[wized='passwordInput']")
    continue_button = context.driver.find_element(By.CSS_SELECTOR, '.login-button')

    email_field.click()
    email_field.send_keys(email)
    password_field.click()
    password_field.send_keys(password)
    continue_button.click()
    sleep(5)


@when('Click on secondary option at the left side menu')
def click_secondary_button(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[href="/secondary-listings"]').click()
    sleep(5)


@when('Verify {text} is in {url} and page opens')
def verify_url(context, text, url):
    assert text in url
    f'Expected {text} not in {url}'


@when('Filter the products by "want to sell"')
def click_button_filter(context):
    filter_button = context.driver.find_element(By.CSS_SELECTOR, '[class="filter-button"]')
    want_to_sell_button = context.driver.find_element(By.CSS_SELECTOR, '[wized="ListingTypeSell"]')
    apply_filter_button = context.driver.find_element(By.CSS_SELECTOR, '[wized="applyFilterButtonMLS"]')

    filter_button.click()
    want_to_sell_button.click()
    apply_filter_button.click()
    sleep(5)


@then('Verify all cards have "for sale" tag')
def verify_cards_tag(context):
    for_sale_tag = context.driver.find_elements(By.CSS_SELECTOR, '[wized="saleTagMLS"]')
    cards = context.driver.find_elements(By.CSS_SELECTOR, '[wized="listingCardMLS"]')
    next_page = context.driver.find_element(By.CSS_SELECTOR, 'img[src*="_Icon.svg"]')
    the_page_number = context.driver.find_element(By.CSS_SELECTOR, '[wized="currentPageProperties"][w-el-text*="1"]')
    page_count = 0

    for tags in for_sale_tag:
        page_count += 1
        count_for_sale_tags = len(for_sale_tag)
        count_for_card = len(cards)
        click_next = next_page
        assert count_for_sale_tags == count_for_card
        assert int(the_page_number.text) == page_count
        print(f'Page {the_page_number.text}, The number of for sale tag {count_for_sale_tags} matches the number of cards {count_for_card}')
        context.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        sleep(5)
        click_next.click()
        sleep(5)
