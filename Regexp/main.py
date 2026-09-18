"""
Основной модуль для демонстрации работы функций валидации.

Запускает набор тестовых примеров для каждой функции.
"""

from validators import is_valid_ipv4, is_valid_phone, is_balanced


def _print_result(label: str, value: str, result: bool) -> None:
    """Выводит результат проверки в читаемом формате."""
    status = "✅ OK" if result else "❌ FAIL"
    print(f"{status} | {label:<12} | {value}")


def demo_ipv4() -> None:
    """Демонстрация проверки IPv4-адресов."""
    print("\n=== Проверка IPv4 ===")
    test_cases = [
        ("192.168.0.1", True),
        ("255.255.255.255", True),
        ("0.0.0.0", True),
        ("256.100.50.25", False),
        ("192.168.0", False),
        ("192.168.0.1.1", False),
        ("01.02.03.04", False),
        ("abc.def.ghi.jkl", False),
    ]
    for value, expected in test_cases:
        result = is_valid_ipv4(value)
        _print_result("IPv4", value, result == expected)


def demo_phone() -> None:
    """Демонстрация проверки телефонных номеров."""
    print("\n=== Проверка телефонов ===")
    test_cases = [
        ("+79161234567", True),
        ("89161234567", True),
        ("8 (916) 123-45-67", True),
        ("+7-916-123-45-67", True),
        ("12345", False),
        ("+7916123456", False),
        ("99161234567", False),
        ("+791612345678", False),
    ]
    for value, expected in test_cases:
        result = is_valid_phone(value)
        _print_result("Phone", value, result == expected)


def demo_balanced() -> None:
    """Демонстрация проверки сбалансированности скобок."""
    print("\n=== Проверка сбалансированности скобок ===")
    test_cases = [
        ("([{}])", True),
        ("((()))", True),
        ("([)]", False),
        ("({[", False),
        ("}", False),
        ("", True),
        ("hello (world)", True),
        ("hello (world]", False),
    ]
    for value, expected in test_cases:
        result = is_balanced(value)
        _print_result("Balanced", value, result == expected)


if __name__ == '__main__':
    demo_ipv4()
    demo_phone()
    demo_balanced()