"""Реализуйте генераторную функцию, которая будет возвращать по
одному члену геометрической прогрессии с указанным множителем.
Генератор должен остановить свою работу или по достижению указанной
границы, или при передаче команды на завершение
"""


def gen_func(start, stop):
    index = start
    while index < stop:
        yield index
        index += 1


x = gen_func(10, 20)
print(x)
