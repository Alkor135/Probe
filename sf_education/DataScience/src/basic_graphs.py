# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt


def load_prices(file_name):
    """ Функция загрузки данных из csv файла в data_frame pandas"""
    data = pd.read_csv(file_name)  # Загрузка данных их файла  ,  index_col=pd.DatetimeIndex('Date')
    data = data.set_index(pd.DatetimeIndex(data['Date']))  # Устанавливаем индекс на дату и делаем формат даты
    data = data.drop('Date', 1)  # Удаляем колонку с датой, т.к. дата у нас теперь в индексе
    return data


def normalize_value(table, new_column, source_column):
    """
    Нормализует колонку (цены) относительно самого раннего по времени значения. Все последующие значения будут
    представлены в виде процентного изменения к этой цене
    :param table: Data Frame который нормализуем
    :param new_column: Название колонки с нормализованными данными
    :param source_column: Колонка с данными которые нормализуем
    :return: Data Frame с новой колонкой нормализованных данных
    """
    price_at_t0 = table.iloc[-1][source_column]  # Берем самое первое по времени значение (к нему нормализуем)
    table[new_column] = table.apply(lambda row: row[source_column] / price_at_t0, axis=1)
    return table


if __name__ == "__main__":
    oil = load_prices('../data/oilPrices.csv')  # Загрузка данных по нефти из файла
    usd_rub_prices = load_prices('../data/usdPrices.csv')  # Загрузка данных по usd/rub из файла

    # re-index Индексы не совпадают поэтому реиндексируем. индекс RUB будет равен индексу нефти
    common_index = oil.index
    usd_rub_prices = usd_rub_prices.reindex(common_index)
    usd_rub_prices = usd_rub_prices.fillna(method='backfill')  # Заполняем "none" последним значением

    # Нормализация цены для корректного отображения на графике нескольких инструментов
    # Графики будут начинаться из одной точки
    usd_rub_prices = normalize_value(usd_rub_prices, 'Normalized value', 'Price')
    oil = normalize_value(oil, 'Normalized value', 'Price')

    # По оси X будет index (date)
    x_axis = oil.index
    # По оси Y будет price
    oil_y_axis = oil['Normalized value'].values
    rub_y_axis = usd_rub_prices['Normalized value'].values

    # Построение графиков
    plt.plot(x_axis, oil_y_axis, color='red', label='Oil Price')  # Вывод графика линией
    plt.plot(x_axis, rub_y_axis, 'b--', label='Rub Price')  # color='blue'
    plt.legend()  # Для показа label
    plt.show()
