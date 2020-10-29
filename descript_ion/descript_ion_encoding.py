# -*- coding: utf-8 -*-

from pathlib import Path
import pathlib

if __name__ == "__main__":
    # path = pathlib.Path.home()
    # file_lst = list(path.glob('**/descript.ion'))
    # print(file_lst)

    print(pathlib.PurePath('c:/Program Files/').root)
    print(pathlib.PurePath('c:/').root)

    # path = pathlib.Path('c:/')
    # file_lst = list(path.glob('**/descript.ion'))  # Создает список всех файлов descript.ion на диске с
    # print(file_lst)

    path = pathlib.Path('c:/descript.ion')  # Путь к файлу который читаем

    path_out = pathlib.Path('c:/descript_ion.new')  # Путь к файлу который создаем
    # path_out.touch(mode=0o666, exist_ok=True)  # Отказано в доступе

    text_file = path.read_text(encoding='cp866')  # Чтение файла

    # path_out.write_text(text_file, encoding='UTF8')

    with path_out.open(mode='wt') as new_file:  # Отказано в доступе
        new_file.write(text_file)

    print(text_file)
