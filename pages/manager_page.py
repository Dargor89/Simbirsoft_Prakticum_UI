import allure
from pages.base_page import BasePage
from data.locators import ManagerPageLocators


class ManagerPage(BasePage):
    """Страница менеджера банка"""

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

    @allure.step("Открыть страницу менеджера")
    def open_manager_page(self):
        self.open(self.url)
        return self

    @allure.step("Нажать кнопку 'Add Customer'")
    def click_add_customer(self):
        self.click(ManagerPageLocators.ADD_CUSTOMER_BTN)
        from pages.add_cutomer_page import AddCustomerPage
        return AddCustomerPage(self.driver)

    @allure.step("Нажать кнопку 'Customers'")
    def click_customers(self):
        self.click(ManagerPageLocators.CUSTOMERS_BTN)
        from pages.customer_page import CustomersPage
        return CustomersPage(self.driver)