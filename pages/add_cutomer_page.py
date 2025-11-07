import allure
from pages.base_page import BasePage
from data.locators import AddCustomerPageLocators
from utils.helpers import generate_name_from_post_code, generate_post_code, generate_last_name


class AddCustomerPage(BasePage):
    """Страница добавления клиента"""

    def __init__(self, driver):
        super().__init__(driver)
        self._generate_customer_data()

    def _generate_customer_data(self):
        """Сгенерировать данные клиента"""
        self.post_code = generate_post_code()
        self.first_name = generate_name_from_post_code(self.post_code)
        self.last_name = generate_last_name()

    @allure.step("Показать сгенерированные данные")
    def show_generated_data(self):
        """Показать связь между данными"""
        print(f"\n=== Сгенерированные данные ===")
        print(f"Post Code: {self.post_code}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")

        allure.attach(
            f"Post Code: {self.post_code}\nFirst Name: {self.first_name}\nLast Name: {self.last_name}",
            name="Generated Customer Data",
            attachment_type=allure.attachment_type.TEXT
        )
        return self

    @allure.step("Заполнить форму данными клиента")
    def fill_customer_form(self, first_name=None, last_name=None, post_code=None):
        """Заполнить форму данными клиента"""
        first_name = first_name or self.first_name
        last_name = last_name or self.last_name
        post_code = post_code or self.post_code

        self.fill_field(AddCustomerPageLocators.FIRST_NAME, first_name)
        self.fill_field(AddCustomerPageLocators.LAST_NAME, last_name)
        self.fill_field(AddCustomerPageLocators.POST_CODE, post_code)

        return first_name, last_name, post_code

    @allure.step("Отправить форму добавления клиента")
    def submit_customer_form(self):
        """Отправить форму"""
        self.click(AddCustomerPageLocators.SUBMIT_BTN)

    @allure.step("Добавить клиента со сгенерированными данными")
    def add_customer_with_generated_data(self):
        """Полный процесс добавления клиента"""
        self.show_generated_data()
        first_name, last_name, post_code = self.fill_customer_form()
        self.submit_customer_form()

        return {
            'first_name': first_name,
            'last_name': last_name,
            'post_code': post_code
        }

    @allure.step("Проверить успешное добавление")
    def verify_success_alert(self):
        """Проверить алерт об успешном добавлении"""
        alert_text = self.get_alert_text()
        if alert_text:
            assert "customer" in alert_text.lower() or "success" in alert_text.lower()
            return alert_text
        return None