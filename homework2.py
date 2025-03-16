# Домашнее задание 2. Таблица умножения
# На вход подается число n.
# Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.

LOWER_LIMIT = 1
UPPER_LIMIT = 10


for s_num in range(LOWER_LIMIT, UPPER_LIMIT):
    for f_num in range(LOWER_LIMIT, UPPER_LIMIT):
        print(f"{f_num:>2} *{s_num:>2} ={f_num*s_num:>2}")
    print()

