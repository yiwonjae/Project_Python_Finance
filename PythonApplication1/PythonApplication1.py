import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

start   = datetime.datetime(2010,1,1)
end     = datetime.datetime(2016,10,9)

# CODE: GS - A078930
# CODE: SKHINIX - A000660
# CODE: TESNA - 131970
data = web.DataReader("000660.KS", "yahoo", start, end)

print(data)

print(data.info())

# start, end를 주지 않는 경우 default
# start : 2010-01-01
# end   : Function 동작 시간
data = web.DataReader("000660.KS", "yahoo")

print(data.info())

import matplotlib.pyplot as plt

plt.plot(data["Adj Close"])

plt.show()