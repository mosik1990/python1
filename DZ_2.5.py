
my_list = [7, 5, 3, 3, 2]
new_number = int(input("Введите новый номер рейтинга: "))
i = 0
for n in my_list:
    if n > new_number:
        i += 1
my_list.insert(i, new_number)
print(f"{my_list}")
