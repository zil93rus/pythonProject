# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

# def abc():
#     while True:
#         try:
#             a = int(input("a - "))
#             b = int(input("b - "))
#             c = a / b
#             return c
#         except ZeroDivisionError:
#             print("Нельзя делить на ноль")
#             break
# print(abc())

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


# def userdata():
#     dict = {"имя": "", "фамилия": "", "год рождения": "", "город": "", "email": "", "телефон": ""}
#     for i in dict.keys():
#         user_input = input(f"{i.title()} - ")
#         dict[i] = user_input
#     return print(" ".join(dict.values()))
#
# def userdata2(**owner):
#     return print(" ".join(owner.values()))
#
# userdata2(name = "Vladimir",
#           surname = "Zelov",
#           year = "10.11.1985",
#           city = "Moscow",
#           email = "abra@kadab.ra",
#           phone = "9267776369")


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

# def my_func(a, b, c):
#     return print((a + b + c) - min(a, b, c))
#
# my_func(100,2,50)


# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# def my_func1(x, y):
#     return print(x ** y)
#
# def my_func2(x, y):
#     res = 1
#     for i in range(abs(y)):
#         res *= x
#     if y >= 0:
#         return print(res)
#     else:
#         return print(1 / res)
#
#
# my_func1(3, -3)
# my_func2(3, -3)


# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом
# и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа
# вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

# def my_func(*args):
#     ls2 = []
#     while True:
#         if "*" in ls2:
#             print(sum(ls2[:-1]))
#             break
#         user = list(input('Введите числа: ').split(" "))
#         ls = []
#         for i in user:
#             if i == "*":
#                 print("После символа * сумма не считается")
#                 ls.append(i)
#                 break
#             else:
#                 ls.append(int(i))
#         ls2 += ls
#         print(sum(ls2))
#
# my_func()


def sum_func():
    total_sum = 0
    while True:
        sum_list = input("Input any numbers separated by space to sum it. To exit enter 'Q': ").lower()
        sum_list = sum_list.split()

        for i, item in enumerate(sum_list):
            if item == 'Q'.lower():
                while i < len(sum_list):
                    sum_list.pop(i)
                return f"New sum = {sum(sum_list)}. Total sum = {total_sum + sum(sum_list)}."
            else:
                try:
                    sum_list[i] = int(item)
                except ValueError:
                    sum_list.remove(item)
                    sum_list.insert(i, 0)
        print(f" New sum = {sum(sum_list)}. Total sum = {total_sum + sum(sum_list)}.")
        total_sum = total_sum + sum(sum_list)


print(sum_func())

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func():
    pass