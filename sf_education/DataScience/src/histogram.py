# -*- coding: utf-8 -*-
from sf_education.DataScience.src.basic_graphs import load_prices
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib import pyplot, mlab

spx = load_prices('../data/^spx_d.csv')
spx = spx[['Close']]  # В 'spx' оставляем только колонку 'Close'
spx = spx.assign(Pct_change=spx.pct_change())  # Добавляем колонку процентного изменения

close = spx['Pct_change'].values[1:]
# print(close)

# plt.hist(close, 50)  # Построение графика гистограммы
# plt.show()

n, buckets, patches = plt.hist(close, 50, normed=1)

mean = close.mean()  # Среднее значение
std = close.std()  # Стандартная девиация (стандартное отклонение)
mu = mean
sigma = std
best_fit_line = mlab.normpdf(buckets, mu, sigma)
plt.plot(buckets, best_fit_line, 'y--')
plt.show()

# plt.plot(spx.index, spx['Close'])
# plt.show()

# print(spx)
