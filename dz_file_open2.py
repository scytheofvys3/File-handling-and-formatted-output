def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    strings_positions = {}
    x = 0
    for i in strings:
        t1 = file.tell()
        file.write(f'{i}\n')
        strings_positions.update({(x,t1):i})
        x += 1
    file.close()
    return strings_positions
    # file = open(file_name, 'r', encoding='utf-8')
    # pprint(file.read())


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)