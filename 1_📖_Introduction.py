from styles import css
import streamlit as st
import os

# 1. Page Config
st.set_page_config(
    page_title="Introduction",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📖"
)
css()

# 2. Introduction Content
st.header('Purchasing Patterns and Product Associations: Data Analysis')
st.subheader('Introduction')
st.write('In the competitive landscape of retail, understanding customer behavior and purchasing patterns is essential for driving business growth and operational efficiency. The ability to segment customers effectively and identify product relationships can significantly enhance inventory management, marketing strategies, and overall profitability. This analysis examines the Superstore Sales Dataset, which contains comprehensive transactional data from a retail superstore, including order information, product categories, customer segments, sales figures, and geographic details.')

st.subheader('Purpose of Research')
# st.markdown('<br><h6 style="text-align: center; font-style: italic;">How can we identify distinct customer purchasing patterns and product associations to optimize inventory management and targeted marketing strategies?</h6><br>', unsafe_allow_html=True)
st.info(':material/forum: ***How can we identify distinct customer purchasing patterns and product associations to optimize inventory management and targeted marketing strategies?***')
st.write("This research question deserves focused attention because it addresses multiple high-impact business challenges simultaneously while being grounded in actionable data analysis. The question bridges the gap between raw transactional data that most businesses collect and strategic intelligence that drives competitive advantage. Rather than examining isolated metrics, it seeks to understand the underlying behavioral patterns that explain why customers make the purchasing decisions they do, and how products relate to each other in customers' minds and shopping baskets.")

st.subheader('About Dataset')
st.markdown('The [Superstore Sales Dataset](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting/data?select=train.csv) from Kaggle contains transactional sales data from a retail superstore GitHub. This dataset is widely used for non-stationary data, such as economic data, weather data, stock prices, and retail sales forecasting.')
with st.expander("Dataset Features", expanded = True):
    st.dataframe({
        "Features": [
            "Customer Name",
            "Order ID",
            "Order Date",
            "Category",
            "Sub-Category",
            "Sales",
        ],
        "Description": [
            "Name of the customer",
            "Order identification number",
            "Date of order's creation",
            "Category assigned to the product of the order",
            "Specific category for the product",
            "Acquired sales of the order"
        ]
    })

st.subheader('Analysis Techniques')
st.write('we employ these two complementary data mining techniques for the analysis of this dataset')
st.info("""
    ### DBSCAN Clustering
    > Why DBSCAN Clustering?

    DBSCAN is particularly well-suited for the Superstore dataset because it can identify customer segments based on purchasing behavior without requiring pre-specification of the number of clusters, which is ideal when natural customer groupings are unknown. Given the dataset's nature, DBSCAN excels at discovering dense regions of similar purchasing patterns while effectively handling outliers—such as unusual bulk orders or exceptionally high-value transactions—by classifying them as noise rather than forcing them into inappropriate clusters. This density-based approach is especially valuable for identifying micro-segments of customers with unique purchasing behaviors across different geographic regions and product categories, enabling more nuanced targeting strategies than traditional k-means clustering would allow.
""")
st.info("""
    ### Apriori
    > Why Apriori?

    Apriori is the optimal technique for uncovering product associations in the Superstore dataset because it systematically identifies which product categories and subcategories are frequently purchased together, generating actionable association rules with measurable confidence and support metrics. The dataset's transactional structure, containing order-level information across multiple product categories (Furniture, Office Supplies, Technology) and their subcategories, makes it perfectly suited for market basket analysis where Apriori can reveal patterns like "customers who buy chairs often also purchase filing cabinets" or "technology buyers in certain regions tend to bundle phones with accessories." These insights directly inform cross-selling strategies and promotional bundling opportunities, while the algorithm's support and confidence thresholds ensure that only statistically significant and commercially relevant associations are surfaced for business action.
""")

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
