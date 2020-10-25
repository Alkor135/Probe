
file = open('tst.csv', 'r', encoding='UTF8')  # Открываем файл на чтение в формате
lines = file.readlines()  # Читаем построчно и запоминаем в lines
file.close()  # Закрываем файл

one_column_value = []  # Сохраняем результат сюда
for line in lines:  # Перебироем строки прочитанного lines
    line = line.replace('\n', '')  # Очищаем от конца строки
    ogrns = line.split(';')  # Разбиваем по ';'
    for ogrn in ogrns:
        ogrn = ogrn.replace(',', '')  # Очищаем от лишних запятых
        ogrn = ogrn.replace(' ', '')  # Очищаем от лишних пробелов
        one_column_value.append(f'{ogrn}\n')  # Сохраняем каждый ОГРН в список с новой строки
    # print(line)
    # print(ogrns)

ready_file = open('read.csv', 'w', encoding='UTF8')  # Открываем файл на запись
ready_file.writelines(one_column_value)  # Записывем в файл строки из списка
ready_file.close()
# print(one_column_value)
