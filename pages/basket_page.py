from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        """Проверка, что корзина полностью пуста (объединяет две проверки)"""
        self.should_not_be_items_in_basket()
        self.should_be_empty_basket_message()
    
    def should_not_be_items_in_basket(self):
        """
        Отрицательная проверка: товаров в корзине НЕТ.
        Используем метод is_not_element_present для проверки отсутствия элементов.
        """
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "В корзине есть товары, но должна быть пуста"
    
    def should_be_empty_basket_message(self):
        """Проверка, что есть сообщение о пустой корзине"""
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Нет сообщения о пустой корзине"