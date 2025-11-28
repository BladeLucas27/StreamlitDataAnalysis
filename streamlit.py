import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Final Project",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def css():
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
        [data-testid="stHeader"] {visibility: hidden;}

        .stApp {
            background-color: #082e90;
            background-size: cover;
        }
                
        h1, h2 {
            color: #93fff0 !important;
        }
        
        h3 {
            color: #B8C7F4 !important;
        }

        p, .stMarkdown {
            color: #FFC1D6 !important;
        }

        </style>
    """, unsafe_allow_html=True)
css()

st.header('Application of Apriori Analysis to a Supermarket Sales dataset')
st.subheader('About the Dataset')
st.write('Hello World')

st.subheader('Transaction Table')

data = {
    'Still to be imported',
    'Still to be cleaned'
}

st.table(data, border="horizontal")