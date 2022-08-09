import streamlit as st
import yfinance as fy
import plotly.express as px

from app.libraries.time_series import adf_test, kpss_test
from statsmodels.tsa.seasonal import seasonal_decompose


def single_stock(dropdown, data):
    with st.container():
        st.write("##")
        st.subheader(f'Historical Price of {", ".join(dropdown)}')
        st.write("Mean : $ {:.2f}".format(data.mean()))
        st.write("Standard deviation : {:.2f}".format(data.std()))
        fig = px.line(data, x=data.index, y="Adj Close", title=f'Historical Price of {", ".join(dropdown)}')

        fig.update_xaxes(rangeslider_visible=True)
        st.plotly_chart(fig, use_container_width=True)
        st.subheader("Test for Stationarity")
        st.write("##")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("ADF Test")
            st.write(adf_test(data))
        with col2:
            st.subheader("KPSS Test")
            st.write(kpss_test(data))
        st.subheader("Decomposition")
        st.write("##")
        decomp = seasonal_decompose(x=data, model='multiplicative', period=12)
        st.write(decomp.trend)
