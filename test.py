import pandas as pd
from pandas_datareader import data as pdr
import numpy as np
import datetime as dt
from scipy.stats import norm
from multivariate_var import multivariate_var

class TestVaR:
    def test_VaR(self):

        tickers_list = [['AAPL', 'FB', 'C'], ['DIS', 'TSLA', 'ADSK', 'AMC'],
                        ['AAPL', 'FB', 'C', 'DIS', 'TSLA', 'ADSK', 'AMC']]
        weights_list = [np.array([0.1, 0.1, 0.8]), np.array([0.5, 0.05, 0.4, 0.05]),
                        np.array([0.2, 0.2, 0.2, 0.2, 0.1, 0.05, 0.05])]
        from_date_list = ['2018-02-01', '2018-04-01', '2018-08-01']
        to_date_list = ['2020-05-01', '2020-08-01', '2021-01-01']
        intitial_investment_list = [1000, 1050, 1000.1]
        conf_level_list = [0.01, 0.05, 0.07]
        n_list = [10, 50, 100]
        results = [145.71, 245.1, 248.16]

        for values, result in zip(zip(tickers_list, weights_list, from_date_list, to_date_list,
                                      intitial_investment_list, conf_level_list, n_list), results):
            assert (multivariate_var(*values) == result )



