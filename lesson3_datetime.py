
import datetime as dt
import time as tm

now = dt.datetime.now()  # actual date and time
now.year

fivedays = dt.timedelta(days=5)

now-fivedays

dt.datetime.strftime(now, '%F %T')
now.strftime('%b, %d. %Y')

onedate = dt.datetime.strptime('2016-07-04 14:45:31', '%Y-%m-%d %H:%M:%S' )
type(onedate)

# lubridate





import urllib.request
urllib.request.urlretrieve("https://vincentarelbundock.github.io/" +
                           "Rdatasets/csv/Ecdat/Garch.csv",
                           "Exchange_rates.csv")
rates=pd.read_csv("Exchange_rates.csv")
rates.head()

rates=rates[["date","dm","bp"]] # keep only these three columns
rates.date=pd.to_datetime(rates.date, format="%y%m%d")
rates.head()
rates.dtypes
rates = rates.set_index("date")
rates["1980"].head()
rates["1980-01":"1980-02"].head()

rates.resample('W').mean().head()
rates.resample('2D').sum().head()
rates.resample('2W').agg([np.mean, np.min, np.max]).head()


