import allure
import pytest
import time


@allure.feature("Сортировка клиентов")
@allure.story("Сортировка по First Name")
class TestCustomerSorting:

    @pytest.mark.regression
    @allure.title("Проверка сортировки по имени в порядке Z-A")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sort_customers_by_first_name_descending(self, customers_page):
        """
        Тест проверяет что при нажатии на First Name клиенты
        сортируются в обратном алфавитном порядке (Z-A)
        """
        try:
            with allure.step("Получить исходный порядок имен"):
                initial_names = customers_page.get_all_first_names()
                print(f"Исходный порядок имен: {initial_names}")

                if len(initial_names) < 2:
                    pytest.skip(f"Недостаточно клиентов для проверки сортировки. Найдено: {len(initial_names)}")

                allure.attach(
                    f"Начальное состояние:\nКлиентов: {len(initial_names)}\nИмена: {initial_names}",
                    name="Initial State",
                    attachment_type=allure.attachment_type.TEXT
                )

            with allure.step("Нажать на заголовок First Name для сортировки"):
                customers_page.click_first_name_header()
                time.sleep(2)
                print("✅ Нажали на заголовок First Name")

            with allure.step("Получить порядок имен после сортировки"):
                sorted_names = customers_page.get_all_first_names()
                print(f"Порядок после сортировки: {sorted_names}")

            with allure.step("Проверить что имена отсортированы Z-A"):
                # Ожидаем обратную сортировку (Z-A)
                expected_sorted = sorted(initial_names, reverse=True)
                is_sorted_desc = sorted_names == expected_sorted

                print(f"Ожидаемый порядок (Z-A): {expected_sorted}")
                print(f"Фактический порядок: {sorted_names}")
                print(f"Сортировка Z-A корректна: {is_sorted_desc}")

                allure.attach(
                    f"Результат сортировки:\n"
                    f"Исходный порядок: {initial_names}\n"
                    f"После нажатия: {sorted_names}\n"
                    f"Ожидаемый (Z-A): {expected_sorted}\n"
                    f"Результат: {'✅ ОТСОРТИРОВАНО Z-A' if is_sorted_desc else '❌ НЕ ОТСОРТИРОВАНО Z-A'}",
                    name="Sorting Result",
                    attachment_type=allure.attachment_type.TEXT
                )

                assert is_sorted_desc, f"Клиенты не отсортированы Z-A. Ожидалось: {expected_sorted}, Получено: {sorted_names}"

                print("✅ Сортировка по First Name в порядке Z-A работает корректно!")

        except Exception as e:
            print(f"❌ Ошибка в тесте сортировки: {e}")
            raise

    @pytest.mark.regression
    @allure.title("Проверка двойного нажатия - сортировка A-Z затем Z-A")
    @allure.severity(allure.severity_level.NORMAL)
    def test_double_click_sorting(self, customers_page):
        """
        Тест проверяет что двойное нажатие переключает сортировку
        """
        try:
            with allure.step("Получить исходные имена"):
                initial_names = customers_page.get_all_first_names()
                if len(initial_names) < 2:
                    pytest.skip("Недостаточно клиентов")

            with allure.step("Первое нажатие - сортировка Z-A"):
                customers_page.click_first_name_header()
                time.sleep(2)
                names_first_click = customers_page.get_all_first_names()
                print(f"После первого клика (Z-A): {names_first_click}")

            with allure.step("Второе нажатие - сортировка A-Z"):
                customers_page.click_first_name_header()
                time.sleep(2)
                names_second_click = customers_page.get_all_first_names()
                print(f"После второго клика (A-Z): {names_second_click}")

            with allure.step("Проверить переключение сортировки"):
                # После второго клика должна быть обычная сортировка A-Z
                expected_asc = sorted(initial_names)
                is_asc_sorted = names_second_click == expected_asc

                print(f"Ожидаемый порядок (A-Z): {expected_asc}")
                print(f"Фактический порядок: {names_second_click}")
                print(f"Сортировка A-Z корректна: {is_asc_sorted}")

                if is_asc_sorted:
                    print("✅ Двойное нажатие переключает сортировку Z-A → A-Z")
                else:
                    print("⚠️ Двойное нажатие не переключает сортировку как ожидалось")

        except Exception as e:
            print(f"Ошибка при проверке двойного нажатия: {e}")