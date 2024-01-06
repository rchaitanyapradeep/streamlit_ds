
import streamlit as st
import plotly.express as px
import pandas as pd

# Load data
df = pd.read_csv("/Users/chaitanyapradeeprepaka/Library/CloudStorage/OneDrive-Personal/Mac/Trainings/AI course/Data/house-prices-advanced-regression-techniques/train.csv")

# Streamlit app structure
'Basic Data Exploration App'
"This is a simple data exploration app using Streamlit and Plotly."

# Data display
if st.checkbox('Show Dataset'):
    st.write(df)

# User inputs for plot customization
x_axis_val = st.selectbox('Select the X-axis', options=df.columns)
y_axis_val = st.selectbox('Select the Y-axis', options=df.columns)
plot_type = st.selectbox('Select Plot Type', ['scatter', 'line'])

# Creating Plotly chart
if plot_type == 'scatter':
    fig = px.scatter(df, x=x_axis_val, y=y_axis_val)
else:
    fig = px.line(df, x=x_axis_val, y=y_axis_val)

st.plotly_chart(fig)
