import numpy as np
import pandas as pd
# import pandas_datareader as pdr
import pandas_datareader.data as web

from_date = '2018-04-30'
to_date = '2019-10-20'
#
# data_frame = pdr.get_data_moex('MGNT', from_date, to_date)
# print(data_frame.head())

data_frame = web.DataReader('GS', 'stooq', from_date, to_date)
print(data_frame.head())

# f = web.DataReader('^DJI', 'stooq')
# f.to_excel('rec_data/dji.xlsx')


# f = web.DataReader('MGNT', 'moex', start='2019-07-01', end='2020-07-31')
# f.to_excel('rec_data/mgnt.xlsx')
