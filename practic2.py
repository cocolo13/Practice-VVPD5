"""Практическая работа №2 по основам программирования
1 семестр - Списки, словари."""

import random


def view_matrix(matrix):
    """Функция для вывода матрицы(двумерного списка)
    на экран
    Args:
        matrix - матрица в виде двумерного списка

    Returns: None

    Raises:
        IndexError

    Examples:
        >>>view_matrix([[1,2,3], [0,0,0],[4,5,6]])
        1 2 3
        0 0 0
        4 5 6
        >>>view_matrix()
        Traceback (most recent call last):
        ...
        IndexError
        """
    for element in matrix:
        print(*element)


def search_index(key, array):
    """ Функция для нахождения индекса числа в двумерном массиве.
    Находит индекс ближайшего по модулю числа к заданному.
    Args:
        key - заданное число
        array - массив, в котором происходит поиск
    Returns:
        (index1, index2) - картеж из индексов элемента
    Raises:
        ValueError
    Examples:
        >>>search_index(10, [[1,2,3], [99,5,9], [0,67,8]])
        (1,2)
        >>>search_index(10, [])
        Traceback (most recent call last):
        ...
        ValueError
        """
    index1, index2 = 0, 0
    for ind1, elem in enumerate(array):
        for ind2, inside in enumerate(elem):
            if inside == key:
                index1, index2 = ind1, ind2
    return index1, index2


def search_max_near_number(key, array):
    """Функция для нахождения максимально близкого
        по модулю числа к заданному числу в двумерном массиве.
    Args:
        key - заданное число
        array - массив чисел, в котором происходит поиск.
    Returns:
        result - максимально близкое по модулю число в массиве
        array к исходному числу key
    Raises:
        ValueError
    Examples:
        >>>search_max_near_number(10, [[1,2,3],[11,20,30]])
        11
        >>>search_max_near_number(10, [])
        Traceback (most recent call last):
        ...
        ValueError
    """
    nums = []
    length = len(array)
    for i in range(length):
        for j in range(length):
            nums.append([abs(key - array[i][j]), array[i][j]])
    result = min(nums)[1]
    return result


def print_info(value, matrix):
    """Функция для вывода информации пользователю.
    Выводит ближайшее по модулю число к заданному,
    индекс ближайшего по модулю числа в массиве,
    разницу заданного и найденного чисел
    Args:
        value - заданное пользователем число
        matrix - двумерный массив, в котором происходит поиск
    Returns:
        Строка с соответствующей информацией
    Examples:
        >>>input_info(10, [[1,2,3], [34,56,90,99]])
        Самое близкое число к вашему: 2
        Индекс: (0, 1)
        Разница чисел равна: 8
    """
    return (f"Самое близкое число к вашему:"
            f" {search_max_near_number(value, matrix)}\n"
            f"Индекс:"
            f" {search_index(search_max_near_number(value, matrix), matrix)}\n"
            f"Разница чисел равна:"
            f" {abs(value - search_max_near_number(value, matrix))}")


while True:
    command = input("Если хотите запустить программу, нажмите Enter."
                    "Для завершения программы введите 'finish': ")
    if command == "finish":
        break
    try:
        n = int(input("Введите число n - размер матрицы: "))
        assert n >= 1
        m = [[random.randint(0, 100) for j in range(n)] for i in range(n)]
        print("Матрица до транспонирования")
        view_matrix(m)
        print()
        m_transport = list(zip(*m))
        print("Матрица после транспонирования")
        view_matrix(m_transport)
        min_row, max_row, min_col, max_col = \
            10 ** 5, -10 ** 5, 10 ** 5, -10 ** 5
        for i in range(n):
            minimum = min(m_transport[i])
            min_row = min(minimum, min_row)
            maximum = max(m_transport[i])
            max_row = max(maximum, max_row)
        d = {"min_row": min_row, "max_row": max_row}
        print("Характеристика матрицы:")
        for k, v in d.items():
            print(f"{k}: {v}")
        number = int(input("Введите число, которое хотите найти в матрице "))
        print(input_info(number, m_transport))
    except (ValueError, AssertionError, IndexError):
        print("Вы ввели некорректное значение")
