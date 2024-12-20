# Домашнее задание по теме "Декораторы"
#
# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
#
# Задание:
# Напишите 2 функции:
#
# 1. Функция, которая складывает 3 числа (sum_three).
# 2. Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и
#    "Составное" в противном случае.

# Пример:
#
# result = sum_three(2, 3, 6)
# print(result)
#
# Результат консоли:
#
# Простое
# 11
#
# Примечания:
#
# Не забудьте написать внутреннюю функцию wrapper в is_prime
# Функция is_prime должна возвращать wrapper
# @is_prime - декоратор для функции sum_three
#

def is_prime(func):
    def wrapper(*args):
        number = func(*args)

        _is_prime = True
        if number < 2:
            _is_prime = False
        else:
            for j in range(2, (number // 2) + 1):
                if number % j == 0:
                    _is_prime = False

        if _is_prime:
            print('Простое')
        else:
            print('Составное')

        return number

    return wrapper


@is_prime
def sum_three(num1, num2, num3):
    return num1 + num2 + num3


result = sum_three(2, 3, 6)
print(result)
