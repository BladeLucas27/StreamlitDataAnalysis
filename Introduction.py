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
st.header('Purchasing Patterns and Product Associations: Data Analysis')
st.subheader('Introduction')
st.write('In the competitive landscape of retail, understanding customer behavior and purchasing patterns is essential for driving business growth and operational efficiency. The ability to segment customers effectively and identify product relationships can significantly enhance inventory management, marketing strategies, and overall profitability. This analysis examines the Superstore Sales Dataset, which contains comprehensive transactional data from a retail superstore, including order information, product categories, customer segments, sales figures, and geographic details.')

st.subheader('Purpose of Research')
st.markdown('<br><h6 style="text-align: center; font-style: italic;">How can we identify distinct customer purchasing patterns and product associations to optimize inventory management and targeted marketing strategies?</h6><br>', unsafe_allow_html=True)
st.write('This research question seeks to uncover hidden patterns in customer behavior and product relationships that can inform business decisions around product placement, promotional bundling, and customer segmentation.')

st.subheader('About Dataset')
st.write('The Superstore Sales Dataset from Kaggle contains transactional sales data from a retail superstore GitHub, typically including features such as order dates, product categories, customer segments, sales amounts, quantities, discounts, and geographic information. This dataset is commonly used for sales analysis and forecasting tasks.')
# Add st.table here for dataset attributes

st.subheader('Analysis Techniques')
st.write('we employ two complementary data mining techniques: DBSCAN clustering and Apriori association rule mining.')
# justify each techniques blahblah blah

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
    show_member("assets/kp.jpg", 'Kelvin Pehrson Kierulf')
with col2:
    show_member("assets/zillion.jpg", 'John Zillion Reyes')
with col3:
    show_member("assets/gil.jpg", 'Gil Florenz Sastre')
with col4:
    show_member("assets/raymond.jpg", 'Raymond Gerard Tio')
