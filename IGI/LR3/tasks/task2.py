"""
Выполнил Малиновский Илья, группа 353502
Вариант 19
Задание 2
Разложение функции в степенной ряд
11.02.2025
"""

def last_digits_product():
    """
    Считывает целые числа, пока не введётся 0, и выводит произведение их последних цифр
    """

    result_product = 1
    while True:
        try:
            x = int(input("Введите целое число (если хотите завершить ввод, введите 0:\n"))

            if x == 0:
                break
            result_product *= abs(x) % 10
        except ValueError:
            print("Ошибка ввода!")

    print(result_product)

if __name__ == "__main__":
    last_digits_product()