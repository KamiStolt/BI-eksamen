import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Sidebar navigation
menu = st.sidebar.radio("Vælg sektion", ["Introduktion", "Data", "Analyse", "Verdenskort", "HDI", "Konklusion"])

# Indlæs data
df = pd.read_csv("owid-covid-latest.csv")
hdi = pd.read_csv("human-development-index.csv", sep=";")  # brug evt sep="," hvis nødvendigt

# INTRODUKTION
if menu == "Introduktion":
    st.title("COVID-19 & Public Health")
    st.write("""
    I dette projekt undersøger vi, om sundhedsfaktorer (som diabetes og HDI) har en sammenhæng med COVID-19-smittetal og dødsfald.
    """)

# DATA
elif menu == "Data":
    st.title("Datasæt")
    st.subheader("COVID-19 Data")
    st.write(df[['location', 'population', 'total_cases', 'total_deaths', 'diabetes_prevalence']].dropna().head())

    st.subheader("Human Development Index (HDI)")
    st.write(hdi.head())

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

    df_map = df[['location', 'total_deaths']].dropna()
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
    Vores analyse viser, at faktorer som sundhed og udviklingsniveau har indflydelse på COVID-19-smitte og dødsfald.
    Der er kun en svag sammenhæng mellem befolkningens størrelse og smittetal, hvilket tyder på at andre faktorer som HDI og sundhedsprofil spiller en større rolle.
    """)
