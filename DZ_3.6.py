def int_func(str):
    return str.capitalize()
str = input("Ввод строки: ")
print(' '.join(map(int_func, str.split())))


"""def func(str):
        return str.title()
print(func("sadasd adasd dsfsdf sdfsdf sdfsdf sdf"))"""