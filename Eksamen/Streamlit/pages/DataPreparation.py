import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score    

# Load datasets
try:
    df_covid = pd.read_csv("df_covid_cleaned.csv")
    df_age = pd.read_csv("df_age_cleaned.csv")
    df_health = pd.read_csv("df_health_cleaned.csv")
    st.success("Datasets successfully loaded!")
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

st.title("Data Overview")
st.write("Explore the datasets structure and statistics")
st.subheader("Covid-level Dataset")
st.dataframe(df_covid.head(10), use_container_width=True)
st.dataframe(df_covid.describe(), use_container_width=True)

st.subheader("Health-level Dataset")
st.dataframe(df_health.head(10), use_container_width=True)

st.subheader("Age-level Dataset")
st.dataframe(df_age.head(10), use_container_width=True)