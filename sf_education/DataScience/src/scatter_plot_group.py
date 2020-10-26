# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/sf_pe_salaries_2011.csv')  # Загрузка данных их файла
# data = data.reindex(data['Id'])
data['BasePay'] = data['BasePay'].replace('Not Provided', '0')  # Заменяем в DF "Not Provided" на "0"
data = data.fillna('0')  # Все 'Nan' меняем на "0"
data['BasePay'] = data['BasePay'].astype(float)  # Меняем тип данных в колонке на 'float'
data = data.drop('Id', 1)
# print(data)

# x_axis = data.index  # Ось X
# x_axis_percentile = data.index / data.index.max() * 100  # Ось X показывает прорцентное соотношение
# y_axis = data['BasePay'].values  # Ось Y
# y_axis_sorted = sorted(y_axis)  # Сортируем все значения из колонки 'BasePay' Ось Y
#
# plt.scatter(x_axis_percentile, y_axis_sorted)
# plt.grid()  # Добавляеи сетку на график
# plt.show()

base_pay = data['BasePay'].values  # Список всех значений колонки BasePay
print(f' До очистки:{len(base_pay)}')
base_pay = base_pay[base_pay > 1000]
print(f' После очистки:{len(base_pay)}')

step = 20000
buckets = list(range(1000, int(base_pay.max()), step))
chelikov_in_buckets = []
for bucket_start in buckets:
    bucket_end = bucket_start + step
    kol_vo = base_pay[(base_pay > bucket_start) & (base_pay < bucket_end)]
    chelikov_in_buckets.append(len(kol_vo))
    # print(bucket_start, bucket_end)

# print(len(buckets))
# print(len(chelikov_in_buckets))

x_axis = buckets
y_axis = chelikov_in_buckets

plt.scatter(x_axis, y_axis)  # Вывод графика точками
plt.plot(x_axis, y_axis)  # Вывод линейного графика
plt.show()

