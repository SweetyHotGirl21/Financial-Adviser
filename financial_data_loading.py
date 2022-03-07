from typing import ClassVar
import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from dateutil.relativedelta import relativedelta


# Load preprocessd data from the prepared .csv files
def load_data_csv():
    business_df = pd.read_csv("businiess_df.csv")
    # Keep only variables relevant for the stock picking
    business_df = business_df[["symbol","longBusinessSummary","longName","sector","dividendYield","priceToBook"]]
    sustain_df = pd.read_csv("sustain_df.csv")
    sustain_df.rename(columns={"Unnamed: 0": "symbol"}, inplace= True)
    sustain_df.set_index("symbol", inplace = True, drop = False)
    recommendation_df = pd.read_csv("recommendation_df.csv")
    recommendation_df["Date"] = pd.to_datetime(recommendation_df["Date"])
    recommendation_df.set_index("Date", inplace = True)
    return business_df, sustain_df, recommendation_df

# Obtain all ticker symbols of companies in the S&P 500 by scraping from Wikipedia
def get_ticker_list():
    sp_wiki_df_list = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    sp_df = sp_wiki_df_list[0]
    sp_ticker_list = list(sp_df["Symbol"].values)
    return sp_ticker_list

# Obtain the retrun time series for all available companies with the option to choose the beginning year
# The time sereise consist of daily returns
def load_retrun_time_series(y = 2010):
    sp_ticker_list = get_ticker_list()
    sp_data = yf.download(sp_ticker_list)   # The download function allows to request multile TS of securities
    sp_close = sp_data["Adj Close"]
    sp_close_2010 = sp_close.loc[(sp_close.index >= dt.datetime(y,1,1)) & (sp_close.index < dt.datetime(2021,1,1))]
    sp_return = sp_close.pct_change()
    sp_return_2010 = sp_return.loc[sp_return.index >= dt.datetime(y,1,1)].dropna(axis = 1)
    sp_t_list = list(sp_return_2010.columns.values)
    return sp_return_2010

# Creats a dict that collects the yf.Tickker symbols for all available companies
def create_ticker_dict():
    sp_ticker_list = get_ticker_list()
    ticker_dict = {key: yf.Ticker(key) for key in sp_ticker_list} # requesting all the ticker symbols and saving in dict
    return  ticker_dict



# !!!!!!!!!!!!!!!!!!!!! CAREFULL the following function Take AGES !!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# That's why we're provinding additional .csv files which contain the results of the functions

# Creates a datafame that contains all the business information for available companies
def get_business_data():
    t_dict = create_ticker_dict()
    businiess_df = pd.DataFrame(columns=list(t_dict["F"].info))

    for key in t_dict:
        if type(t_dict[key]) is yf.ticker.Ticker:
            businiess_df = businiess_df.append(pd.DataFrame([ticker_dict[key].info]))
    else:
        print(key)

    businiess_df.to_csv("businiess_df.csv")  
    return businiess_df

# Creates a datafame that contains all the sustainability information for available companies
def get_sustain_data():
    t_dict = create_ticker_dict()
    sustain_df = pd.DataFrame(columns=list(t_dict[list(t_dict.keys())[0]].sustainability.index))

    for stock in t_dict:
        print(stock)
        if type(t_dict[stock].sustainability) is pd.core.frame.DataFrame:
            temp = t_dict[stock].sustainability.T
            sustain_df = sustain_df.append(temp).rename(index={"Value":stock}) 
    else:
        print(stock)

    sustain_df.to_csv("sustain_df.csv")    
    return sustain_df

# Creates a datafame that contains all the analyst resommendations for available companies
def get_recom_data():
    t_dict = create_ticker_dict()
    recommendation_df = pd.DataFrame()
    i = 0
    for ticker in t_dict:
        temp = t_dict[ticker].recommendations
        if type(temp) is pd.core.frame.DataFrame:
            temp = pd.DataFrame(temp.rename(columns = {"To Grade": ticker})[ticker])
            recommendation_df = pd.concat([recommendation_df,temp],join = "outer" )
        else:
            print(ticker)
        if  i%5 == 0:
            print(recommendation_df)
        i += 1

    recommendation_df.sort_index().to_csv("recommendation_df.csv")
    return recommendation_df.sort_index()



