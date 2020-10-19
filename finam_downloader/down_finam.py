# -*- coding: utf-8 -*-
"""
Закачивает исторические данные с ФИНАМа, за указанный период, в указанном формате
Каждый день в своем файле
"""
from urllib.parse import urlencode
from urllib.request import urlopen
from datetime import datetime
from pathlib import Path
from settings import *
import pandas as pd
import time


class DownloadFinam:
    def __init__(self, ticker, period=3):
        self.ticker = ticker
        self.period = period
        self.market = 14  # Для фьючерсов
        self.datf = 7  # Для тиков
        self.url = ''

    def url_finam(self, date_rev):
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

        start_date = datetime.strptime(date_rev, "%Y%m%d").date()  # Переводим формат в datetime
        end_date = start_date

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
            ('f', self.ticker + "_" + date_rev + "_" + date_rev),  # Имя сформированного файла
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

        self.url = f'{FINAM_URL}{ticker}_{date_rev}_{date_rev}.csv?{params}'  # урл составлен!
        # print(f'Ссылка для запроса готова: {url}')

    def path(self, date_rev):
        """
        Функция создает имя файла и путь его сохранения
        """
        period_txt = PERIODS[period]  # Для добавления к имени файла периода
        file_name = f'{self.ticker}_{date_rev}_{date_rev}_{period_txt}.csv'  # Имя выходного файла
        # print(f'Имя выходного файла {file_name}')

        dir_path = Path('..') / 'data_finam'  # Папка для сохранения (родительский каталог, папка data_finam)
        if not dir_path.exists():  # Проверяем существует ли папка
            dir_path.mkdir()  # Создаем папку при её отсутствии

        return Path('..') / 'data_finam' / file_name  # Создаем пути для сохранения файла

    def download(self, date_rev):
        self.url_finam(date_rev)  # Вызываем функцию составления url
        file_path = self.path(date_rev)  # Вызываем функцию составления путей и имени файла
        if not file_path.exists():  # Если файла не существует
            txt = urlopen(self.url).readlines()  # Получаем в txt массив данных с Финама.

            with open(file_path, 'w', encoding='utf-8') as file_out:  # задаём файл, в который запишем котировки.
                for line in txt:  # записываем файл строку за строкой.
                    file_out.write(line.strip().decode("utf-8") + '\n')

            print(f'Готово. Проверьте файл {file_path} по указанному пути')
        else:
            print(f'Файл {file_path} уже существует')


if __name__ == "__main__":

    ticker = "SPFB.RTS"  # задаём тикер
    period = 3  # задаём период. Выбор из: 'tick': 1, 'min': 2, '5min': 3, '10min': 4, '15min': 5, '30min': 6, 'hour': 7
    start = "01.01.2020"  # с какой даты начинать тянуть котировки
    end = "02.09.2020"  # финальная дата, по которую тянуть котировки

    # Делаем преобразования дат:
    start_date_range = datetime.strptime(start, '%d.%m.%Y').strftime('%Y%m%d')  # Дата в нужном формате строкой
    end_date_range = datetime.strptime(end, '%d.%m.%Y').strftime('%Y%m%d')
    date_range = pd.date_range(start_date_range, end_date_range)

    data = DownloadFinam(ticker, period)  # Создаем экземпляр класса
    for single_date in date_range:
        download_date = single_date.strftime('%Y%m%d')
        data.download(download_date)

        time.sleep(2)  # Сон в 2 секунды
