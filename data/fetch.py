import yfinance as yf
import sys
import os
import pandas as pd
import shutil
from config import BASE_DIR

def main():
    # get ticker symbol list

    sys.path.append(os.path.abspath('..'))
    from config import ticker_symbols

    #####################
    ### DATA FETCHING ###
    #####################

    # fetch requested ticker data

    data = yf.download(ticker_symbols, period='max', interval='1d')

    # put each ticker in dict

    dict = {}

    if isinstance(data.columns, pd.MultiIndex):
        for ticker in ticker_symbols:
            df = data.xs(ticker, axis=1, level=1, drop_level=False).droplevel(1, axis=1)
            df.reset_index(inplace=True)

            dict[ticker] = df
    
    return dict

if __name__ == '__main__':
    main()