"""
Домашнее задание к лекции 2. «Iterators. Generators. Yield».

Содержит:
- класс FlatIterator для плоского обхода списка списков;
- функцию-генератор flat_generator;
- улучшенные версии (необязательное задание) для любой вложенности.
"""

import types
from typing import Any, Iterator, List


# ============================================================
# ЗАДАНИЕ 1: Итератор для плоского обхода списка списков
# ============================================================

class FlatIterator:
    """
    Итератор, который принимает список списков и возвращает их плоское
    представление (последовательность вложенных элементов).
    """

    def __init__(self, list_of_list: List[List[Any]]):
        """
        Инициализирует итератор.

        Args:
            list_of_list: список списков для обхода.
        """
        self.list_of_list = list_of_list
        self.outer_index = 0
        self.inner_index = 0

    def __iter__(self) -> 'FlatIterator':
        """Возвращает сам итератор."""
        return self

    def __next__(self) -> Any:
        """
        Возвращает следующий элемент плоской последовательности.

        Raises:
            StopIteration: когда элементы закончились.
        """
        # Пропускаем пустые подсписки
        while self.outer_index < len(self.list_of_list):
            current_sublist = self.list_of_list[self.outer_index]

            if self.inner_index < len(current_sublist):
                item = current_sublist[self.inner_index]
                self.inner_index += 1
                return item

            # Переходим к следующему подсписку
            self.outer_index += 1
            self.inner_index = 0

        raise StopIteration


# ============================================================
# ЗАДАНИЕ 2: Генератор для плоского обхода
# ============================================================

def flat_generator(list_of_lists: List[List[Any]]) -> Iterator[Any]:
    """
    Генератор, который принимает список списков и возвращает их плоское
    представление.

    Args:
        list_of_lists: список списков для обхода.

    Yields:
        Элементы вложенных списков по одному.
    """
    for sublist in list_of_lists:
        for item in sublist:
            yield item


# ============================================================
# ЗАДАНИЕ 3 (необязательное): Итератор для любой вложенности
# ============================================================

class FlatIteratorRecursive:
    """
    Итератор, который обрабатывает списки с любым уровнем вложенности.
    """

    def __init__(self, list_of_list: List[Any]):
        """
        Инициализирует итератор.

        Args:
            list_of_list: список с любой вложенностью.
        """
        self.list_of_list = list_of_list
        self.stack = [iter(list_of_list)]

    def __iter__(self) -> 'FlatIteratorRecursive':
        """Возвращает сам итератор."""
        return self

    def __next__(self) -> Any:
        """
        Возвращает следующий элемент с учётом вложенности.

        Raises:
            StopIteration: когда элементы закончились.
        """
        while self.stack:
            try:
                item = next(self.stack[-1])
            except StopIteration:
                self.stack.pop()
                continue

            if isinstance(item, list):
                self.stack.append(iter(item))
            else:
                return item

        raise StopIteration


# ============================================================
# ЗАДАНИЕ 4 (необязательное): Генератор для любой вложенности
# ============================================================

def flat_generator_recursive(list_of_list: List[Any]) -> Iterator[Any]:
    """
    Генератор, который обрабатывает списки с любым уровнем вложенности.

    Args:
        list_of_list: список с любой вложенностью.

    Yields:
        Элементы вложенных списков по одному.
    """
    for item in list_of_list:
        if isinstance(item, list):
            yield from flat_generator_recursive(item)
        else:
            yield item


# ============================================================
# ТЕСТЫ
# ============================================================

def test_1() -> None:
    """Тест для FlatIterator (задание 1)."""
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_1),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None
    ]
    print("✅ Задание 1: тест пройден.")


def test_2() -> None:
    """Тест для flat_generator (задание 2)."""
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
        flat_generator(list_of_lists_1),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None
    ]
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    print("✅ Задание 2: тест пройден.")


def test_3() -> None:
    """Тест для FlatIteratorRecursive (задание 3, необязательное)."""
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
        FlatIteratorRecursive(list_of_lists_2),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIteratorRecursive(list_of_lists_2)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!'
    ]
    print("✅ Задание 3 (необязательное): тест пройден.")


def test_4() -> None:
    """Тест для flat_generator_recursive (задание 4, необязательное)."""
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
        flat_generator_recursive(list_of_lists_2),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator_recursive(list_of_lists_2)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!'
    ]
    assert isinstance(flat_generator_recursive(list_of_lists_2), types.GeneratorType)
    print("✅ Задание 4 (необязательное): тест пройден.")


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()