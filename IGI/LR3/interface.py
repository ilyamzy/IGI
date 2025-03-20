"""
Реализует пользовательский интерфейс выбора задания
"""

from tasks.task1 import task_1
from tasks.task2 import task_2
from tasks.task3 import task_3
from tasks.task4 import task_4
from tasks.task5 import task_5

if __name__ == "__main__":
    while True:
        try:
            num = int(input(
                "Выберите номер задания (1..5) или "
                "0, если хотите завершить программу: "
            ))
            match num:
                case 0:
                    break
                case 1:
                    task_1()
                case 2:
                    task_2()
                case 3:
                    task_3()
                case 4:
                    task_4()
                case 5:
                    task_5()
        except ValueError:
            print("Введите целое число от 0 до 5!")
