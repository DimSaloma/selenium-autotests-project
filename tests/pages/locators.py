from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    # URL проверка
    LOGIN_URL = "login"
    
    # Форма логина
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "[name='login_submit']")
    
    # Форма регистрации
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    """Локаторы для страницы товара."""
    
    # Кнопка добавления в корзину
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    
    # Название товара на странице
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    
    # Цена товара на странице
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    
    # Сообщение об успешном добавлении в корзину
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    
    # Название товара в сообщении об успехе
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success strong")
    
    # Цена товара в сообщении о корзине
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    
    # Или альтернативные локаторы, если вышеуказанные не работают:
    # ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    # PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    # PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
    # SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alert-success strong")
    # BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, "div.alert-info strong")