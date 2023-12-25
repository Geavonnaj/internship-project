from selenium.webdriver.common.by import By
from pages.base_page import Page

class SigninPage(Page):
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[wized='passwordInput']")
    CONTINUE_BUTTON  = (By.CSS_SELECTOR, '.login-button')

    def open_signin_url(self):
        self.open_url('https://soft.reelly.io/sign-in')

    def click_and_sign_in(self, email, password):
        self.find_element(*self.EMAIL_FIELD).click()
        self.input(email,*self.EMAIL_FIELD)
        self.find_element(*self.PASSWORD_FIELD).click()
        self.input(password, *self.PASSWORD_FIELD)
        self.find_element(*self.CONTINUE_BUTTON).click()



