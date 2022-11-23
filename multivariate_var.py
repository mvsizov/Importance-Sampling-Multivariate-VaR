import pandas as pd
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
import numpy as np
import datetime as dt
from scipy.stats import norm

def multivariate_var(tickers, # list of tickers
                     weights, # np.array of weights
                     from_date, #date in format yyyy-mm-dd
                     to_date, #date in format yyyy-mm-dd
                     initial_investment, # value of initial investment (integer or float)
                     conf_level,
                     n # number of days for n-days VaR calculation
                     ):
    # raise Exception(NotImplementedError)

    # import returns data
    data = pdr.get_data_yahoo(tickers, start=from_date, end=to_date)['Close']
    returns = data.pct_change()

    # generate covariance matrix
    cov_matrix = returns.cov()

    # calculate mean and standard deviation
    port_mean = returns.mean().dot(weights)
    mean_investment = (1 + port_mean) * initial_investment
    port_stdev = np.sqrt(weights.T.dot(cov_matrix).dot(weights))
    stdev_investment = initial_investment * port_stdev

    # determine confidence level cutoff from the normal distribution
    cutoff = norm.ppf(conf_level, mean_investment, stdev_investment)

    # calculate daily VaR
    VaR = initial_investment - cutoff

    # calculate n-days VaR
    VaR_n_days = np.round(VaR * np.sqrt(n), 2)

    return VaR_n_days