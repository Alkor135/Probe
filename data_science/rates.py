import pandas as pd
import numpy as np
# ежедневный обменный курс
# https://open.canada.ca/data/en/dataset/1bc25b1e-0e02-4a5e-afd7-7b96d6728aac

# Загрузите CSV-файл
# rates = pd.read_csv('https://lemay.ai/forex/10100008.csv')
rates = pd.read_csv('10100008.csv')

# Решите, какие колонки нам нужны
rates_cols = ['REF_DATE', 'VALUE']

# Сохраняйте только спотовую цену закрытия для нашей валютной пары
rates = rates[rates['Type of currency'] == 'United States dollar, closing spot rate']

# Сбросьте столбцы, которые нам не нужны, и заполните нулевые значениями (0)
rates = rates[rates_cols].fillna(0)

# Форсируйте общий индекс с экономическими данными, которые мы получим дальше
rates.index = pd.to_datetime(rates['REF_DATE'])

# Теперь, когда мы установили индекс, отбросьте дополнительный столбец даты
rates.drop(['REF_DATE'], axis=1, inplace=True)

# Давайте дадим нашему активу хорошее дружественное человеку имя: USD_CAD
rates.rename(columns={'VALUE': 'USD_CAD'}, inplace=True)

# Если курс находится в выходные дни или дневной рынок закрыт, то используйте самый последний дневной курс
# Выходные длятся 2 дня, так что копируйте субботние вещи в воскресенья
# Перенесите ставки на 3-дневное и 4-дневное закрытие рынка
while rates[rates == 0].count(axis=0)['USD_CAD']/len(rates.index) > 0:
    print("Смещение ставок. Дни со ставкой в 0 = %", rates[rates == 0].count(axis=0)['USD_CAD']/len(rates.index))
    rates['yesterday'] = rates['USD_CAD'].shift(1)
    rates['USD_CAD'] = np.where(rates['USD_CAD'] == 0, rates['yesterday'], rates['USD_CAD'])

# Убедитесь, что у нас нет дней со ставками 0
print("Дни со ставкой в 0 = %", rates[rates == 0].count(axis=0)['USD_CAD']/len(rates.index))

# Спотовая проверка результатов по календарю торговых дней: http://www.swingtradesystems.com/trading-days-calendars.html
# График данных
rates.drop(['yesterday'], axis=1, inplace=True)
rates.plot()
rates.tail()