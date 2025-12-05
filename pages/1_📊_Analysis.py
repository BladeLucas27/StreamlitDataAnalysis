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

st.set_page_config(page_title="Dataset Analysis", layout="wide", page_icon="📊")
css()

# --- DATA LOADING ---
@st.cache_data
def load_data():
    if os.path.exists("train.csv"):
        return pd.read_csv("train.csv")
    path = kagglehub.dataset_download("rohitsahoo/sales-forecasting")
    csv_path = os.path.join(path, "train.csv")
    return pd.read_csv(csv_path, encoding='latin1')

try:
    df = load_data()
    df.columns = df.columns.str.strip()
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
    required_cols = ['Customer Name', 'Sales']
    if 'Profit' in df.columns:
        required_cols.append('Profit')
    df.dropna(subset=required_cols, inplace=True)
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# --- CONTENT ---
st.header('📊 Dataset Analysis')
st.subheader('Dataset Overview')
st.write(f"**Rows:** {df.shape[0]} | **Columns:** {df.shape[1]}")
with st.expander("View Raw Data"):
    st.dataframe(df.head())
st.markdown("---")

# DBSCAN
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
    st.info("Using **RFMP** Analysis")

X = customer_df[features_to_scale]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=2)
components = pca.fit_transform(X_scaled)
pca_df = pd.DataFrame(data=components, columns=['PC1', 'PC2'])
pca_df['Customer Name'] = customer_df['Customer Name']

col1, col2 = st.columns([1, 2])
with col1:
    epsilon = st.slider('Epsilon ($\\epsilon$)', 0.1, 5.0, 0.5, 0.1)
    min_samples = st.slider('Min Points (minPts)', 2, 20, 5)
    dbscan = DBSCAN(eps=epsilon, min_samples=min_samples)
    clusters = dbscan.fit_predict(X_scaled)
    pca_df['Cluster'] = clusters
    customer_df['Cluster'] = clusters
    n_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
    st.info(f"**Clusters:** {n_clusters}")

with col2:
    fig = px.scatter(pca_df, x='PC1', y='PC2', color=pca_df['Cluster'].astype(str), hover_data=['Customer Name'])
    st.plotly_chart(fig, use_container_width=True)

if n_clusters > 0:
    st.dataframe(customer_df.groupby('Cluster')[features_to_scale].mean())

st.markdown("---")

# APRIORI
st.header('2. Apriori Analysis')
basket = (df.groupby(['Order ID', 'Sub-Category'])['Sub-Category'].count().unstack().reset_index().fillna(0).set_index('Order ID'))
basket_encoded = basket.applymap(lambda x: 1 if x >= 1 else 0)

col_a, col_b = st.columns(2)
with col_a:
    min_support = st.slider('Min Support', 0.001, 0.01, 0.005, 0.001)
with col_b:
    min_lift = st.slider('Min Lift', 1.0, 10.0, 1.2, 0.1)

try:
    frequent_itemsets = apriori(basket_encoded, min_support=min_support, use_colnames=True)
    if not frequent_itemsets.empty:
        rules = association_rules(frequent_itemsets, metric="lift", min_threshold=min_lift)
        st.subheader("Top Association Rules")
        st.dataframe(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].sort_values('lift', ascending=False).head(20))
    else:
        st.warning("No itemsets found.")
except Exception as e:
    st.error(f"Apriori Error: {e}")