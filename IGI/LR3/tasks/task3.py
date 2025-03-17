"""
Выполнил Малиновский Илья, группа 353502
Вариант 19
Задание 3
Разложение функции в степенной ряд
11.02.2025
"""

from string import punctuation

def get_count(data):
    spaces_count = data.count(' ')
    digits_count = 0
    punctuation_count = 0
    for symbol in data:
        if symbol.isdigit():
            digits_count += 1
        if symbol in punctuation:
            punctuation_count += 1
    return spaces_count, digits_count, punctuation_count

if __name__ == "__main__":
    input_data = input("Введите строку: ")
    spaces_count, digits_count, punctuation_count = get_count(input_data)
    print(f"Количество пробелов: {spaces_count}")
    print(f"Количество цифр: {digits_count}")
    print(f"Количество знаков пунктуации: {punctuation_count}")
