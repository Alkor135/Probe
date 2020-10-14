# -*- coding: utf-8 -*-

from pathlib import Path

current_dir = Path.cwd()
home_dir = Path.home()

file_path = Path.home() / 'PycharmProjects' / 'Probe' / 'data_finam'

if file_path.is_dir():
    print(' Папка существует')
else:
    print(' Папки нет')
    file_path.mkdir()

print(current_dir)
print(home_dir)
print(file_path)
