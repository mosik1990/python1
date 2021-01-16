import codecs
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('file_4.txt', 'r') as file_1:
    content = file_1.read().splitlines()
    for i in content:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + ' ' + i[1])
    print(new_file)

with codecs.open('file_4_rus.txt', 'w', 'utf-8') as file_2:
    file_2.writelines('\n'.join(new_file))