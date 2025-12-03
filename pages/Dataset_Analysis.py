from styles import css
import streamlit as st
import pandas as pd
import numpy as np
import kagglehub
import os
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from mlxtend.frequent_patterns import apriori, association_rules
import plotly.express as px

# streamlit page config n shi
st.set_page_config(
    page_title="Sales Analysis Project",
    layout="wide",
    initial_sidebar_state="expanded"
)

css()
# data loading section

st.header('Application of Data Analysis Techniques: Superstore Sales')

@st.cache_data
def load_data():
    if os.path.exists("train.csv"):
        return pd.read_csv("train.csv")
    
    path = kagglehub.dataset_download("rohitsahoo/sales-forecasting")
    csv_path = os.path.join(path, "train.csv")
    return pd.read_csv(csv_path, encoding='latin1')

try:
    with st.spinner('Loading dataset...'):
        df = load_data()
    df.columns = df.columns.str.strip()
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
    required_cols = ['Customer Name', 'Sales']
    if 'Profit' in df.columns:
        required_cols.append('Profit')
    
    df.dropna(subset=required_cols, inplace=True)
    
    st.success("Dataset loaded successfully!")

except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

 
# data overview section
st.subheader('Dataset Overview')
st.write(f"**Rows:** {df.shape[0]} | **Columns:** {df.shape[1]}")
with st.expander("View Raw Data"):
    st.dataframe(df.head())

st.markdown("---")

# dbscan clustering section
st.header('1. DBSCAN Clustering Analysis')

reference_date = df['Order Date'].max() + pd.Timedelta(days=1)
recency = df.groupby('Customer Name')['Order Date'].max().reset_index()
recency['Recency'] = (reference_date - recency['Order Date']).dt.days

frequency = df.groupby('Customer Name')['Order ID'].nunique().reset_index()
frequency.rename(columns={'Order ID': 'Frequency'}, inplace=True)

monetary = df.groupby('Customer Name')['Sales'].sum().reset_index()
monetary.rename(columns={'Sales': 'Monetary'}, inplace=True)

customer_df = recency.merge(frequency, on='Customer Name').merge(monetary, on='Customer Name')

features_to_scale = ['Recency', 'Frequency', 'Monetary']
if 'Profit' in df.columns:
    profitability = df.groupby('Customer Name')['Profit'].sum().reset_index()
    profitability.rename(columns={'Profit': 'Profitability'}, inplace=True)
    customer_df = customer_df.merge(profitability, on='Customer Name')
    features_to_scale.append('Profitability')
    st.info("Using **RFMP** Analysis (Recency, Frequency, Monetary, Profitability)")
else:
    pass

X = customer_df[features_to_scale]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)
components = pca.fit_transform(X_scaled)
pca_df = pd.DataFrame(data=components, columns=['PC1', 'PC2'])
pca_df['Customer Name'] = customer_df['Customer Name']

# interactive DBSCAN parameters
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Parameters")
    epsilon = st.slider('Epsilon ($\\epsilon$)', 0.1, 5.0, 0.5, 0.1)
    min_samples = st.slider('Min Points (minPts)', 2, 20, 5)

    dbscan = DBSCAN(eps=epsilon, min_samples=min_samples)
    clusters = dbscan.fit_predict(X_scaled)
    
    pca_df['Cluster'] = clusters
    customer_df['Cluster'] = clusters

    n_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
    n_noise = list(clusters).count(-1)
    
    st.info(f"**Clusters:** {n_clusters}")
    st.warning(f"**Noise Points:** {n_noise}")

with col2:
    st.subheader("Cluster Visualization")
    fig = px.scatter(
        pca_df, x='PC1', y='PC2', 
        color=pca_df['Cluster'].astype(str),
        hover_data=['Customer Name'],
        title=f"DBSCAN Clusters"
    )
    st.plotly_chart(fig, use_container_width=True)

if n_clusters > 0:
    st.subheader("Cluster Characteristics (Average)")
    avg_stats = customer_df.groupby('Cluster')[features_to_scale].mean()
    st.dataframe(avg_stats.style.highlight_max(axis=0, color='lightgreen'))

st.markdown("---")

# apriori analysis section
st.header('2. Apriori Analysis (Market Basket)')

#data prep
basket = (df.groupby(['Order ID', 'Sub-Category'])['Sub-Category']
          .count().unstack().reset_index().fillna(0)
          .set_index('Order ID'))

def encode_units(x):
    return 1 if x >= 1 else 0

basket_encoded = basket.applymap(encode_units)

# rules
col_a, col_b = st.columns(2)
with col_a:
    min_support = st.slider('Min Support', 0.001, 0.1, 0.01, 0.001)
with col_b:
    min_lift = st.slider('Min Lift', 1.0, 10.0, 1.2, 0.1)

# run apriori
try:
    frequent_itemsets = apriori(basket_encoded, min_support=min_support, use_colnames=True)
    
    if frequent_itemsets.empty:
        st.warning("No itemsets found. Try lowering Min Support.")
    else:
        rules = association_rules(frequent_itemsets, metric="lift", min_threshold=min_lift)
        
        st.subheader("Top Association Rules")
        rules['antecedents'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
        rules['consequents'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))
        
        st.dataframe(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]
                     .sort_values('lift', ascending=False).head(20))

except Exception as e:
    st.error(f"Apriori Error: {e}")