import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

from app.libraries.risk import (
    relative_ret, 
    cov_matrix_calc, 
    corr_matrix_calc, 
    log_returns,
    generate_ptfs
    )

def multiple_stocks(dropdown, data):
    with st.container():

        st.write("##")
        st.subheader(f'Portfolio Historical Normalized Cumulative Returns for {", ".join(dropdown)}')
        data_normalised = relative_ret(data)
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
        st.line_chart(data.sum(axis=1))

        st.write("##")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Portfolio Return")
            st.write(np.mean(data.sum(axis=1)))
        with col2:
            st.subheader("Portfolio Volatility")
            st.write(np.std(data.sum(axis=1)))

        st.write("##")
        st.subheader("Portfolio Log Returns")
        log_ret = log_returns(data)
        st.line_chart(log_ret)

        st.write("##")
        st.subheader("Scatter Plot of Log Returns")
        mean, sdv = generate_ptfs(log_ret, 1000)
        log_ret_plot_data = pd.DataFrame(mean, sdv)
        st.dataframe(log_ret_plot_data)
