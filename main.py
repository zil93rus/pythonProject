# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.

var1 = "Hello"
name = input("Введите имя: ")
years = int(input("Сколько Вам лет?:"))
age = 18
a = age - years
if years > age:
    print(f"{var1} {name} доступ разрешен")
else:
    print(f"{var1}, {name}, доступ запрещен. Увидимся через {a} лет/года")

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_sec = int(input("Введите секунды: "))
hours = int(user_sec / 3600)
minutes = int((user_sec - hours * 3600) / 60)
seconds = int(user_sec - hours * 3600 - minutes * 60)
print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}")

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input("Please enter the number: ")
n2 = n * 2
n3 = n * 3
total = int(n) + int(n2) + int(n3)
print(f'Total - {total}')

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Please enter the number: "))
n = str(number)
i = 0
b = 0
while i < len(n):
    a = number % 10
    i += 1
    if a > b:
        b = a
    number //= 10
print(b)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите
# численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

gain = int(input("Введите значение выручки: "))
expense = int(input("Введите значение издержек: "))
if gain > expense:
    total = gain - expense
    print(f'Прибыль — выручка больше издержек, рентабельность выручки {total}')
    worker = int(input("Введите кол-во сотрудников: "))
    total /= worker
    print(f"Прибыль фирмы в расчете на одного сотрудника составляет {round(total,2)}")
else:
    total = gain - expense
    print(f"Убыток — издержки больше выручки: {round(total,2)}")

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
# на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения
# параметров a и b и выводить одно натуральное число — номер дня.
#
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

a = 2
b = 3
i = 0
while a < b:
    print(f"{i + 1}-й день: {round(a,2)}")
    a = a + (a / 100 * 10)
    i += 1
print(f"На {i + 1}-й день спортсмен достиг результата — не менее {b} км")