from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import Page

class SigninPage(Page):
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[wized='passwordInput']")
    CONTINUE_BUTTON  = (By.CSS_SELECTOR, '.login-button')

    def open_signin_url(self):
        webpage_loaded = ec.presence_of_element_located(self.CONTINUE_BUTTON)
        self.wait.until(webpage_loaded)

        self.open_url('https://soft.reelly.io/sign-in')


    def click_and_sign_in(self, email, password):
        self.wait.until(ec.presence_of_element_located(self.EMAIL_FIELD)).click()
        self.input(email,*self.EMAIL_FIELD)
        self.wait.until(ec.presence_of_element_located(self.PASSWORD_FIELD)).click()
        self.input(password, *self.PASSWORD_FIELD)
        self.wait.until(ec.presence_of_element_located(self.CONTINUE_BUTTON)).click()



        # self.input(email,*self.EMAIL_FIELD)
        # self.input(password, *self.PASSWORD_FIELD)
        # self.find_element(*self.CONTINUE_BUTTON).click()



