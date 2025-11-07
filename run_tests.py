#!/usr/bin/env python3
"""
Скрипт для запуска тестов
"""

import subprocess
import sys
import os


def run_tests_parallel(workers="auto", headless=False):
    """Запуск тестов в параллельном режиме"""

    cmd = [
        "pytest",
        "-n", workers,
        "--alluredir=allure-results",
        "tests/",
        "-v"
    ]

    if headless:
        cmd.append("--headless")

    print(f"🚀 Запускаем тесты параллельно: {' '.join(cmd)}")

    result = subprocess.run(cmd)
    return result.returncode


def run_tests_sequential(headless=False):
    """Запуск тестов в последовательном режиме"""
    cmd = [
        "pytest",
        "--alluredir=allure-results",
        "tests/",
        "-v"
    ]

    if headless:
        cmd.append("--headless")

    print(f"🔍 Запускаем тесты последовательно: {' '.join(cmd)}")
    return subprocess.run(cmd).returncode


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Запуск тестов")
    parser.add_argument("--workers", "-n", default="auto", help="Количество workers")
    parser.add_argument("--sequential", "-s", action="store_true", help="Последовательный запуск")
    parser.add_argument("--headless", action="store_true", help="Headless режим")

    args = parser.parse_args()

    # Создаем директорию для отчетов
    os.makedirs("allure-results", exist_ok=True)

    if args.sequential:
        return_code = run_tests_sequential(headless=args.headless)
    else:
        return_code = run_tests_parallel(
            workers=args.workers,
            headless=args.headless
        )

    # Генерация Allure отчета
    if return_code == 0:
        print("📈 Генерация Allure отчета...")
        subprocess.run(["allure", "generate", "allure-results", "--clean", "-o", "reports/allure-report"])
        print("📊 Allure отчет: reports/allure-report/index.html")

    sys.exit(return_code)