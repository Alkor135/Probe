# -*- coding: utf-8 -*-

from pathlib import Path
import pathlib

if __name__ == "__main__":
    # path = pathlib.Path.home()
    # file_lst = list(path.glob('**/descript.ion'))
    # print(file_lst)

    print(pathlib.PurePath('c:/Program Files/').root)
    print(pathlib.PurePath(pathlib.Path.cwd()).root)

    path = pathlib.Path('c:/')
    file_lst = list(path.glob('**/descript.ion'))
    print(file_lst)
