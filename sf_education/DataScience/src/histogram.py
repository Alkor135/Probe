# -*- coding: utf-8 -*-
# from sf_education.DataScience.src.basic_graphs import load_prices
from basic_graphs import load_prices
# from PycharmProjects.Probe.sf_education.DataScience.src.basic_graphs import load_prices
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.stats as stats

spx = load_prices('../data/^spx_d.csv')
spx = spx[['Close']]  # В 'spx' оставляем только колонку 'Close'
spx = spx.assign(Pct_change=spx.pct_change())  # Добавляем колонку процентного изменения

close = spx['Pct_change'].values[1:]

n, buckets, patches = plt.hist(close, 50, normed=1)

mean = close.mean()  # Среднее значение
std = close.std()  # Стандартная девиация (стандартное отклонение)
best_fit_line = mlab.normpdf(buckets, mean, std)
plt.plot(buckets, best_fit_line, 'y--')
plt.show()

# plt.plot(spx.index, spx['Close'])
# plt.show()

# print(spx)
