# -*- coding: utf-8 -*-

from datetime import datetime
import pandas as pd


def date_proba(single_date, single_date_2):
    print(type(single_date))


start = "01.09.2020"  # с какой даты начинать тянуть котировки
end = "30.09.2020"  # финальная дата, по которую тянуть котировки

# Делаем преобразования дат:
start_date_range = datetime.strptime(start, '%d.%m.%Y').strftime('%Y%m%d')  # Дата в нужном формате строкой
end_date_range = datetime.strptime(end, '%d.%m.%Y').strftime('%Y%m%d')
date_range = pd.date_range(start_date_range, end_date_range)

for single_date in date_range:  # single_date уже имеет тип datetime
    start_date = single_date
    print(single_date.strftime('%Y.%m.%d'))

    print(start_date.day)
    print(start_date.month - 1)
    print(start_date.year)
    print(start_date)


