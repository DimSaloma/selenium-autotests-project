from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_basket(self):
        # Нажимаем кнопку добавления в корзину
        add_button = self.browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        add_button.click()
    
    def should_be_product_name_in_message(self):
        # Получаем название товара
        product_name = self.browser.find_element(By.CSS_SELECTOR, ".product_main h1").text
        # Получаем название из сообщения
        message_name = self.browser.find_element(By.CSS_SELECTOR, ".alert-success strong").text
        assert product_name == message_name, f"Expected {product_name}, got {message_name}"
    
    def should_be_basket_price_equal_product_price(self):
        # Получаем цену товара
        product_price = self.browser.find_element(By.CSS_SELECTOR, ".product_main .price_color").text
        # Получаем цену из сообщения о корзине
        basket_price = self.browser.find_element(By.CSS_SELECTOR, ".alert-info strong").text
        assert product_price == basket_price, f"Expected {product_price}, got {basket_price}"