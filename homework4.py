# Домашнее задание 4
# Корреляция - статистическая мера, используемая для оценки связи между двумя случайными величинами.
# Ваша задача

# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами). 
# Можете использовать любую парадигму, но рекомендую использовать функциональную, 
# т.к. в этом примере она значительно упростит вам жизнь.

import math

def pearson_correlation(arr1, arr2):

    # Проверка на то, что массивы одинаковой длины
    if len(arr1) != len(arr2):
        raise ValueError("Массивы должны быть одинаковой длины")

    n = len(arr1)

    # Расчет среднего значения
    mean_x = sum(arr1) / n
    mean_y = sum(arr2) / n

    variance_x = sum([(xi - mean_x) ** 2 for xi in arr1]) / float(len(arr1))
    variance_y = sum([(yi - mean_y) ** 2 for yi in arr2]) / float(len(arr2))

    covariance = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(arr1,arr2)]) / n 
    correlation = covariance / (math.sqrt(variance_x * variance_y))

    return correlation

array_1 = [1,3,3,7,5,7,7]
array_2 = [6,7,8,9,5,6,7]

correlation = round(pearson_correlation(array_1, array_2),4)
print(f"Корреляция Пирсона: {correlation}")