# -*- coding: utf-8 -*-

import pandas as pd

df_data = pd.read_csv('../data_finam/SPFB.RTS_20200103_20200103_5min.csv')  # Загрузка данных их файла в df
print(df_data)

df_data['date_time'] = df_data['<DATE>'].astype(str) + ' ' + df_data['<TIME>'].astype(str)  # Слияние столбцов
print(df_data)
print(df_data.columns.values)  # Проверяем, что есть в названиях столбцов


