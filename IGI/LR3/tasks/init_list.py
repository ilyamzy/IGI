"""
Функции для инициализации списка вещественных чисел
"""

import random


def input_list():
    """
    Считывает вещественные числа как строку, проверяет валидность
    введённых вещественных чисел и возвращает список
    """

    while True:
        input_data = input("Введите числа через пробел: ")
        try:
            nums = [float(num) for num in input_data.split()]
            return nums
        except ValueError:
            print("Ошибка ввода! Вводите только вещественные числа!")


def input_list_by_count():
    """
    Считывает количество вводимых чисел, а также сам числа.
    Проверяет валидность введённых данных. Возвращает список.
    """

    nums_count = 0
    while True:
        try:
            nums_count = int(input("Введите количество вводимых чисел: "))
            if nums_count <= 0:
                print("Количество чисел должно быть положительным числом")
                continue
            break
        except ValueError:
            print("Введите целое положительное число!")

    nums = []
    for i in range(nums_count):
        while True:
            try:
                num = float(input(f"Введите {i + 1}-е число: "))
                nums.append(num)
                break
            except ValueError:
                print("Введённое число не является вещественным!")
    return nums


def generate_list(
        count_nums=None,
        min_val=None,
        max_val=None
):
    if count_nums is None:
        count_nums = random.randint(100, 1000)
    if min_val is None:
        min_val = random.uniform(-1000, 1000)
    if max_val is None:
        max_val = min_val + random.uniform(10, 1000)

    return [random.uniform(min_val, max_val) for _ in range(count_nums)]


def choose_init_method(func):
    def wrapper():
        print("""
        Выберите способ инициализации листа вещественных чисел:
        1) Ввод чисел через пробел
        2) Ввод количества чисел, а затем и самих чисел
        3) Сгенерировать
        """)
        while True:
            try:
                choose_var = int(input(
                    "Введите номер соответствующего способа: "
                ))
                if choose_var not in [1, 2, 3]:
                    print("Введите одно число: 1, 2 или 3!")
                    continue
                nums = []
                match choose_var:
                    case 1:
                        nums = input_list()
                    case 2:
                        nums = input_list_by_count()
                    case 3:
                        nums = generate_list()
                return func(nums)
            except ValueError:
                print("Введите одно число: 1, 2 или 3!")
    return wrapper
