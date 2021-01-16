from sys import argv
script_name, output_in_hours, rate_per_hour, bonus = argv
output_in_hours = float(input("Выработка в часах: "))
rate_per_hour = int(input("Ставка в час: "))
bonus = int(input("Премия: "))
def my_calc():
    return output_in_hours * rate_per_hour + bonus

print('Имя скрипта: ', script_name)
print('Выплата в часах: ', output_in_hours)
print('Ставка в час: ', rate_per_hour)
print('Премия: ', bonus)
print('Заработная плата: ', my_calc())


