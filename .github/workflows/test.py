import numpy as np
import pandas as pd
class TestData:
    def test_stocks_returns(self):
        assets = ['AAPL']
        weights = [1.]
        returns = stocks_returns(assets, weights, from_date='09/02/2022', to_date='09/07/2022')
        test_returns = pd.Series(
            data=[-0.0136, -0.0082, 0.0093], 
            index=pd.to_datetime(['09/02/2022', '09/06/2022', '09/07/2022']),
        )
        assert np.allclose(returns, test_returns, atol=0.0001)
    
        assets = ['AAPL', 'GOOGL']
        weights = [0.3, 0.7]
        returns = stocks_returns(assets, weights, from_date='09/02/2022', to_date='09/07/2022')
        test_returns = pd.Series(
            data=[-0.0158, -0.0091, 0.0188], 
            index=pd.to_datetime(['09/02/2022', '09/06/2022', '09/07/2022']),
        )
        assert np.allclose(returns, test_returns, atol=0.0001)

        assets = ['AAPL', 'AMD', 'AMZN', 'GOOGL', 'INTC', 'META', 'MSFT', 'MU', 'NVDA', 'TSLA']
        weights = np.ones(10)
        returns = stocks_returns(assets, weights, from_date='09/02/2022', to_date='09/07/2022')
        test_returns = pd.Series(
            data=[-0.0193, -0.0068,  0.0196],
            index=pd.to_datetime(['09/02/2022', '09/06/2022', '09/07/2022']),
        )
        assert np.allclose(returns, test_returns, atol=0.0001)
