# -*- coding: utf-8 -*-

from pathlib import Path
import pandas as pd


file_path = Path.home() / 'PycharmProjects' / 'Probe' / 'data_finam' / 'SPFB.RTS_20200103_20200103_5min.csv'
f_rts_5m = pd.read_csv(file_path)
f_rts_5m.set_index('<TIME>', inplace=True)
f_rts_5m.to_excel('rec_data/f_rts_5m_index.xlsx')
# print(f_rts_5m)
