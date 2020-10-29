# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/sf_pe_salaries_2011.csv')  # Загрузка данных их файла
# data = data.reindex(data['Id'])
data['BasePay'] = data['BasePay'].replace('Not Provided', '0')  # Заменяем в DF "Not Provided" на "0"
data = data.fillna('0')  # Все 'Nan' меняем на "0"
data['BasePay'] = data['BasePay'].astype(float)  # Меняем тип данных в колонке на 'float'
data = data.drop('Id', 1)  # Удаление ненужной колонки, которая стала индексом
print(data)

x_axis = data.index  # Ось X
x_axis_percentile = data.index / data.index.max() * 100  # Ось X показывает прорцентное соотношение
y_axis = data['BasePay'].values  # Ось Y
y_axis_sorted = sorted(y_axis)  # Сортируем все значения из колонки 'BasePay' Ось Y

plt.scatter(x_axis_percentile, y_axis_sorted)  # вывод графика точками
plt.grid()  # Добавляеи сетку на график
plt.show()
