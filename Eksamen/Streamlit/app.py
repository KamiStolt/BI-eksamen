import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# st.set_page_config(page_title="COVID-19 Analysis", layout="wide")

# Indlæs data
df_covid = pd.read_csv("df_covid_cleaned.csv")
df_age = pd.read_csv("df_age_cleaned.csv")
df_health = pd.read_csv("df_health_cleaned.csv")

# INTRODUKTION
menu = "Introduktion"
st.title(" Explaining COVID-19 Death Rates Across Countries: The Role of Demographics, Health, and Development")
st.write("""
This project explores why some countries were hit harder by COVID-19 than others. We examine key factors such as population size, age distribution, health conditions, and the Human Development Index (HDI) to see how they relate to death rates — both total and per capita.
Our goal is to uncover patterns that can help identify high-risk populations and support better planning for future pandemics. Behind the data are real people, and by understanding what drives the outcomes, we hope to inform smarter and more compassionate public health decisions.
""")
st.write("""
Made by: Juvena, Kamilla og Jeanette 
""")



    


