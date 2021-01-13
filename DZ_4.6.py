from itertools import count

for el in count(int(input('Введите стартовое число: '))):
    print(el)
    quit = input()
    if quit == "q":
        break
while quit != "q":
    print(next(iter), end=" ")
    quit = input()

from itertools import cycle

my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    print(el)