from selenium.common.exceptions import NoSuchElementException  # ← добавляем импорт

class BasePage():
    def __init__(self, browser, url, timeout=10):  # ← добавляем timeout
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)      # ← неявное ожидание

    def open(self): 
        self.browser.get(self.url)
    
    def is_element_present(self, how, what):       # ← новый метод
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:              # ← перехватываем исключение
            return False
        return True