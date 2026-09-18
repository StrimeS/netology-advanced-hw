"""
Основной модуль для запуска программы «Бухгалтерия».

Импортирует функции из пакета application и демонстрирует их вызов.
"""

from datetime import datetime

from application.salary import calculate_salary
from application.db.people import get_employees


def _print_current_date() -> None:
    """Выводит текущую дату и время в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС."""
    now = datetime.now()
    print(f"Текущая дата и время: {now.strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == '__main__':
    _print_current_date()
    calculate_salary()
    get_employees()