from pathlib import Path

print(Path.cwd())  # Текущая дирректория
print(Path.home())  # Домашняя дирректория

print(Path('/../data_finam'))  # data_finam в родительской дирректории

print(Path('/../../data_finam'))  # data_finam в предродительской дирректории

print(sorted(Path('..').glob('*.py')))  # все файлы py в родительской дирректории

print(sorted(Path('../..').glob('*.py')))  # все файлы py в предродительской дирректории

print(sorted(Path('../../..').glob('*.py')))  # все файлы py в пред пред родительской дирректории

p = Path.cwd()
print(p.parents[0])
print(p.parents[1])
print(p.parents[2])
