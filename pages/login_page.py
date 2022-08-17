from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_INPUT = (By.ID, 'user_login_email')
    PASSWORD_INPUT = (By.ID, 'user_login_password')
    CONTINUA_BTN = (By.ID, 'user_login_continue')
    ACTIVEAZA_MAI_TARZIU_BTN = (By.XPATH, '//a[text()="Activează mai târziu"]')
    LOGO_IMG = (By.XPATH, '//img[@alt="eMAG"]')

    def set_email(self, email):
        self.wait_and_fill_elem(*self.EMAIL_INPUT, email)

    def set_password(self, email):
        self.wait_and_fill_elem(*self.PASSWORD_INPUT, email)

    def click_continua_btn(self):
        self.wait_and_click_elem(*self.CONTINUA_BTN)

    def click_activeaza_mai_tarziu_btn(self):
        self.wait_and_click_elem(*self.ACTIVEAZA_MAI_TARZIU_BTN)

    def click_logo_img(self):
        self.wait_and_click_elem(*self.LOGO_IMG)





