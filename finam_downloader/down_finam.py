# -*- coding: utf-8 -*-
"""

"""
from urllib.parse import urlencode
from urllib.request import urlopen
from datetime import datetime
from pathlib import Path
from settings import *


class DownloadFinam:
    def __init__(self, ticker, start, end, period=3):
        self.ticker = ticker
        self.period = period
        self.start = start
        self.end = end
        self.market = 14  # Для фьючерсов
        self.datf = 7  # Для тиков
        self.start_date_rev = 0
        self.end_date_rev = 0
        self.url = ''
        self.file_path = 0

    def url_finam(self):
        """
        Функция составляет url для запроса на сервер FINAMa
        """
        if self.ticker == "SPFB.RTS":  # Если выбран фьючерс на индекс РТС
            self.market = 14  # FUTURES = 14  # non-expired futures
        else:
            self.market = 0  # Это рынок, на котором торгуется бумага. Для акций работает с любой цифрой.

        if self.period == 1:  # Если период выбран тики
            self.datf = 7  # Формат записи для тиков 'TICKER, DATE, TIME, LAST, VOL'
        else:
            self.datf = 1  # Формат записи для минутных баров 'TICKER, PER, DATE, TIME, OPEN, HIGH, LOW, CLOSE, VOL'

        # Делаем преобразования дат:
        start_date = datetime.strptime(self.start, "%d.%m.%Y").date()  # Переводим формат в datetime
        self.start_date_rev = datetime.strptime(self.start, '%d.%m.%Y').strftime('%Y%m%d')  # Дата в нужном формате строкой
        end_date = datetime.strptime(self.end, "%d.%m.%Y").date()
        self.end_date_rev = datetime.strptime(self.end, '%d.%m.%Y').strftime('%Y%m%d')

        # Все параметры упаковываем в единую структуру.
        # Здесь есть дополнительные параметры, кроме тех, которые заданы в шапке. См. комментарии.
        params = urlencode([
            ('market', self.market),  # на каком рынке торгуется бумага
            ('em', TICKERS[ticker]),  # вытягиваем цифровой символ, который соответствует бумаге.
            ('code', self.ticker),  # тикер фин инструмента
            ('apply', 0),  # не нашёл что это значит.
            ('df', start_date.day),  # Начальная дата, номер дня (1-31)
            ('mf', start_date.month - 1),  # Начальная дата, номер месяца (0-11)
            ('yf', start_date.year),  # Начальная дата, год
            ('from', start_date),  # Начальная дата полностью
            ('dt', end_date.day),  # Конечная дата, номер дня
            ('mt', end_date.month - 1),  # Конечная дата, номер месяца
            ('yt', end_date.year),  # Конечная дата, год
            ('to', end_date),  # Конечная дата
            ('p', self.period),  # Таймфрейм
            ('f', self.ticker + "_" + self.start_date_rev + "_" + self.end_date_rev),  # Имя сформированного файла
            ('e', ".csv"),  # Расширение сформированного файла
            ('cn', self.ticker),  # ещё раз тикер
            # См.страницу  # https://www.finam.ru/profile/moex-akcii/sberbank/export/
            ('dtf', 1),  # В каком формате брать даты. Выбор из 5 возможных.
            ('tmf', 1),  # В каком формате брать время. Выбор из 4 возможных.
            ('MSOR', 0),  # Время свечи (0 - open; 1 - close)
            ('mstime', "on"),  # Московское время
            ('mstimever', 1),  # Коррекция часового пояса
            ('sep', 1),  # Разделитель полей	(1 - запятая, 2 - точка, 3 - точка с запятой, 4 - табуляция, 5 - пробел)
            ('sep2', 1),  # Разделитель разрядов
            ('datf', self.datf),  # Формат записи в файл. Выбор из 11 возможных (1-для минутных баров, 7-для тиков).
            ('at', 1)  # Нужны ли заголовки столбцов
        ])

        self.url = f'{FINAM_URL}{ticker}_{self.start_date_rev}_{self.end_date_rev}.csv?{params}'  # урл составлен!
        # print(f'Ссылка для запроса готова: {url}')

    def path(self):
        """
        Функция создает имя файла и путь его сохранения
        """
        period_txt = PERIODS[period]  # Для добавления к имени файла периода
        file_name = f'{self.ticker}_{self.start_date_rev}_{self.end_date_rev}_{period_txt}.csv'  # Имя выходного файла
        # print(f'Имя выходного файла {file_name}')

        dir_path = Path('..') / 'data_finam'  # Папка для сохранения (родительский каталог, папка data_finam)
        if not dir_path.exists():  # Проверяем существует ли папка
            dir_path.mkdir()  # Создаем папку при её отсутствии

        self.file_path = Path('..') / 'data_finam' / file_name  # Создаем пути для сохранения файла

    def download(self):
        if not self.file_path.exists():  # Если файла не существует
            txt = urlopen(self.url).readlines()  # Получаем в txt массив данных с Финама.

            with open(self.file_path, 'w', encoding='utf-8') as file_out:  # задаём файл, в который запишем котировки.
                for line in txt:  # записываем файл строку за строкой.
                    file_out.write(line.strip().decode("utf-8") + '\n')

            print(f'Готово. Проверьте файл {str(self.file_path)} по указанному пути')
        else:
            print(f'Файл {str(self.file_path)} уже существует')


if __name__ == "__main__":

    ticker = "SPFB.RTS"  # задаём тикер
    period = 1  # задаём период. Выбор из: 'tick': 1, 'min': 2, '5min': 3, '10min': 4, '15min': 5, '30min': 6, 'hour': 7, 'daily': 8, 'week': 9, 'month': 10
    start = "02.09.2020"  # с какой даты начинать тянуть котировки
    end = "02.09.2020"  # финальная дата, по которую тянуть котировки

    data = DownloadFinam(ticker, start, end, period)
    data.url_finam()
    data.path()
    data.download()
