from styles import css
import streamlit as st
import os

# 1. Page Config
st.set_page_config(
    page_title="CS365 - Final Project",
    layout="wide",
    initial_sidebar_state="expanded"
)
css()

# 2. Introduction Content
st.header('Application of Data Analysis Techniques: Superstore Sales')
st.subheader('Introduction')
st.write('This streamlit program is to demonstrate the use of the Apriori Data Analysis Technique on a chosen dataset depicting Supermarket Sales. This dataset includes the order and shipping dates of the sale, the customer\'s name, and details of the product.')

st.subheader('Apriori Data Analysis')
st.write('The reason why Apriori was chosen over the other forms of Data Analysis is because it effectively uncovers hidden patterns and relationships within large transaction datasets, making it ideal for identifying product bundles and optimizing cross-selling strategies.')

# 3. Team Members
st.subheader('Team Members')

col1, col2, col3, col4 = st.columns(4, gap="large")

def show_member(image_path, name):
    with st.container():
        # Check if image exists to avoid crash
        if os.path.exists(image_path):
            st.image(image_path, width=200)
        else:
            st.warning(f"Image {image_path} not found")
        st.write(name)

with col1:
    show_member("kp.jpg", 'Kelvin Pehrson Kierulf')
with col2:
    show_member("zillion.jpg", 'John Zillion Reyes')
with col3:
    show_member("gil.jpg", 'Gil Florenz Sastre')
with col4:
    show_member("raymond.jpg", 'Raymond Gerard Tio')