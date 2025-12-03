from styles import css
import streamlit as st

st.set_page_config(page_title="Conclusion", layout="wide")
css()

st.header("📝 Conclusion & Recommendations")

st.success("### Key Takeaways")
st.markdown("""
Based on our analysis of the Superstore Sales dataset, we have identified distinct patterns in customer behavior and product sales.
""")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Cluster Insights (DBSCAN)")
    st.markdown("""
    jema jema type shi""")
    
with col2:
    st.subheader("Product Associations (Apriori)")
    st.markdown("""
    omsim apriori type shi
    """)

st.info("### Final Recommendation")
st.write("we recommend type shi")