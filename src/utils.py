import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_bar_chart(df, x_col, y_col, title):
    fig = px.bar(df, x=x_col, y=y_col, title=title)
    return fig

def create_pie_chart(df, names_col, values_col, title):
    fig = px.pie(df, names=names_col, values=values_col, title=title)
    return fig
