from behave import given, when, then



@when('Click on secondary option at the left side menu')
def secondary_button_clicked(context):
    context.app.main_page.click_secondary_button()



