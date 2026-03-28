import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("🏦 PhonePe Transaction Insights")

# Pure Pandas + Native Charts
data = {
    'State': ['Maharashtra', 'Karnataka', 'Tamil Nadu'],
    'Transactions': [1250000, 980000, 750000],
    'Amount_Cr': [500, 380, 280]
}
df = pd.DataFrame(data)

# Native Streamlit Charts (NO Plotly!)
col1, col2 = st.columns(2)

with col1:
    st.subheader("💳 Transactions")
    st.bar_chart(df.set_index('State')['Transactions'])

with col2:
    st.subheader("💰 Amount")
    st.line_chart(df.set_index('State')['Amount_Cr'])

# Data Table
st.subheader("📊 Data")
st.dataframe(df)

st.caption("Fast PhonePe Dashboard | Shivika Verma")



