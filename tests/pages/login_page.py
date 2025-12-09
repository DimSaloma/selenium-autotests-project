import time  # для генерации email
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.browser.current_url, "Login url is not correct"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
    
    def register_new_user(self, email, password):
        """Регистрация нового пользователя"""
        # Заполняем поле email
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        
        # Заполняем поле пароля
        password_field1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        password_field1.send_keys(password)
        
        # Подтверждаем пароль
        password_field2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        password_field2.send_keys(password)
        
        # Нажимаем кнопку регистрации
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        register_button.click()