import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score  



# ANALYSE
menu = "Analyse"
st.title("Analyse: Population vs. Total Cases")df_selected = df[['population', 'total_cases']].dropna()

X = df_selected[['population']]
y = df_selected['total_cases']

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)

fig, ax = plt.subplots()
ax.scatter(X, y, label="Data")
ax.plot(X, y_pred, color="red", label="Linear regression")
ax.set_xlabel("Population")
ax.set_ylabel("Total Cases")
ax.set_title("Linear Regression: Population vs. Total Cases")
ax.legend()
st.pyplot(fig)

st.write(f"R²-score: {r2:.4f}")