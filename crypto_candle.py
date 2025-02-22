import pandas_datareader as web
import datetime as dt
import mplfinance as mpf

start = dt.datetime(2013, 4, 29)
end = dt.datetime.now()

# Altcoins also work
data = web.DataReader("BTC-USD", "yahoo", start, end)

mpf.plot(data, type="candle", volume=True, style="yahoo")
