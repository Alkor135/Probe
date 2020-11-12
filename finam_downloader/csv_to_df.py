# -*- coding: utf-8 -*-

# import pandas as pd
from pathlib import Path


if __name__ == "__main__":

	# Выбор файла с ТФ в минутах
	dir_name = 'c:/data_finam_quote_csv'  # Папка с файлами
	file_name = 'SPFB.RTS_5min_200103.csv'  # Имя файла
	file_path = Path(f'{dir_name}/{file_name}')  # Путь к файлу
	if file_path.exists():  # Если файл существует
		split_name = file_name.split('_')
		print(split_name)


	df_data = pd.read_csv(file_path)  # Загрузка данных их файла в df
	print(df_data)

	df_data['date_time'] = df_data['<DATE>'].astype(str) + ' ' + df_data['<TIME>'].astype(str)  # Слияние столбцов
	print(df_data)
	print(df_data.columns.values)  # Проверяем, что есть в названиях столбцов
