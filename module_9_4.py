# Домашнее задание по теме "Создание функций на лету"
#
# Цель: освоить на практике замыкание, объекты-функторы и lambda-функции.
# Задача "Функциональное разнообразие":
#
# Lambda-функция:
#
# Даны 2 строки:

first = 'Мама мыла раму'
second = 'Рамена мало было'
#
# Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
# Здесь ? - место написания lambda-функции.
#
# Результатом должен быть список совпадения букв в той же позиции:
#
# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
#
# Где True - совпало, False - не совпало.

print(list(map(lambda x, y: x == y, first, second)))

# Замыкание:
#
# Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
# Внутри этой функции, напишите ещё одну - write_everything(*data_set),
# где *data_set - параметр принимающий неограниченное количество данных любого типа.
#
# Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
#
# Функция get_advanced_writer возвращает функцию write_everything.
#
# Данный код:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for data in data_set:
                line = ''
                if isinstance(data, str):
                    line = data
                elif isinstance(data, int | float):
                    line = str(data)
                elif isinstance(data, bool):
                    line = 'True' if data == True else 'False'
                elif isinstance(data, list):
                    line = f'[{", ".join(map(lambda x: "'" + x + "'" if isinstance(x, str) else str(x), data))}]'
                elif isinstance(data, set):
                    line = "{" + ", ".join(map(lambda x: "'" + x + "'" if isinstance(x, str) else str(x), data)) + "}"
                elif isinstance(data, dict):
                    len_dict = len(data)
                    i = 0
                    for key, value in data.items():
                        i += 1
                        if isinstance(key, str):
                            line += "'" + key + "': "
                        else:
                            line += str(key) + ": "
                        if isinstance(value, str):
                            line += "'" + value + ("'" if i == len_dict else "', ")
                        else:
                            line += str(value) + ('' if i == len_dict else ", ")
                    line = "{" + line + "}"

                file.write(line + '\n')
                # file.write(str(data) + '\n') - можно было просто написать str(data) и преобразовать любой тип данных
                # в строку ;)

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#
# Запишет данные в файл в таком виде:
# 'Это строчка'
# ['А', 'это', 'уже', 'число', 5, 'в', 'списке']
#
#
# Метод __call__:
#
# Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
# В этом классе также определите метод __call__ который будет случайным образом выбирать слово из words и
# возвращать его. Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции можете
# использовать функцию choice из модуля random.
#
# Ваш код (количество слов для случайного выбора может быть другое):
#
from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())
print(first_ball())
print(first_ball())

#
# Примерный результат (может отличаться из-за случайности выбора):
#
# Да
# Да
# Наверное
