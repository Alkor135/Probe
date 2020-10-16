# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime

start = "02.09.2020"
end = "30.09.2020"

start_date = datetime.strptime(start, "%d.%m.%Y").date()  # Переводим формат в datetime
end_date = datetime.strptime(end, "%d.%m.%Y").date()

date_range = pd.date_range(start_date, end_date)

for single_date in date_range:
    print(single_date.strftime("%Y-%m-%d"))

# print(date_range)
