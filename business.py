# The following two functions return list of companies related to the investors preferences 
# over the general business

import pandas as pd
import numpy as np


# Returns the companies which are best suited for the investors preferences over constant payments
def get_div_comp(data, option):   
    s = option
    # if the investor wnats a constant income stream from the investment we propose the 40% of companies with the highest 
    # dividend yield
    if s.lower() == "yes":    
        out = list(data[data["dividendYield"] > data["dividendYield"].quantile(.6)].index)
    # if that is not import we keep all companies
    else: 
        out = list(data.index)
    return out


# This function takes into account the preferences of the investor about the expected growth of the company
def get_growth_comp(data, option):
    user = option
    # if the investor wnats to invest in a growing company, we propose the 30% companies wth the highest P/B
    if user.lower() == "yes":    
        out = list(data[data["priceToBook"] > data["priceToBook"].quantile(.7)].index)
    # if the investor wnats to invest in a established company, we propose the 50% companies wth the lowest P/B
    else: 
        out = list(data[data["priceToBook"] < data["priceToBook"].quantile(.5)].index)
    return out

