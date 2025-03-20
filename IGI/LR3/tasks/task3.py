"""
Выполнил Малиновский Илья, группа 353502
Вариант 19
Задание 3
Подсчёт количества пробелов, цифр, а также знаков пунктуации в строке
11.02.2025
"""

from string import punctuation


def get_space_count(data):
    """Считает количество пробелов в строке"""
    return data.count(' ')


def get_digit_count(data):
    """Считает количество цифр в строке"""
    total_count = 0
    for char in data:
        if char.isdigit():
            total_count += 1
    return total_count


def get_punctation_count(data):
    """Считает количество знаков пунктуации в строке"""
    total_count = 0
    for char in data:
        if char in punctuation:
            total_count += 1
    return total_count


def task_3():
    input_data = input("Введите строку: ")
    space_count = get_space_count(input_data)
    digit_count = get_digit_count(input_data)
    punctuation_count = get_punctation_count(input_data)
    print(f"Количество пробелов: {space_count}")
    print(f"Количество цифр: {digit_count}")
    print(f"Количество знаков пунктуации: {punctuation_count}")
