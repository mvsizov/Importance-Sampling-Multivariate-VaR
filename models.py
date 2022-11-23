import pandas as pd
from pandas_datareader import data as pdr
import numpy as np
import datetime as dt
from scipy.stats import norm

def multivariate_var(tickers, # list of tickers
                     weights, # np.array of weights
                     from_date, #date in format yyyy-mm-dd
                     to_date, #date in format yyyy-mm-dd
                     initial_investment, # value of initial investment (integer or float)
                     alpha, # alpha, where 1 - alpha = confidence level
                     n # number of days for n-days VaR calculation
                     ):
    '''
    Be careful: you should round the answer to 2 decimal points!
    '''
    raise Exception(NotImplementedError)