import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


def pytest_addoption(parser):
    """Добавляем опции командной строки"""
    parser.addoption("--headless", action="store_true", default=False, help="Run in headless mode")


@pytest.fixture(scope="function")
def driver(request):
    """Фабрика WebDriver - упрощенная версия"""
    worker_id = getattr(request.config, 'worker_id', 'master')
    print(f"🚀 Запуск браузера для worker: {worker_id}")

    # Получаем опцию headless
    headless = request.config.getoption("--headless")

    # Настройки Chrome
    chrome_options = Options()

    # Базовые настройки
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Headless режим если указан
    if headless:
        chrome_options.add_argument("--headless=new")
        print(f"🔧 Headless режим активирован для worker: {worker_id}")

    try:
        # Простая инициализация драйвера
        driver = webdriver.Chrome(options=chrome_options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        print(f"✅ Браузер Chrome запущен для worker: {worker_id}")

        def fin():
            driver.quit()
            print(f"✅ Браузер закрыт для worker: {worker_id}")

        request.addfinalizer(fin)
        return driver

    except Exception as e:
        print(f"❌ Ошибка инициализации драйвера: {e}")
        raise


@pytest.fixture
def manager_page(driver):
    """Фикстура главной страницы менеджера"""
    from pages.manager_page import ManagerPage
    page = ManagerPage(driver)
    page.open_manager_page()
    return page


@pytest.fixture
def add_customer_page(manager_page):
    """Фикстура страницы добавления клиента"""
    return manager_page.click_add_customer()


@pytest.fixture
def customers_page(manager_page):
    """Фикстура страницы списка клиентов"""
    return manager_page.click_customers()


def pytest_sessionstart(session):
    """Вызывается при старте тестовой сессии"""
    print("🎯 Начало тестовой сессии")
    headless = session.config.getoption("--headless")
    print(f"📊 Режим: {'Headless' if headless else 'GUI'}")


def pytest_sessionfinish(session):
    """Вызывается при завершении тестовой сессии"""
    print("✅ Тестовая сессия завершена")