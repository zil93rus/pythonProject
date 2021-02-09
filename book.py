import random

# boobles = [ 10,  25,  94,  12,  94,  65,  32,  94,  78,  65]
# cost =    [.21, .65, .11, .12, .12, .32, .61, .14, .35, .25]
# max = 0
# maxls = []
# money = 100
# index = 0
# for i in range(len(boobles)):
#     if boobles[i] > max:
#         max = boobles[i]
# print(f'Максимальное число {max}')
#
# # for i in range(len(boobles)):
# #     if max == boobles[i]:
# #         maxls.append(boobles[i])
# # print(maxls)
#
# for i in range(len(boobles)):
#     if max == boobles[i] and money > cost[i]:
#         maxls.append(boobles[i])
#         index = i
#         money = cost[i]
# print(f'{cost[index]}')

# smoothies = ['кокосовый', 'клубничный', 'банановый', 'тропический', 'ягодный']
# has_coconut = [True, False, False, True, False]
# lenght = len(smoothies)
# for i in range(lenght):
#     if has_coconut[i]:
#         print(f'{smoothies[i]} содержит кокос')

# def dog_func(dog_name, dog_weight):
#     if dog_weight > 20:
#         print(f'{dog_name} говорит ГАВ-ГАВ')
#     else:
#         print(f'{dog_name} говорит гав-гав')
#
# dog_func('Tuzik', 20, 0)
# dog_func('Puzik', 41)

ls = [6, 2, 5, 3, 9]

# def booble_sort(list, list2):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(0, len(list)-1):
#             if list[i] < list[i+1]:
#                 temp = list[i]
#                 list[i] = list[i+1]
#                 list[i+1] = temp
#                 temp = list2[i]
#                 list2[i] = list2[i+1]
#                 list2[i+1] = temp
#                 swapped = True
#     return
#
# number_of_list_1 = len(ls)
# number = list(range(number_of_list_1))
# sorted_ls = booble_sort(ls, number)
#
# for i in range(len(ls)):
#     print(f'{i+1}. Пузырьковый раствоп №{number[i]+1} - результат {ls[i]}')


# for word in ['як', 'кот', 'пума', 'ягуар', 'собака']:
#     for i in range(2, 7):
#         letters = len(word)
#         if (letters % i) == 0:
#             print(i, word)

# characters = 'amanaplanac'
#
# output = ''
# lenght = len(characters)
# i = 0
# while i < lenght:
#     output += characters[i]
#     i += 1
# lenght *= -1
# i = -2
#
# while i >= lenght:
#     output += characters[i]
#     i -= 1
#
# print(output)

