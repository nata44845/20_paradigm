# Домашнее задание 6. Бинарный поиск
# Предположим, что мы хотим найти элемент в массиве (получить его индекс). 
# Мы можем это сделать просто перебрав все элементы.
# Но что, если массив уже отсортирован? В этом случае можно использовать бинарный поиск. 
# Принцип прост: сначала берём элемент находящийся посередине и сравниваем с тем, который мы хотим найти. 
# Если центральный элемент больше нашего, рассматриваем массив слева от центрального, 
# а если больше - справа и повторяем так до тех пор, пока не найдем наш элемент.
# Задача
# Написать программу на любом языке в любой парадигме для бинарного поиска. 
# На вход подаётся целочисленный массив и число. На выходе - индекс элемента или -1, 
# в случае если искомого элемента нет в массиве.

def binary_search(arr, target, left, right):
    if left > right:  
        return -1
    mid = left + (right - left) // 2 

    if arr[mid] == target: 
        return mid  
    elif arr[mid] < target: 
        return binary_search(arr, target, mid + 1, right)  
    else: 
        return binary_search(arr, target, left, mid - 1)  

arr = [2, 6, 9, 22, 34, 38, 59, 80, 100]
result = binary_search( arr, 7, 0, len(arr) - 1)
if result == -1:
    print("Элемент не найден")
else:
    print(f"Индекс элемента {result}")