import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf

style.use('ggplot')
START = dt.datetime(2000,1,1)
END = dt.datetime(2016,12,31)

# data_frame = web.DataReader('TSLA', 'yahoo', START, END)
data_frame = yf.download('TSLA', start=START, end=END)
# data_frame looks similar to a spreadsheet

print(data_frame.head())


