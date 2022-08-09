# sourcery skip: use-fstring-for-formatting
import pandas as pd
import streamlit as st

from app.sections.header import header
from app.sections.single_stock import single_stock
from app.sections.multiple_stocks import multiple_stocks
from app.libraries.data import get_data

from app.libraries.constants import TICKERS


if __name__ == '__main__':

    header()

    dropdown = st.multiselect("Select your assets", TICKERS)
    start_date = st.date_input("Start Date", value=pd.to_datetime('2022-01-01'))
    end_date = st.date_input("End Date", value=pd.to_datetime('today'))

    if len(dropdown) == 1:
        data = get_data(dropdown, start_date, end_date)
        single_stock(dropdown, data)

    elif len(dropdown) > 1:
        data = get_data(dropdown, start_date, end_date)
        multiple_stocks(dropdown, data)
    
