from behave import given, when, then
from time import sleep


@when('Verify {expected_url} is in search result url')
def verify_page(context, expected_url):
    context.app.secondary_page.verify_expected_url(expected_url)


@when('Filter the products by "want to sell"')
def click_button_filter(context):
    context.app.secondary_page.click_button_filter()
    sleep(5)


@then('Verify all cards have "for sale" tag')
def verify_cards_tag(context):
    context.app.secondary_page.verify_cards_tag()


