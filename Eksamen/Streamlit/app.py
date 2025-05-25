import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

st.set_page_config(page_title="COVID-19 Analysis", layout="wide")

# Sidebar navigation
menu = st.sidebar.radio("Vælg sektion", ["Introduktion", "Data", "Analyse", "Verdenskort", "HDI", "Konklusion"])

# Indlæs data
df_covid = pd.read_csv("df_covid_cleaned.csv")
df_age = pd.read_csv("df_age_cleaned.csv")
df_health = pd.read_csv("df_health_cleaned.csv")

# INTRODUKTION
if menu == "Introduktion":
    st.title(" Explaining COVID-19 Death Rates Across Countries: The Role of Demographics, Health, and Development")
    st.write("""
    I dette projekt undersøger vi, om sundhedsfaktorer (som diabetes og HDI) har en sammenhæng med COVID-19-smittetal og dødsfald.
    """)


# ANALYSE
elif menu == "Analyse":
    st.title("Analyse: Population vs. Total Cases")
    df_selected = df[['population', 'total_cases']].dropna()

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
    

# VERDENSKORT
elif menu == "Verdenskort":
    st.title("COVID-19 Dødsfald – Verdenskort")

    df_map = df_covid[['location', 'total_deaths']].dropna()
    df_map = df_map[df_map['location'] != 'World']
    df_map.rename(columns={"location": "country"}, inplace=True)

    fig = px.choropleth(
        df_map,
        locations="country",
        locationmode="country names",
        color="total_deaths",
        color_continuous_scale="Reds",
        title="Totale COVID-19 Dødsfald pr. Land"
    )

    fig.update_layout(geo=dict(showframe=False, showcoastlines=False))
    st.plotly_chart(fig, use_container_width=True)

# HDI
elif menu == "HDI":
    st.title("Sammenhæng mellem HDI og COVID-dødsfald")

    merged = pd.merge(df, hdi, left_on="location", right_on="Country", how="inner")
    merged = merged[['location', 'total_deaths', 'HDI']].dropna()

    st.subheader("Tabel over HDI og COVID-19 dødsfald")
    st.write(merged.sort_values(by="HDI", ascending=False))

    st.subheader("Scatterplot: HDI vs. Total Deaths")
    fig2, ax2 = plt.subplots()
    ax2.scatter(merged["HDI"], merged["total_deaths"])
    ax2.set_xlabel("HDI")
    ax2.set_ylabel("Total Deaths")
    st.pyplot(fig2)

# KONKLUSION
elif menu == "Konklusion":
    st.title("Konklusion")
    st.write("""
   This study explored why COVID-19 death rates varied across countries by analyzing demographic, socio-economic, and health-related factors. The goal was not to predict outcomes, but to uncover patterns that explain global differences in mortality.

The most consistent finding was that age-related demographics—especially median age and the proportion of people aged 65+—strongly correlate with higher COVID-19 death rates. This was confirmed through both statistical analysis and classification models, which effectively identified countries at greater risk based on age structure.

Population size, while moderately related to total deaths, had no meaningful link to deaths per capita. This shows that per capita metrics are more useful for comparing severity across countries than raw totals, which can be misleading due to large population sizes.

Contrary to expectations, the Human Development Index (HDI) was not a strong predictor of COVID-19 mortality. Countries with similar HDI scores often had very different death rates, suggesting that HDI does not capture critical pandemic-specific variables like healthcare capacity or policy response.

Health-related factors such as smoking and chronic conditions showed only weak correlations with national death rates. While these increase individual risk, they alone cannot explain country-level outcomes—further emphasizing the role of broader structural and policy-related factors.

In summary, the variation in COVID-19 death rates is best explained by demographic structure, especially aging populations. However, outcomes were also shaped by healthcare capacity, public health interventions, and reporting accuracy. For future pandemics, countries must focus on protecting vulnerable age groups and strengthening health systems, rather than relying solely on general development indicators like HDI.
    """)
