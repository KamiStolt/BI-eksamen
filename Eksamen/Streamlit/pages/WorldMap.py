import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score    


# Load datasets
try:
    df_covid = pd.read_csv("df_covid_cleaned.csv")
    st.success("Datasets successfully loaded!")
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()


# VERDENSKORT
menu = "Worldmap"
st.title("COVID-19 Deaths – worldmap")

df_map = df_covid[['location', 'total_deaths']].dropna()
df_map = df_map[df_map['location'] != 'World']
df_map.rename(columns={"location": "country"}, inplace=True)

fig = px.choropleth(
        df_map,
        locations="country",
        locationmode="country names",
        color="total_deaths",
        color_continuous_scale="Reds",
        title="Totale COVID-19 Deaths pr. Country"
    )

fig.update_layout(geo=dict(showframe=False, showcoastlines=False))
st.plotly_chart(fig, use_container_width=True)