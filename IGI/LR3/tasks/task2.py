"""
Выполнил Малиновский Илья, группа 353502
Вариант 19
Задание 2
Нахождения произведения последних цифр чисел
11.02.2025
"""


def input_data():
    """
    Считывает целые числа, пока не введётся 0.
    Возвращает список чисел.
    """
    nums = []
    while True:
        try:
            x = int(input("Введите целое число "
                          "(если хотите завершить ввод, введите 0):\n"))
            if x == 0:
                break
            nums.append(x)
        except ValueError:
            print("Ошибка ввода!")
    return nums


def get_mul_last_digits(nums):
    """
    Получает список целых чисел и возвращает
    произведение их последних цифр
    """
    result = 1
    for num in nums:
        result *= num % 10
    return result


def task_2():
    nums = input_data()
    mul = get_mul_last_digits(nums)
    print(mul)
