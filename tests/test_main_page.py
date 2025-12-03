from .pages.main_page import MainPage
from .pages.login_page import LoginPage   # ← новый импорт

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    
    # Работаем с MainPage
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    
    # Переключаемся на LoginPage (страницу логина)
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()   # ← проверяем что это действительно страница логина  # выполняем метод страницы — переходим на страницу логина