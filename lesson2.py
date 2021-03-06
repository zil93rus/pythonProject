# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать
# у пользователя, а указать явно, в программе.


# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

"""
ls = []
for i in range(21):
    ls.append(i)
pos = 0
for i in range(int(len(ls) / 2)):
    ls[pos], ls[pos + 1] = ls[pos + 1], ls[pos]
    pos += 2
print(ls)
"""

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

"""
user_month = int(input("Please enter the month: "))
month = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

if user_month in winter:
    print(f"Your month {user_month} is winter")
elif user_month in spring:
    print(f"Your month {user_month} is spring")
elif user_month in summer:
    print(f"Your month {user_month} is summer")
else:
    print(f"Your month {user_month} is autumn")
"""

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

"""
user_input = input("enter a string of multiple words separated by spaces: ")
ls = user_input.split(" ")
for i in ls:
    if len(i) > 10:
        print(f"{i[:10]}")
    else:
        print(i)
"""

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

"""
my_list = [7, 5, 3, 3, 2]
user_int = int(input("Enter the number: "))
if user_int not in my_list:
    for i in my_list:
        if i == user_int - 1:
            my_list.insert(my_list.index(i), user_int)
            break
        elif i < user_int:
            my_list.insert(my_list.index(i), user_int)
            break
        else:
            if my_list[-1] > user_int:
                my_list.append(user_int)
elif user_int in my_list:
    num_pos = my_list.index(user_int)
    num_count = my_list.count(user_int)
    my_list.insert(num_pos + (num_count - 1), user_int)
print(my_list)
"""

"""
my_list = [7, 5, 3, 3, 2]
user_int = int(input("Enter the number: "))
i = 0
for ls in my_list:
    if user_int <= ls:
        i += 1
my_list.insert(i, user_int)
print(my_list)
"""

# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать
# программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

"""
goods = []
features = {"название": " ", "цена": " ", "количество": " ", "eд": " "}
analytics = {"название": [], "цена": [], "количество": [], "eд": []}

count = 0
while True:
    if input("Для продолжения нажмите Enter. Чтобы выйти введите Q: ").upper() == "Q":
        break
    count += 1
    for i in features.keys():
        user_input = input(f"Заполните данные. {i.title()} - ")
        features[i] = user_input
        analytics[i].append(features[i])
    goods.append((count, features))
for i in goods:
    print(i)
for key, value in analytics.items():
    print(f"{key.title()} - {value}")
"""