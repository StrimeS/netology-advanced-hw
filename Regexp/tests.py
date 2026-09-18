"""
Модуль с unit-тестами для функций валидации.

Использует стандартный модуль unittest.
"""

import unittest

from validators import is_valid_ipv4, is_valid_phone, is_balanced


class TestIPv4(unittest.TestCase):
    """Тесты для функции is_valid_ipv4."""

    def test_valid_addresses(self):
        self.assertTrue(is_valid_ipv4("192.168.0.1"))
        self.assertTrue(is_valid_ipv4("255.255.255.255"))
        self.assertTrue(is_valid_ipv4("0.0.0.0"))
        self.assertTrue(is_valid_ipv4("127.0.0.1"))

    def test_invalid_addresses(self):
        self.assertFalse(is_valid_ipv4("256.100.50.25"))
        self.assertFalse(is_valid_ipv4("192.168.0"))
        self.assertFalse(is_valid_ipv4("192.168.0.1.1"))
        self.assertFalse(is_valid_ipv4("01.02.03.04"))
        self.assertFalse(is_valid_ipv4("abc.def.ghi.jkl"))


class TestPhone(unittest.TestCase):
    """Тесты для функции is_valid_phone."""

    def test_valid_phones(self):
        self.assertTrue(is_valid_phone("+79161234567"))
        self.assertTrue(is_valid_phone("89161234567"))
        self.assertTrue(is_valid_phone("8 (916) 123-45-67"))
        self.assertTrue(is_valid_phone("+7-916-123-45-67"))

    def test_invalid_phones(self):
        self.assertFalse(is_valid_phone("12345"))
        self.assertFalse(is_valid_phone("+7916123456"))
        self.assertFalse(is_valid_phone("99161234567"))


class TestBalanced(unittest.TestCase):
    """Тесты для функции is_balanced."""

    def test_balanced(self):
        self.assertTrue(is_balanced("([{}])"))
        self.assertTrue(is_balanced("((()))"))
        self.assertTrue(is_balanced(""))
        self.assertTrue(is_balanced("hello (world)"))

    def test_unbalanced(self):
        self.assertFalse(is_balanced("([)]"))
        self.assertFalse(is_balanced("({["))
        self.assertFalse(is_balanced("}"))


if __name__ == '__main__':
    unittest.main()