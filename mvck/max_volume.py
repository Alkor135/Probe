# -*- coding: utf-8 -*-
import time
import pandas as pd


def max_volume_cluster(time_candle):
    """
    Функция подсчитывает объемы по всем кластерам свечи и возвращает цену с макс объемом и этот макс объем в кластере
    :param time_candle: Время начала свечи
    :return: Цена кластера с макс объемом, макс объем из всех кластеров
    """
    # Формирование df под одну свечу
    df_candle = df_ticks[df_ticks['<TIME>'] >= time_candle]  # Отсекаем предшествующие
    df_candle = df_candle[df_candle['<TIME>'] < time_candle + 500]  # Отсекаем последующие

    # Группировка по ценам в свече
    s_rez = df_candle.groupby('<LAST>')['<VOL>'].sum()  # Series (в индексе цена, в значениях суммы объемов)
    max_clu = s_rez.max()  # Нахождение максимального значения в Series (макс сумма объема в кластере)
    max_idx = s_rez.idxmax()  # Нахождение индекса для максимального значения в Series (соответствует цене)
    return max_idx, max_clu


if __name__ == "__main__":
    start = time.time()
    df_5m = pd.read_csv('SPFB.RTS_200901_200901.csv', delimiter=',')
    df_ticks = pd.read_csv('SPFB.RTS_200901_200901_ticks.csv', delimiter=',')

    add_dic = {'<MAX_V_PR>': [], '<MAX_V>': []}
    num = 0
    for idx in df_5m.index:  # Перебираем индексы df_5m
        cur_time = df_5m.iloc[idx][3]  # Время начала выбранной свечи
        response = max_volume_cluster(cur_time)
        add_dic['<MAX_V_PR>'].append(response[0])
        add_dic['<MAX_V>'].append(response[1])

    df = pd.DataFrame(add_dic)
    df_merge = df_5m.join(df)

    end = time.time()
    print(f' Время выполнения: {round(end - start, 3)} сек.')
    print(df_merge)
