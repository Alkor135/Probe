# -*- coding: utf-8 -*-

from pathlib import Path

# print(Path.cwd())
# print(Path.home())
#
# file_path = Path.home() / 'PycharmProjects' / 'Probe' / 'data_finam'
#
# if file_path.is_dir():
#     print(f'Папка существует {file_path}')
# else:
#     print(f'Папки нет {file_path}')
#     file_path.mkdir()
#
# print(file_path)
#
# print(Path('settings.py').stat().st_size)
#
# print(sorted(Path('.').glob('*.py')))
#
#
# p = Path('.')
# file_lst = [x for x in p.iterdir() if x.is_file()]
# print(file_lst)
#
# p = Path.home() / 'PycharmProjects' / 'Probe'
# file_lst = [x for x in p.iterdir() if x.is_file()]
# print(file_lst)
# print(str(file_lst[0]))

# p = Path.cwd()
p = Path('..') / 'data_finam'
file_lst = list(p.glob('**/*'))
print(file_lst)
print(str(file_lst[-1]))
