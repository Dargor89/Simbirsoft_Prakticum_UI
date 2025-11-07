import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        """Открыть страницу"""
        with allure.step(f"Открытие страницы: {url}"):
            self.driver.get(url)

    def find_element(self, locator, timeout=None):
        """Найти элемент с ожиданием"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def find_clickable_element(self, locator, timeout=None):
        """Найти кликабельный элемент"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        """Кликнуть по элементу"""
        with allure.step(f"Клик по элементу: {locator}"):
            element = self.find_clickable_element(locator)
            element.click()

    def fill_field(self, locator, text):
        """Заполнить поле текстом"""
        with allure.step(f"Заполнение поля {locator}: {text}"):
            element = self.find_clickable_element(locator)
            element.clear()
            element.send_keys(text)

    def get_alert_text(self):
        """Получить текст алерта"""
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text
        except TimeoutException:
            return None

    def take_screenshot(self, name="screenshot"):
        """Сделать скриншот"""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )