import pandas as pd

def main(eng_dict):
    # get ticker symbols

    ticker_symbols = list(eng_dict.keys())

    # create mega_df

    cols = eng_dict[ticker_symbols[0]].columns

    mega_df = pd.DataFrame(columns=cols)

    # loop through tickers, concat all DFs, and set index

    for i, ticker in enumerate(ticker_symbols):
        eng_dict[ticker]['ticker'] = ticker
        mega_df = pd.concat([mega_df, eng_dict[ticker]])

    #reorder cols

    cols = ['ticker', 'Date'] + [c for c in mega_df.columns if c not in ['ticker', 'Date']]

    return mega_df[cols].sort_values('Date')