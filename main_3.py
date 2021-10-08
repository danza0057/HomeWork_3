def my_func(digit1, digit2, digit3):
    my_list = [digit1, digit2, digit3]
    min_digit = min(my_list)
    my_list.remove(min_digit)
    my_sum = sum(my_list)
    print(my_sum)


a, b, c = int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(
    input('Введите третье число: '))
my_func(a, b, c)
