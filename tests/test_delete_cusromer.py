import allure
import pytest
import math


@allure.feature("Удаление клиентов")
@allure.story("Удаление по средней длине имени")
class TestSmartDeletion:

    @pytest.mark.smoke
    @allure.title("Удаление клиента по средней длине имени")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_by_average_name_length(self, customers_page):
        """
        Тест удаления клиента с длиной имени ближайшей к средней
        """
        # 1. Получить имена клиентов
        names = customers_page.get_all_first_names()

        if len(names) < 2:
            pytest.skip("Недостаточно клиентов для анализа")

        print(f"📊 Клиентов: {len(names)}")
        print(f"📝 Имена: {names}")

        # 2. Вычислить среднюю длину
        name_lengths = [len(name) for name in names]
        average_length = sum(name_lengths) / len(name_lengths)

        print(f"📏 Длины: {name_lengths}")
        print(f"🧮 Средняя длина: {average_length:.2f}")

        # 3. Найти имя с длиной ближайшей к средней
        target_name = min(names, key=lambda name: abs(len(name) - average_length))
        target_length = len(target_name)

        print(f"🎯 Удаляем: '{target_name}' (длина: {target_length}, средняя: {average_length:.2f})")

        # 4. Удалить клиента
        deletion_result = customers_page.delete_customer_by_average_length()

        if deletion_result and deletion_result['deleted_customer']:
            print(f"✅ Успешно удален: {target_name}")
            assert deletion_result['deleted_customer'] == target_name
        else:
            pytest.fail(f"Не удалось удалить {target_name}")

        print("🎉 Тест завершен!")