from styles import css
import streamlit as st

st.set_page_config(
    page_title="CS365 - Final Project",
    layout="wide",
    initial_sidebar_state="expanded"
)


css()

st.header('Application of Data Analysis Techniques: Superstore Sales')
st.subheader('Introduction')
st.write('This streamlit program is to demonstrate the use of the Apriori Data Analysis Technique on a chosen dataset depicting Supermarket Sales. This dataset includes the order and shipping dates of the sale, the customer\'s name, and details of the product.')
st.subheader('Apriori Data Analysis')
st.write('The reason why Apriori was chosen over the other forms of Data Analysis is because.......')
st.subheader('Team Members')


col1, col2, col3, col4 = st.columns(4, gap="large", border=True)



with col1:
    with st.container(height="content", horizontal_alignment="center"):
        st.image("kp.jpg", width=200)
        st.write('Kelvin Pehrson Kierulf')

with col2:
    with st.container(height="content", horizontal_alignment="center"):
        st.image("zillion.jpg", width=200)
        st.write('John Zillion Reyes')

with col3:
    with st.container(height="content", horizontal_alignment="center"):
        st.image("gil.jpg", width=200)
        st.write('Gil Florenz Sastre')

with col4:
    with st.container(height="content", horizontal_alignment="center"):
        st.image("raymond.jpg", width=200)
    with st.container(height="content", horizontal_alignment="center"):
        st.write('Raymond Gerard Tio')