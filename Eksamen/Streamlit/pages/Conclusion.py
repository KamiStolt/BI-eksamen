import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score    

# KONKLUSION
menu = "Conclusion"
st.title("Conclusion")
st.write("""
   This study explored why COVID-19 death rates varied across countries by analyzing demographic, socio-economic, and health-related factors. The goal was not to predict outcomes, but to uncover patterns that explain global differences in mortality.

The most consistent finding was that age-related demographics—especially median age and the proportion of people aged 65+—strongly correlate with higher COVID-19 death rates. This was confirmed through both statistical analysis and classification models, which effectively identified countries at greater risk based on age structure.

Population size, while moderately related to total deaths, had no meaningful link to deaths per capita. This shows that per capita metrics are more useful for comparing severity across countries than raw totals, which can be misleading due to large population sizes.

Contrary to expectations, the Human Development Index (HDI) was not a strong predictor of COVID-19 mortality. Countries with similar HDI scores often had very different death rates, suggesting that HDI does not capture critical pandemic-specific variables like healthcare capacity or policy response.

Health-related factors such as smoking and chronic conditions showed only weak correlations with national death rates. While these increase individual risk, they alone cannot explain country-level outcomes—further emphasizing the role of broader structural and policy-related factors.

In summary, the variation in COVID-19 death rates is best explained by demographic structure, especially aging populations. However, outcomes were also shaped by healthcare capacity, public health interventions, and reporting accuracy. For future pandemics, countries must focus on protecting vulnerable age groups and strengthening health systems, rather than relying solely on general development indicators like HDI.
    """)