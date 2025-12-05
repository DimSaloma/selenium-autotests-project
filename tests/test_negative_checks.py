import pytest
from .pages.product_page import ProductPage


@pytest.mark.xfail(reason="Сообщение появляется после добавления товара в корзину")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Тест 1: Проверяем, что нет сообщения после добавления товара."""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()  # Упадет - сообщение есть


def test_guest_cant_see_success_message(browser):
    """Тест 2: Проверяем, что нет сообщения на чистой странице."""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()  # Пройдет - сообщения нет


@pytest.mark.xfail(reason="Сообщение не исчезает автоматически после появления")
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Тест 3: Проверяем, что сообщение исчезает."""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_message()  # Упадет - сообщение не исчезает