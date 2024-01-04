from behave import given, when, then
from time import sleep


@when('Click on mobile testing secondary option')
def click_mobile_testing_secondary_button(context):
    context.app.main_page.mobile_testing()


@when('Click on secondary option at the left side menu')
def secondary_button_clicked(context):
    context.app.main_page.click_secondary_button()


