"""
Основной модуль для запуска программы «Бухгалтерия».

Импортирует функции из пакета application и демонстрирует их вызов.
Использует сторонний пакет colorama для цветного вывода.
"""

from datetime import datetime

from colorama import Fore, Style, init

from application.salary import calculate_salary
from application.db.people import get_employees

# Инициализация colorama (для корректной работы на Windows)
init(autoreset=True)


def _print_current_date() -> None:
    """Выводит текущую дату и время в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС."""
    now = datetime.now()
    print(
        Fore.CYAN
        + f"Текущая дата и время: {now.strftime('%Y-%m-%d %H:%M:%S')}"
        + Style.RESET_ALL
    )


if __name__ == '__main__':
    _print_current_date()
    calculate_salary()
    get_employees()