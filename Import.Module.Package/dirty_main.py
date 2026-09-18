"""
Модуль с «грязным» импортом всех функций через *.

Создан для демонстрации необязательного задания.
"""

from datetime import datetime

from application.salary import *
from application.db.people import *


if __name__ == '__main__':
    now = datetime.now()
    print(f"Текущая дата и время: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    calculate_salary()
    get_employees()