def div():
    try:
        number_1 = float(input("Укажите знаминатель:"))
        number_2 = float(input("Укажите делитель:"))
        res = number_1 / number_2
    except ZeroDivisionError:
        return "Ошибка! На ноль делить нельзя"
    return res
print(f'result  {div()}')