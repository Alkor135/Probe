import pandas as pd
import pandas_datareader.data as web


from_date = '2018-04-30'
to_date = '2019-10-20'

magnit = web.DataReader('MGNT', 'moex', start='2019-07-01', end='2020-07-31')
print(magnit.head())
# magnit.to_csv('rec_data/mgnt.csv')

# magnit = pd.read_csv('rec_data/mgnt.xlsx')
# magnit.set_index('Time', inplace=True)