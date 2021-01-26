class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input("Введите значения и нажимайте Enter: "))
                self.my_list.append(val)
                print(f"Текущий список - {self.my_list} \n ")
            except:
                print(f"Неверное значение. Введите число. Для выхода введите букву")
                Stop = input(f"Вы уверены что хотите выйти? Если да то пиши буковки ")

                if Stop == "Stop" or Stop == "stop":
                    print(try_except.my_input())
                elif Stop == "Stop" or Stop == "stop":
                    return f"Вы вышли"
                else:
                    return f"Вы вышли"

try_except = Error(1)
print(try_except.my_input())