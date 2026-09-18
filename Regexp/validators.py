"""
Модуль с функциями валидации на основе регулярных выражений.

Содержит:
- is_valid_ipv4 — проверка строки на соответствие IPv4-адресу.
- is_valid_phone — проверка строки на соответствие российскому номеру телефона.
- is_balanced — проверка сбалансированности скобок (дополнительная задача).
"""

import re


def is_valid_ipv4(ip_string: str) -> bool:
    """
    Проверяет, является ли строка корректным IPv4-адресом.

    IPv4-адрес состоит из четырёх чисел (октетов) от 0 до 255,
    разделённых точками. Ведущие нули запрещены.

    Args:
        ip_string: строка для проверки.

    Returns:
        True, если строка является корректным IPv4-адресом, иначе False.

    Examples:
        >>> is_valid_ipv4("192.168.0.1")
        True
        >>> is_valid_ipv4("256.100.50.25")
        False
        >>> is_valid_ipv4("192.168.0")
        False
    """
    # Регулярное выражение для одного октета (0-255 без ведущих нулей)
    octet = r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])'
    pattern = rf'^{octet}\.{octet}\.{octet}\.{octet}$'
    
    return bool(re.fullmatch(pattern, ip_string))


def is_valid_phone(phone: str) -> bool:
    """
    Проверяет, является ли строка корректным российским номером телефона.

    Поддерживаемые форматы:
    - +7XXXXXXXXXX
    - 8XXXXXXXXXX
    - +7 (XXX) XXX-XX-XX
    - 8-XXX-XXX-XX-XX

    Args:
        phone: строка для проверки.

    Returns:
        True, если строка является корректным номером, иначе False.

    Examples:
        >>> is_valid_phone("+79161234567")
        True
        >>> is_valid_phone("8 (916) 123-45-67")
        True
        >>> is_valid_phone("12345")
        False
    """
    # Убираем все разделители для упрощения проверки
    digits_only = re.sub(r'[^\d]', '', phone)
    
    # Проверяем длину (11 цифр для РФ)
    if len(digits_only) != 11:
        return False
    
    # Проверяем, что номер начинается с 7 или 8
    if not re.match(r'^[78]', digits_only):
        return False
    
    return True


def is_balanced(text: str) -> bool:
    """
    Проверяет сбалансированность скобок в строке.

    Учитываются круглые (), квадратные [] и фигурные {} скобки.
    Каждая открывающая скобка должна иметь соответствующую закрывающую,
    и пары должны быть правильно вложены.

    Args:
        text: строка для проверки.

    Returns:
        True, если скобки сбалансированы, иначе False.

    Examples:
        >>> is_balanced("([{}])")
        True
        >>> is_balanced("([)]")
        False
        >>> is_balanced("((()))")
        True
    """
    # Убираем все символы, кроме скобок
    brackets = re.sub(r'[^(){}\[\]]', '', text)
    
    # Стек для проверки вложенности
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in brackets:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != pairs[char]:
                return False
    
    return len(stack) == 0