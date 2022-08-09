import matplotlib.pyplot as plt
import streamlit as st

from app.libraries.constants import GITHUB_URL

def header():
    # Basic setup configs
    plt.set_loglevel('WARNING')
    st.set_page_config(page_title="financial analysis", page_icon=":tada:", layout="centered")


    # Header section
    with st.container():
        st.header("Financial Analysis")
        st.markdown("This application will help you to analyze financial data")
        st.markdown(f"Developed by [Lehlohonolo Mopeli]({GITHUB_URL})")
        

