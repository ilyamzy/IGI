"""
Выполнил Малиновский Илья, группа 353502
Вариант 19
Задание 1
Разложение функции в степенной ряд
11.02.2025
"""

import math
import tabulate

def get_input_values():
    """
    Получает значения аргумента x и точности epsilon от пользователя.
    Проверяет их на правильность ввода и возвращает их.
    Если значение аргумента x находится за пределами допустимого интервала (-1 < x < 1),
    функция выводит сообщение об ошибке и требует повторный ввод данных.
    Если значение точности epsilon отрицательное, функция также выводит сообщение об ошибке и требует повторный ввод данных.
    """

    while True:
        try:
            x = float(input("Введите значение аргумента x (-1 <= x <= 1): "))
            if not -1 <= x <= 1:
                print("Недопустимое значение аргумента x")
                continue
            epsilon = float(input("Введите желаемую точность вычислений epsilon: "))
            if epsilon < 0:
                print("Значение должно быть больше нуля")
        except ValueError:
            print("Ошибка ввода")
            continue
        return x, epsilon

def arccos(x, eps):
    """
    Выполняет разложение функции в степенной ряд для заданных значения аргумента x и точности epsilon.
    Функция возвращает значение суммы степенного ряда, а также количество итераций суммы

    Цикл выполяется, пока на каждой итерации прибавляемое значение будет не меньше значения epsilon, либо когда не
    будет достигнуто 500 итераций
    """

    result_value = math.pi / 2
    iter_count = 0
    while iter_count < 500:
        value = (math.factorial(2 * iter_count) / 4 ** iter_count
        / (math.factorial(iter_count) ** 2) / (2 * iter_count + 1) * (x ** (2 * iter_count + 1)))

        if value < eps / 10:
            break
        result_value += value
        iter_count += 1

    return result_value, iter_count

if __name__ == "__main__":
    x, eps = get_input_values()
    value, iter_count = arccos(x, eps)

    data = [[x, iter_count, value, math.acos(x), eps]]
    headers = ["x", "n", "F(x)", "Math F(x)", "eps"]

    print(tabulate.tabulate(data, headers=headers, tablefmt="grid"))