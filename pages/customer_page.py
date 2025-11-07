import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.locators import CustomersPageLocators


class CustomersPage(BasePage):
    """Страница списка клиентов"""

    @allure.step("Нажать на заголовок First Name для сортировки")
    def click_first_name_header(self):
        """Нажать на заголовок First Name чтобы отсортировать"""
        self.click(CustomersPageLocators.FIRST_NAME_HEADER)
        return self

    @allure.step("Получить все имена из таблицы")
    def get_all_first_names(self):
        """Получить список всех First Name из таблицы"""
        try:
            # Ждем появления таблицы
            self.find_element(CustomersPageLocators.CUSTOMER_TABLE)

            # Находим все ячейки с именами (первая колонка)
            name_elements = self.driver.find_elements(By.CSS_SELECTOR, "table.table tbody tr td:nth-child(1)")
            names = [element.text for element in name_elements if element.text]

            print(f"Найдено имен: {len(names)}")
            return names
        except Exception as e:
            print(f"Ошибка при получении имен: {e}")
            return []

    @allure.step("Удалить клиента по средней длине имени")
    def delete_customer_by_average_length(self):
        """Найти и удалить клиента с длиной имени ближайшей к средней"""
        names = self.get_all_first_names()

        if len(names) < 2:
            print("⚠️ Недостаточно клиентов для удаления по средней длине")
            return None

        # Вычисляем среднюю длину имен
        name_lengths = [len(name) for name in names]
        average_length = sum(name_lengths) / len(name_lengths)

        # Находим имя с длиной ближайшей к средней
        target_name = min(names, key=lambda name: abs(len(name) - average_length))

        print(f"🔍 Поиск клиента для удаления:")
        print(f"   Имена: {names}")
        print(f"   Длины: {name_lengths}")
        print(f"   Средняя длина: {average_length:.2f}")
        print(f"   Целевое имя: '{target_name}' (длина: {len(target_name)})")

        # Удаляем найденного клиента
        success = self._delete_customer_by_name(target_name)

        return {
            'deleted_customer': target_name if success else None,
            'average_length': average_length,
            'all_names': names,
            'deletion_success': success
        }

    def _delete_customer_by_name(self, first_name):
        """Внутренний метод для удаления клиента по имени"""
        try:
            # Находим строку с нужным именем
            rows = self.driver.find_elements(By.CSS_SELECTOR, "table.table tbody tr")

            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                if len(cells) >= 3 and cells[0].text == first_name:
                    # Находим кнопку удаления в этой строке
                    delete_btn = row.find_element(By.CSS_SELECTOR, "button[ng-click*='deleteCust']")
                    delete_btn.click()
                    print(f"✅ Клиент '{first_name}' удален")
                    return True

            print(f"❌ Клиент '{first_name}' не найден в таблице")
            return False

        except Exception as e:
            print(f"❌ Ошибка при удалении клиента '{first_name}': {e}")
            return False

    @allure.step("Найти клиента по имени")
    def find_customer_by_name(self, first_name):
        """Проверить наличие клиента в таблице по имени"""
        names = self.get_all_first_names()
        return first_name in names