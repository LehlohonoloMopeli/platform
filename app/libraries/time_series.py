from statsmodels.tsa.stattools import adfuller, kpss
import pandas as pd

def adf_test(df):
    """
    Returns ADF test results
    """

    # return adfuller(df)

    result = adfuller(df)
    df_adf = pd.Series(result[:2], index=['ADF Test Statistic', 'p-value'])
    for key, value in result[4].items():
        df_adf[f'Critical Value ({key})'] = value
    df_adf.rename('Values', inplace=True)
    return df_adf


def kpss_test(df):
    """
    Returns KPSS test results
    """

    # return kpss(df)

    result = kpss(df)
    df_kpss = pd.Series(result[:2], index=['KPSS Test Statistic', 'p-value'])
    for key, value in result[3].items():
        df_kpss[f'Critical Value ({key})'] = value
    df_kpss.rename('Values', inplace=True)
    return df_kpss
   
