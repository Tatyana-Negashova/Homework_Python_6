# 1 . Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# day = int(input("Введите номер дня недели от 1 до 7: "))
# check_day = lambda day: "выходной" if day == 6 or day == 7 else "будний день"
# print(check_day(day))

# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# # Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# import math

# factorial = int (input("Введите число: "))
# print([math.factorial(i) for i in range(1,factorial +1)])

# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# n = int(input('Введите число: '))
# print(round(sum([round((1 + 1 / x)**x, 3) for x in range(1, n + 1)]), 3))

# 4.  Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''

numbers_list =[2, 3, 5, 9, 3]
print(sum(numbers_list[item] for item in range(1, len(numbers_list), 2)))