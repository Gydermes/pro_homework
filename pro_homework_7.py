# Exercises 1
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
for item in x:
    print(item)

print('****************')
# Exercises 2


def test():
    yield from range(5)


for i in test():
    print(i)

# Exercises 4
a = [x**3 for x in range(1, 10)]
print(a)