import os
import time

directory = '.'
for root, dirs, files in os.walk(directory): # что такое directory # также расписать синтаксис os.walk()
    # print(root) # расписать что такое root
    # print(dirs) # расписать что такое dirs
    # print(files) # расписать что такое files
    for file in files:
        filepath = os.path.join(root,file) # расписать
        # print(filepath)
        filetime = os.path.getmtime(file) # расписать
        formatted_time = time.strftime("%d.%m.%Y.%H:%M",time.localtime(filetime))
        # print(formatted_time)
        filesize = os.path.getsize(file) # расписать
        # print(filesize)
        parent_dir = os.path.dirname(filepath) # расписать
        # print(parent_dir)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')


