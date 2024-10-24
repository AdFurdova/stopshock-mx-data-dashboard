import streamlit as st
import pandas as pd
import plotly.express as px

st.title("MX Data Dashboard")

st.title("CSV File Uploader")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/STOPSHOCK_MX_clean.csv")

st.write("### Data Preview")
st.dataframe(df)

st.sidebar.title("Column Options")
column = st.sidebar.selectbox("Select a column for analysis", df.columns)

st.write(f"### {column} Analysis")
value_counts = df[column].value_counts()
missing_percentage = df[column].isnull().sum() / len(df) * 100

st.write(f"**Value Counts for {column}:**")
st.write(value_counts)

st.write(f"**Missing Values Percentage for {column}:** {missing_percentage:.2f}%")

st.write(f"### Distribution Plot of {column}")
fig = px.histogram(df, x=column, title=f"Distribution of {column}")
st.plotly_chart(fig)

st.write(f"### Missing Data Distribution for {column}")
missing_fig = px.bar(
    x=["Missing", "Not Missing"],
    y=[df[column].isnull().sum(), df[column].notnull().sum()],
    labels={"y": "Count"},
    title=f"Missing Data for {column}"
)
st.plotly_chart(missing_fig)
