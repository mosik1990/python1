
s_list = ['зима', 'весна', 'лето', 'осень']
s_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
number_month = int(input(f"Введите номер месяца: "))
if number_month ==12 or number_month == 1 or number_month == 2:
        print(f"{s_dict.get(1)}")
        print(f"{s_list[0]}")
elif number_month == 3 or number_month == 4 or number_month ==5:
    print(f"{s_dict.get(2)}")
    print(f"{s_list[1]}")
elif number_month == 6 or number_month == 7 or number_month == 8:
    print(f"{s_dict.get(3)}")
    print(f"{s_list[2]}")
elif number_month == 9 or number_month == 10 or number_month == 11:
    print(f"{s_dict.get(4)}")
    print(f"{s_list[3]}")
else:
    print(f"В году 12 месяцев, так что учи времена года!=)")
