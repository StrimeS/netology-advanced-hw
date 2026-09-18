"""
Модуль для работы с сотрудниками.

Содержит функцию get_employees.
"""

from colorama import Fore, Style


def get_employees() -> None:
    """Имитирует получение списка сотрудников и выводит сообщение."""
    print(Fore.YELLOW + "Список сотрудников получен." + Style.RESET_ALL)