
from datetime import datetime, timedelta

delta = timedelta(weeks=1, days=2, hours=3, minutes=4, seconds=5, milliseconds=6,
                  microseconds=7)
print(f'{delta = }\t-\t{delta}')


date_1 = datetime(2012, 12, 21)
date_2 = datetime(2017, 8, 19)
delta = date_2 - date_1
print(f'{delta = }\t-\t{delta}')
birthday = datetime(1503, 12, 14)
dlt = timedelta(days=365.25 * 33)
new_date = birthday + dlt
print(f'{new_date = }\t-\t{new_date}')
