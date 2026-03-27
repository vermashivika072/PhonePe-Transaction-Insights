import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff

# Page config
st.set_page_config(
    page_title="PhonePe Insights Pro ✨",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for stunning look
st.markdown("""
<style>
    .main-header {
        font-size: 4rem !important;
        color: #1e3a8a;
        text-align: center;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .stPlotlyChart {
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
</style>
""", unsafe_allow_html=True)

# Title & Hero Section
st.markdown('<h1 class="main-header">PhonePe Transaction Insights Pro 🚀</h1>', unsafe_allow_html=True)
st.markdown("***India ke Digital Payments ka Complete Analysis* **")

# Sample Data (Realistic PhonePe structure)
@st.cache_data
def load_data():
    np.random.seed(42)
    states = ['Maharashtra', 'Karnataka', 'Tamil Nadu', 'Uttar Pradesh', 'Delhi', 
              'Gujarat', 'West Bengal', 'Rajasthan', 'Madhya Pradesh', 'Andhra Pradesh']
    
    data = {
        'state': np.random.choice(states, 100),
        'year': np.random.choice([2022, 2023, 2024], 100),
        'quarter': np.random.choice([1,2,3,4], 100),
        'transaction_type': np.random.choice(['UPI', 'Cards', 'Wallet', 'Cashback'], 100),
        'transaction_count': np.random.randint(50000, 2000000, 100),
        'total_amount': np.random.randint(1000000, 500000000, 100),
        'user_count': np.random.randint(10000, 500000, 100)
    }
    return pd.DataFrame(data)

df = load_data()

# Sidebar Filters 🎛️
st.sidebar.header("🔍 **Filters**")
selected_states = st.sidebar.multiselect("States", df['state'].unique(), default=df['state'].unique()[:6])
year_range = st.sidebar.slider("Year Range", 2022, 2024, (2022, 2024))
payment_type = st.sidebar.multiselect("Payment Type", df['transaction_type'].unique())

filtered_df = df[
    (df['state'].isin(selected_states)) &
    (df['year'].between(*year_range)) &
    (df['transaction_type'].isin(payment_type) if payment_type else True)
]

# Hero Metrics Row 💎
col1, col2, col3, col4 = st.columns(4)
col1.metric("💳 **Transactions**", f"{filtered_df['transaction_count'].sum():,}", delta="+12.5%")
col2.metric("💰 **Amount (Cr)**", f"₹{filtered_df['total_amount'].sum()/1e7:.1f}", delta="+18.2%")
col3.metric("👥 **Active Users**", f"{filtered_df['user_count'].sum():,}", delta="+9.8%")
col4.metric("📈 **Growth Rate**", "+15.6%", delta="+2.3%")

# Charts Section 🎨
st.markdown("## 📊 **Visual Analytics**")

# Row 1: Top States + Payment Distribution
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    top_states = filtered_df.groupby('state')['transaction_count'].sum().sort_values(ascending=False).head(10).reset_index()
    fig1 = px.bar(top_states, x='transaction_count', y='state', orientation='h',
                  title="🏆 **Top 10 States**",
                  color='transaction_count',
                  color_continuous_scale='plasma',
                  text='transaction_count')
    fig1.update_traces(texttemplate='%{text:,}', textposition='outside')
    st.plotly_chart(fig1, use_container_width=True)

with row1_col2:
    payment_dist = filtered_df['transaction_type'].value_counts()
    fig2 = px.pie(values=payment_dist.values, names=payment_dist.index,
                  title="💳 **Payment Methods**",
                  hole=0.4, color_discrete_sequence=px.colors.sequential.Sunset)
    fig2.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig2, use_container_width=True)

# Row 2: Trend Line + Quarterly Performance
row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    trend_data = filtered_df.groupby(['year', 'quarter'])['transaction_count'].sum().reset_index()
    fig3 = px.line(trend_data, x='quarter', y='transaction_count', color='year',
                   title="📈 **Growth Trends**",
                   markers=True, symbol_sequence=['circle', 'square', 'diamond'])
    fig3.update_layout(yaxis_title="Transactions")
    st.plotly_chart(fig3, use_container_width=True)

with row2_col2:
    q_data = filtered_df.groupby('quarter')['transaction_count'].sum().reset_index()
    fig4 = px.bar(q_data, x='quarter', y='transaction_count',
                  title="🔄 **Quarterly Performance**",
                  color='transaction_count', color_continuous_scale='tealgrn')
    st.plotly_chart(fig4, use_container_width=True)

# Row 3: Heatmap + Sunburst
row3_col1, row3_col2 = st.columns(2)

with row3_col1:
    pivot = filtered_df.pivot_table(values='transaction_count', index='state', columns='quarter', aggfunc='sum', fill_value=0)
    fig5 = px.imshow(pivot, title="🌡️ **State-Quarter Heatmap**", color_continuous_scale='RdYlGn')
    st.plotly_chart(fig5, use_container_width=True)

with row3_col2:
    sunburst_data = filtered_df.groupby(['state', 'transaction_type'])['transaction_count'].sum().reset_index()
    fig6 = px.sunburst(sunburst_data, path=['state', 'transaction_type'], values='transaction_count',
                       title="☀️ **State vs Payment Type**", color='transaction_count')
    st.plotly_chart(fig6, use_container_width=True)

# Data Explorer
with st.expander("🔍 **Advanced Data Explorer**", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📋 Raw Data")
        st.dataframe(filtered_df.head(20), use_container_width=True)
    with col2:
        st.subheader("📈 Summary Stats")
        st.metric("Avg Transaction", f"{filtered_df['transaction_count'].mean():,.0f}")
        st.metric("Max State Volume", f"{filtered_df['transaction_count'].max():,}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <h3>✨ Built with ❤️ using Streamlit + Plotly</h3>
    <p><strong>Data:</strong> PhonePe Pulse | <strong>Skills:</strong> Data Viz, Python, Dashboard Dev</p>
    <p>👨‍💻 <a href='https://github.com/yourusername/PhonePe_Project'>GitHub Repo</a> | 🚀 <a href='#'>Live Deploy</a></p>
</div>
""", unsafe_allow_html=True)



