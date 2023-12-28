from behave import given, when, then
from time import sleep


@given('Open signin page')
def open_page(context):
    context.app.signin_page.open_url('https://soft.reelly.io/sign-in')
    # sleep(10)


@when('Login to the page with {email} and {password}')
def sign_in(context, email, password):
    context.app.signin_page.click_and_sign_in(email, password)
    # sleep(5)
