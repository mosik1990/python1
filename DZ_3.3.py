def my_func(arg_1 , arg_2, arg_3):
    if arg_1 >= arg_3 and arg_2 >= arg_3:
        return arg_1 + arg_2
    elif arg_1 > arg_2 and arg_1 < arg_3:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3
print(f'Сумма двух аргументов:  {my_func(int(input("Первый аргумент ")), int(input("Второй аргумент ")), int(input("Третий аргумент ")))}')

