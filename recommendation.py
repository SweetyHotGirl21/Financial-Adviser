
import datetime as dt
import calendar

from dateutil.relativedelta import relativedelta

# This function attributes one of three scores to different analysts opinions. positive: 1, neutral: 0, negative: -1
# The output of the function is the cumulative rating of all analysts over a predefined period of time.

def recom(name,df,m = 4):
    months = dt.datetime.today() - relativedelta(months=+m)
    list_of_recoms = list(df[name][df.index >= months].dropna())
    
    rank = 0
    for recom in list_of_recoms:
        if recom.lower() == 'above average':
            rank+=1
        if recom.lower() == 'accumulate':
            rank+=1
        if recom.lower() == 'add':
            rank+=1
        if recom.lower() == 'average':
            rank+=0
        if recom.lower() == 'below average':
            rank-=1
        if recom.lower() == 'buy':
            rank+=1
        if recom.lower() == 'cautious':
            rank+=0
        if recom.lower() == 'conviction buy':
            rank+=1
        if recom.lower() == 'equal-weight':
            rank+=0
        if recom.lower() == 'fair value':
            rank+=0
        if recom.lower() == 'gradually accumulate':
            rank+=1
        if recom.lower() == 'hold':
            rank+=0
        if recom.lower() == 'hold neutral':
            rank+=0
        if recom.lower() == 'in-line':
            rank+=0
        if recom.lower() == 'long-term buy':
            rank+=1
        if recom.lower() == 'market outperform':
            rank+=1
        if recom.lower() == 'market perform':
            rank+=0
        if recom.lower() == 'market underperform':
            rank-=1
        if recom.lower() == 'market weight':
            rank+=0
        if recom.lower() == 'mixed':
            rank+=0
        if recom.lower() == 'negative':
            rank-=1
        if recom.lower() == 'neutral':
            rank+=0
        if recom.lower() == 'outperform':
            rank+=1
        if recom.lower() == 'outperformer':
            rank+=1
        if recom.lower() == 'overweight':
            rank+=1
        if recom.lower() == 'peer perform':
            rank+=0
        if recom.lower() == 'perform':
            rank+=1
        if recom.lower() == 'positive':
            rank+=1
        if recom.lower() == 'reduce':
            rank-=1
        if recom.lower() == 'sector outperform':
            rank+=1
        if recom.lower() == 'sector perform':
            rank+=1
        if recom.lower() == 'sector underperform':
            rank-=1
        if recom.lower() == 'sector weight':
            rank+=0
        if recom.lower() == 'sell':
            rank-=1
        if recom.lower() == 'speculative buy':
            rank+=1
        if recom.lower() == 'strong buy':
            rank+=1
        if recom.lower() == 'strong sell':
            rank-=1
        if recom.lower() == 'top pick':
            rank+=1
        if recom.lower() == 'trim':
            rank-=1
        if recom.lower() == 'underperform':
            rank-=1
        if recom.lower() == 'underperformer':
            rank-=1
        if recom.lower() == 'underweight':
            rank-=1
    return rank

