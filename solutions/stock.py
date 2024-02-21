# from eod import EodHistoricalData
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import os
import pandas as pd
import seaborn as sb
import yfinance as yf
sb.set_theme()

DEFAULT_DATE = dt.date.isoformat(dt.date.today() - dt.timedelta(396))


class Stock:
    def __init__(self, symbol, date =DEFAULT_DATE, folder=None):
        self.symbol = symbol
        self.date = date
        self.folder = folder
        self.data = self.get_data()


    def get_data(self):
        data = yf.download(self.symbol, start=self.date)
        data.index = data.index.date
        self.calc_returns(data)
        return data

    def calc_returns(self, df):
        df['returns'] = np.log(df.Close).diff().round(4)
        df['change'] = df['Close'].diff()
        df.dropna(inplace= True)

    
    def plot_return_dist(self):
        start = self.data.index[0]
        end  = self.data.index[-1]
        plt.hist(self.data['returns'], bins=20, edgecolor='w')
        plt.suptitle(f"Distribution of returns for {self.symbol}", fontsize=14)
        plt.title(f"From {start} to {end}", fontsize=12)
        plt.show()


    

    def plot_performance(self):
        start = self.data.index[0]
        end  = self.data.index[-1]
        plt.plot((self.data.Close / self.data.Close[0] - 1) * 100)
        plt.axhline(0, c='r', ls='--')
        plt.suptitle(f"Volatility of returns for {self.symbol}", fontsize=14)
        plt.title(f"From {start} to {end}", fontsize=12)
        plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
        plt.show()



    


            
                  



def main():
    test = Stock(symbol='AAPL')
    # print(test.data)
    test.plot_return_dist()
    test.plot_performance()

if __name__ == '__main__':
    main()    







