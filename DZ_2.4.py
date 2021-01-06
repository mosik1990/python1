
string_words = input("Введите интересную фразу, слова в которой будут разделены через пробел: ")
list = string_words.split()
i = 1
for x in list:
    print(f"{x[0:10]}")
    i += 1

