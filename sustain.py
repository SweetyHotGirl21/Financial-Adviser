# The following two functions return list of companies related to the investors preferences 
# over the general business

import numpy as np
import pandas as pd


# Should companies delaing with nuclear energy be excluded?
def nuclear(data, option):
    user = option
    if user.lower() == "no": 
        out = list(data[data["nuclear"] == False])
    else: 
        out = list(data.index)
    return out

# Investors prefrences over enviroment
def environment(data, option):
    user = option
    # if the investor is concerned return the 30% of companies with the best "environmentScore"
    if user.lower() == "yes":    
        out = list(data[data["environmentScore"] > data["environmentScore"].quantile(.7)].index)
    # else return all companies 
    else: 
        out = list(data.index)
    return out

# Investors prefrences over social activities 
def social(data, option):
    user = option
    # if the investor is concerned return the 30% of companies with the best "environmentScore"
    if user.lower() == "yes":    
        out = list(data[data["socialScore"] > data["socialScore"].quantile(.7)].index)
    # else return all companies 
    else: 
        out = list(data.index)
    return out

