import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick # optional may be helpful for plotting percentage
import numpy as np
import pandas as pd
import seaborn as sb # optional to set plot theme
sb.set_theme() # optional to set plot theme

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())

class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()


    def get_data(self):
        """method that downloads data and stores in a DataFrame
           uncomment the code below wich should be the final two lines 
           of your method"""
            # self.calc_returns(data)
        # return data
        pass

    
    def calc_returns(self, df):
        """method that adds change and return columns to data"""
        pass

    
    def plot_return_dist(self):
        """method that plots instantaneous returns as histogram"""
        pass


    def plot_performance(self):
        """method that plots stock object performance as percent """
        pass
                  



def main():
    # uncomment (remove pass) code below to test
    # test = Stock(symbol=[stock_symbol]) # optionally test custom data range
    # print(test.data)
    # test.plot_performance()
    # test.plot_return_dist()
    pass

if __name__ == '__main__':
    main() 