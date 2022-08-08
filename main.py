# sourcery skip: use-fstring-for-formatting
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import yfinance as fy
import plotly.express as px

# Basic setup configs
plt.set_loglevel('WARNING')
st.set_page_config(page_title="financial analysis", page_icon=":tada:", layout="centered")


# Header section
with st.container():
    st.header("Financial Analysis")
    st.markdown("This application will help you to analyze financial data")
    st.markdown("Developed by [Lehlohonolo Mopeli](https://github.com/LehlohonoloMopeli)")


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


# sourcery skip: use-fstring-for-formatting

    
# Data section
# sourcery skip: use-fstring-for-formatting
with st.container():
    tickers = ('AMZN', 'GOOGL', 'JNJ', 'V', 'PG', 'UNH', 'JPM', 'HD', 'VZ', 'NFLX', 'DIS', 'MRK', 'PEP', 'BAC', 'KO', 
        'WMT','CVX', 'ABT', 'AMGN', 'MCD', 'COST', 'NKE', 'PM', 'QCOM', 'LOW', 'BA', 'LMT', 'SBUX', 'UPS', 'CAT')
    dropdown = st.multiselect("Select your assets", tickers)

    start_date = st.date_input("Start Date", value=pd.to_datetime('2022-01-01'))
    end_date = st.date_input("End Date", value=pd.to_datetime('today'))

    if len(dropdown) == 1:
        st.write("##")
        st.subheader("Historical Price of {}".format(", ".join(dropdown)))
        data = fy.download(dropdown, start_date, end_date)['Adj Close']
        st.write("Mean : $ {:.2f}".format(data.mean()))
        st.write("Standard deviation : {:.2f}".format(data.std()))
        fig = px.line(data, x=data.index, y="Adj Close", title="Historical Price of {}".format(", ".join(dropdown)))
        fig.update_xaxes(rangeslider_visible=True)
        st.plotly_chart(fig)
        # st.line_chart(data)
        # st.write(np.std(data))

    elif len(dropdown) > 1:
        st.write("##")
        st.subheader("Portfolio Historical Normalized Cumulative Returns for {}".format(", ".join(dropdown)))
        data = fy.download(dropdown, start_date, end_date)['Adj Close']
        data_normalised = relative_ret(fy.download(dropdown, start_date, end_date)['Adj Close'])
        st.line_chart(data_normalised)

        st.write("##")
        st.subheader("Covariance Matrix of the Portfolio")
        cov_matrix = cov_matrix_calc(data_normalised)
        st.write(cov_matrix)

        st.write("##")
        st.subheader("Heatmap of the Correlation of Assets")
        fig, ax = plt.subplots()
        sns.heatmap(data_normalised.corr(), ax=ax)
        st.write(fig)

        st.write("##")
        st.subheader("Correlation Matrix of the portfolio")
        corr_matrix = corr_matrix_calc(data_normalised)
        st.write(corr_matrix)

        st.write("##")
        st.subheader("Portfolio Cumulative Returns")
        st.line_chart(data.sum(axis = 1))

        st.write("##")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Portfolio Return")
            st.write(np.mean(data.sum(axis = 1)))
        with col2:
            st.subheader("Portfolio Volatility")
            st.write(np.std(data.sum(axis = 1)))

        st.write("##")
        st.subheader("Portfolio Log Returns")
        log_ret = log_returns(data)
        st.line_chart(log_ret)

        st.write("##")
        st.subheader("Scatter Plot of Log Returns")
        mean, sdv = generate_ptfs(log_ret, 1000)
        log_ret_plot_data = pd.DataFrame(mean, sdv)
        # log_ret_plot_data.plot.scatter(log_ret_plot_data[0], log_ret_plot_data[1])
        st.dataframe(log_ret_plot_data)

