import allure
import pytest


@allure.feature("Управление клиентами")
@allure.story("Добавление нового клиента")
class TestAddCustomer:


    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Добавление клиента со сгенерированными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_customer_with_generated_data(self, add_customer_page):
        """Тест добавления клиента с автоматической генерацией данных"""

        # Добавляем клиента
        customer_data = add_customer_page.add_customer_with_generated_data()

        # Проверяем алерт
        alert_text = add_customer_page.verify_success_alert()

        # Валидация данных
        assert customer_data['first_name'], "First Name не должен быть пустым"
        assert customer_data['last_name'], "Last Name не должен быть пустым"
        assert customer_data['post_code'], "Post Code не должен быть пустым"
        assert len(customer_data['first_name']) == 5, "First Name должен быть из 5 букв"

        print(f"✅ Клиент {customer_data['first_name']} {customer_data['last_name']} успешно добавлен!")

        add_customer_page.fill_customer_form(**test_data)
        add_customer_page.submit_customer_form()
        add_customer_page.verify_success_alert()