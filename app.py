import streamlit as st
import pandas as pd
import joblib


st.title("Sales Forecasting ML Project")


st.write(
"Predict future sales using historical Superstore data"
)


# Load dataset

df = pd.read_csv(
    "Sample - Superstore.csv",
    encoding="latin1"
)


# Date conversion

df["Order Date"] = pd.to_datetime(
    df["Order Date"]
)


# Monthly sales

sales = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Sales"].sum()


st.subheader("Historical Sales Trend")


st.line_chart(
    sales
)


st.subheader("Sales Data")

st.dataframe(df.head())
