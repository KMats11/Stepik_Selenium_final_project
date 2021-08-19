from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "NO Login url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'NO Log In form'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'NO Register form'

    def register_new_user(self, email, password):
        # Ваш код, который заполняет обязательные поля
        input1 = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        input3.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
