def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input("Введите число. Для выхода из цикла нажмите A: ").split()
        res = 0
        for el in range(len(number)):
            if number[el] == "a" or number[el] == "A":
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f"Сумма чисел: {sum_res}")


my_sum()