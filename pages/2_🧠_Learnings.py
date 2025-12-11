from styles import css
import streamlit as st

st.set_page_config(page_title="Learnings", layout="wide", page_icon="🧠")
css()

st.header("🧠 Project Learnings & Challenges")

st.subheader("1. Data Quality Issues")
st.markdown("""
* **Missing Profit Column:** We discovered that the Kaggle dataset version `sales-forecasting` lacked the 'Profit' column. 
    * *Solution:* We implemented adaptive code that automatically switches from **RFMP** (including Profit) to **RFM** (Recency, Frequency, Monetary) analysis if the column is missing.
* **Encoding Errors:** The raw CSV file used non-standard characters, causing `UnicodeDecodeError`.
    * *Solution:* We forced the dataloader to use `encoding='latin1'` to correctly parse the file.
""")

st.subheader("2. Technical Implementation")
st.markdown("""
* **Interactive Clustering:** We learned how to use Streamlit sliders to dynamically tune DBSCAN hyperparameters ($\epsilon$ and minPts), visualizing the changes instantly.
* **Dimensionality Reduction:** We applied PCA to visualize 4-dimensional customer data on a 2D scatter plot.
""")

