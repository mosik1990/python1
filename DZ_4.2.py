my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_new_list = [el for i, el in zip(my_list, my_list[1:]) if el > i]
print(f'Исходный список: {my_list}')
print(f'Новый список: {my_new_list}')