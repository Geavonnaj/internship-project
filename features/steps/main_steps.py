from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on secondary option at the left side menu')
def click_secondary_button(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[href="/secondary-listings"]').click()
    sleep(5)
