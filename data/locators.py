from selenium.webdriver.common.by import By


class ManagerPageLocators:
    """Локаторы главной страницы менеджера"""
    ADD_CUSTOMER_BTN = (By.CSS_SELECTOR, "button[ng-click='addCust()']")
    CUSTOMERS_BTN = (By.CSS_SELECTOR, "button[ng-click='showCust()']")


class AddCustomerPageLocators:
    """Локаторы страницы добавления клиента"""
    FIRST_NAME = (By.CSS_SELECTOR, "input[ng-model='fName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[ng-model='lName']")
    POST_CODE = (By.CSS_SELECTOR, "input[ng-model='postCd']")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[type='submit']")


class CustomersPageLocators:
    """Локаторы страницы списка клиентов"""
    FIRST_NAME_HEADER = (By.CSS_SELECTOR, "a[ng-click*=\"fName\"]")
    CUSTOMER_TABLE = (By.CSS_SELECTOR, "table.table")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[ng-click*='deleteCust']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[ng-model='searchCustomer']")