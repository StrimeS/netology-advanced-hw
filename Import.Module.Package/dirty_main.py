"""
Модуль с «грязным» импортом всех функций через *.

Создан для демонстрации необязательного задания.
"""

from datetime import datetime

from colorama import Fore, Style, init

from application.salary import *
from application.db.people import *

init(autoreset=True)


if __name__ == '__main__':
    now = datetime.now()
    print(
        Fore.CYAN
        + f"Текущая дата и время: {now.strftime('%Y-%m-%d %H:%M:%S')}"
        + Style.RESET_ALL
    )
    calculate_salary()
    get_employees()