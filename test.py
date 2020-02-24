from datetime import datetime, timedelta
from dateutil.relativedelta import *

date = datetime.now()
print(date)
# 2018-09-24 13:24:04.007620

date1 = date + relativedelta(months=+1)
date2 = date + relativedelta(months=+2)
date3 = date + relativedelta(months=+3)
date4 = date + relativedelta(months=+4)
date5 = date + relativedelta(months=+6)
date6 = date + relativedelta(months=+7)
lst = []
print(date1)
lst.append(date6)
lst.append(date2)
lst.append(date1)
lst.append(date4)
lst.append(date5)
lst.append(date3)
print(lst)
lst.sort()
print(lst)
# 2019-03-24 13:24:04.007620