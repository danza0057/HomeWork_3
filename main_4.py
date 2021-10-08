def my_func(x, y):
    exp_1 = x ** y
    exp_2 = x
    i = 1
    while i < abs(y):
        exp_2 *= x
        i += 1
    print(exp_1, 1 / exp_2)


x, y = int(input('Введите число: ')), int(input('Введите степень: '))
my_func(x, y)
