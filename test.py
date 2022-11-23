import pandas as pd
from pandas_datareader import data as pdr
import numpy as np
import datetime as dt
from scipy.stats import norm
from multivariate_var import multivariate_var

class TestVaR:
    def test_VaR(self):

        assert np.isclose(multivariate_var(tickers = ['AAPL','FB', 'C', 'DIS'],
                                            weights = np.array([.25, .3, .15, .3]),
                                            from_date = "2018-01-01",
                                            to_date = '2019-01-01',
                                            initial_investment = 1000000,
                                            conf_level=0.05,
                                            n = 5 ), # number of days for n-days VaR calculation)
                                            5235.91, atol=0.0001)
