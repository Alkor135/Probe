# -*- coding: utf-8 -*-
"""
Загрузка котирововок из FINAMa для фьючерса РТС тики
"""
import os
from urllib.parse import urlencode
from urllib.request import urlopen
from datetime import datetime
from pathlib import Path

ticker = "SPFB.RTS"  # задаём тикер
period = 1  # задаём период. Выбор из: 'tick': 1, 'min': 2, '5min': 3, '10min': 4, '15min': 5, '30min': 6, 'hour': 7, 'daily': 8, 'week': 9, 'month': 10
start = "02.09.2020"  # с какой даты начинать тянуть котировки
end = "02.09.2020"  # финальная дата, по которую тянуть котировки

periods = {1: 'tick', 2: 'min', 3: '5min', 4: '10min', 5: '15min', 6: '30min', 7: 'hour', 8: 'daily', 9: 'week'}

print(f'{ticker=}; {period=}; {start=}; {end=}')

# каждой акции Финам присвоил цифровой код:
tickers = {'ABRD': 82460, 'AESL': 181867, 'AFKS': 19715, 'AFLT': 29, 'AGRO': 399716, 'SPFB.RTS': 17455}

FINAM_URL = "http://export.finam.ru/"  # сервер, на который стучимся

if ticker == "SPFB.RTS":  # Если выбран фьючерс на индекс РТС
    market = 14  # FUTURES = 14  # non-expired futures
else:
    market = 0  # можно не задавать. Это рынок, на котором торгуется бумага. Для акций работает с любой цифрой.

if period == 1:
    datf = 6  # Формат записи для тиков
else:
    datf = 1  # Формат записи для OHLC баров

# Делаем преобразования дат:
start_date = datetime.strptime(start, "%d.%m.%Y").date()
start_date_rev = datetime.strptime(start, '%d.%m.%Y').strftime('%Y%m%d')
end_date = datetime.strptime(end, "%d.%m.%Y").date()
end_date_rev = datetime.strptime(end, '%d.%m.%Y').strftime('%Y%m%d')

# Все параметры упаковываем в единую структуру.
# Здесь есть дополнительные параметры, кроме тех, которые заданы в шапке. См. комментарии внизу:
params = urlencode([
    ('market', market),  # на каком рынке торгуется бумага
    ('em', tickers[ticker]),  # вытягиваем цифровой символ, который соответствует бумаге.
    ('code', ticker),  # тикер нашей акции
    ('apply', 0),  # не нашёл что это значит.
    ('df', start_date.day),  # Начальная дата, номер дня (1-31)
    ('mf', start_date.month - 1),  # Начальная дата, номер месяца (0-11)
    ('yf', start_date.year),  # Начальная дата, год
    ('from', start_date),  # Начальная дата полностью
    ('dt', end_date.day),  # Конечная дата, номер дня
    ('mt', end_date.month - 1),  # Конечная дата, номер месяца
    ('yt', end_date.year),  # Конечная дата, год
    ('to', end_date),  # Конечная дата
    ('p', period),  # Таймфрейм
    ('f', ticker + "_" + start_date_rev + "_" + end_date_rev),  # Имя сформированного файла
    ('e', ".csv"),  # Расширение сформированного файла
    ('cn', ticker),  # ещё раз тикер акции
    ('dtf', 1),  # В каком формате брать даты. Выбор из 5 возможных. См. страницу # https://www.finam.ru/profile/moex-akcii/sberbank/export/
    ('tmf', 1),  # В каком формате брать время. Выбор из 4 возможных.
    ('MSOR', 0),  # Время свечи (0 - open; 1 - close)
    ('mstime', "on"),  # Московское время
    ('mstimever', 1),  # Коррекция часового пояса
    ('sep', 1),  # Разделитель полей	(1 - запятая, 2 - точка, 3 - точка с запятой, 4 - табуляция, 5 - пробел)
    ('sep2', 1),  # Разделитель разрядов
    ('datf', datf),  # Формат записи в файл. Выбор из 6 возможных (1-для мин баров, 6-для тиков).
    ('at', 1)  # Нужны ли заголовки столбцов
])

url = f'{FINAM_URL}{ticker}_{start_date_rev}_{end_date_rev}.csv?{params}'  # урл составлен!
print(f'Ссылка для запроса готова: {url}')

period_txt = periods[period]  # Для добавления к имени файла периода
file_name = f'{ticker}_{start_date_rev}_{end_date_rev}_{period_txt}.csv'  # Имя выходного файла
print(f'Имя выходного файла {file_name}')

file_path = Path.home() / 'PycharmProjects' / 'Probe' / 'data_finam' / file_name  # Создаем пути для сохр файла

# if not os.path.isfile(file_name):  # Если файл с таким именем не существует
if not file_path.is_dir():
    txt = urlopen(url).readlines()  # Получаем в txt массив данных с Финама.

    with open(file_path, 'w', encoding='utf-8') as file_out:  # задаём файл, в который запишем котировки.
        for line in txt:  # записываем файл строку за строкой.
            file_out.write(line.strip().decode("utf-8") + '\n')

    print(f'Готово. Проверьте файл {file_path} по указанному пути')
else:
    print(f'Файл {file_path} уже существует')
