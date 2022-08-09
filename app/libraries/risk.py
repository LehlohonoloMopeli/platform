import pandas as pd
import numpy as np

def relative_ret(df):
    """
    Returns relative returns
    """
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret


def cov_matrix_calc(array):
    """
    Returns covariance matrix
    """
    return pd.DataFrame(array.cov())


def corr_matrix_calc(array):
    """
    Returns correlation matrix
    """
    return pd.DataFrame(array.corr())


def log_returns(df):
    """
    Returns log returns
    """
    return np.log(df / df.shift(1))


# Define a function to generate N number of random portfolios given a DataFrame of returns
def generate_ptfs(returns, N):
    ptf_rs = []
    ptf_stds = []
    for _ in range(N):
        # Generate random weights between 0 and 1
        weights = np.random.random(len(returns.columns))
        # Ensure that the weights add up to 1
        weights /= np.sum(weights)
        # Append the portfolio return to the list of portfolio returns
        ptf_rs.append(np.sum(returns.mean() * weights) * 252)
        # Append the portfolio volatility to the list of portfolio volatilities
        ptf_stds.append(np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights))))
    ptf_rs = np.array(ptf_rs)
    ptf_stds = np.array(ptf_stds)
    return ptf_rs, ptf_stds

    