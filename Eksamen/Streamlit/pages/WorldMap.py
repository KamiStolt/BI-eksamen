import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="COVID-19 Global Maps")
st.title("COVID-19 WorldMap")
st.markdown("""
Welcome to this interactive COVID-19 global dashboard! 
Here, you can explore how different demographic, health, and development factors relate to the impact of COVID-19 across countries.  
By visualizing data such as death tolls, age structure, life expectancy, and health indicators, this tool aims to reveal patterns that can help understand the pandemic's diverse effects worldwide.  
Use the dropdown menu to select different metrics and discover key insights that may inform public health strategies and preparedness for future outbreaks.
""")

# Load datasets
try:
    df_covid = pd.read_csv("df_covid_cleaned.csv")
    df_age = pd.read_csv("df_age_cleaned.csv")
    df_health = pd.read_csv("df_health_cleaned.csv")
    st.success("Datasets successfully loaded!")
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Rename location columns for consistency
df_covid = df_covid.rename(columns={"location": "Country"})
df_age = df_age.rename(columns={"location": "Country"})
df_health = df_health.rename(columns={"location": "Country"})

# Remove 'World' aggregate from all
df_covid = df_covid[df_covid["Country"] != "World"]
df_age = df_age[df_age["Country"] != "World"]
df_health = df_health[df_health["Country"] != "World"]

# Metric options: mapping metric name to (dataset, column(s))
metric_options = {
    "Total Deaths": ("df_covid", "total_deaths"),
    "Deaths per Million": ("df_covid", "total_deaths_per_million"),
    "Life Expectancy": ("df_age", "life_expectancy"),
    "Human Development Index (HDI)": ("df_covid", "human_development_index"),
    "Aged 65 and Older (%)": ("df_age", "aged_65_older"),
    "Cardiovascular Death Rate": ("df_health", "cardiovasc_death_rate"),
    "Smokers (Avg %)": ("df_health", ["female_smokers", "male_smokers"])
}

# User selects metric to visualize
selected_label = st.selectbox("Select a metric to visualize on the world map:", list(metric_options.keys()))
dataset_key, column_name = metric_options[selected_label]

# Select and prepare correct dataframe
if dataset_key == "df_covid":
    df = df_covid[["Country", column_name]].dropna()
    column_to_plot = column_name
elif dataset_key == "df_age":
    df = df_age[["Country", column_name]].dropna()
    column_to_plot = column_name
else:  # df_health
    if isinstance(column_name, list):
        df = df_health[["Country"] + column_name].dropna()
        df["Smokers (Avg %)"] = df[column_name].mean(axis=1)
        column_to_plot = "Smokers (Avg %)"
    else:
        df = df_health[["Country", column_name]].dropna()
        column_to_plot = column_name

# Rename column for display purposes
df = df.rename(columns={column_to_plot: selected_label})

# Create the choropleth map
fig = px.choropleth(
    df,
    locations="Country",
    locationmode="country names",
    color=selected_label,
    hover_name="Country",
    hover_data={selected_label: True},
    color_continuous_scale="Plasma",
    title=f"{selected_label} by Country"
)

fig.update_layout(
    geo=dict(showframe=False, showcoastlines=False),
    margin=dict(t=40, b=0, l=0, r=0),
    coloraxis_colorbar=dict(title=selected_label)
)

# Display the map
st.plotly_chart(fig, use_container_width=True)

# Info text for each metric
info_texts = {
    "Total Deaths": (
        "The total number of confirmed COVID-19 deaths in each country. "
        "This raw count reflects the overall impact but can be misleading without considering population size, "
        "as larger countries naturally tend to have higher total deaths."
    ),
    "Deaths per Million": (
        "Number of COVID-19 deaths per one million people in each country. "
        "This normalized metric allows fair comparisons between countries of different sizes, "
        "highlighting the relative severity of the pandemic’s impact."
    ),
    "Life Expectancy": (
        "Average number of years a person is expected to live in a country, "
        "which is an indicator of overall population health, quality of healthcare, and living conditions."
    ),
    "Human Development Index (HDI)": (
        "A composite index measuring average achievement in key dimensions of human development: "
        "health (life expectancy), education, and standard of living. "
        "Higher HDI generally suggests better social and economic conditions."
    ),
    "Aged 65 and Older (%)": (
        "The percentage of a country’s population aged 65 and above. "
        "Older populations are more vulnerable to COVID-19, so this metric is crucial to understanding risk."
    ),
    "Cardiovascular Death Rate": (
        "The rate of deaths caused by cardiovascular diseases per 100,000 people. "
        "Cardiovascular conditions can increase vulnerability to severe COVID-19 outcomes."
    ),
    "Smokers (Avg %)": (
        "The average percentage of male and female smokers in the population. "
        "Smoking affects lung health and immune response, which may impact COVID-19 severity."
    )
}

# Expandable section for additional information
with st.expander("What does this map tell us?", expanded=False):
    st.markdown(f"- {info_texts.get(selected_label, '')}")