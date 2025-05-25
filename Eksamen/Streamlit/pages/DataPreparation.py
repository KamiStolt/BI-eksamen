import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Page setup
st.set_page_config(page_title="Data Preparation", page_icon="🧹", layout="wide")
st.title("🧹 Data Preparation")
st.write("This page describes the cleaning and preprocessing steps applied to our COVID-19 dataset.")

# Load datasets
try:
    df_raw = pd.read_csv("owid-covid-latest.csv")
    df_covid = pd.read_csv("df_covid_cleaned.csv")
    df_age = pd.read_csv("df_age_cleaned.csv")
    df_health = pd.read_csv("df_health_cleaned.csv")
    st.success("Datasets successfully loaded!")
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Section: Summary of steps
st.markdown("#### Step-by-Step Cleaning Summary")
st.markdown("""
1. **Remove irrelevant aggregate data**  
   - Excluded OWID aggregates like `OWID_WRL`, `OWID_UMC`, etc.

2. **Remove empty columns**  
   - Dropped columns with only missing values.

3. **Separate datasets by data level**  
   - Age-related variables (e.g. `median_age`) stored in `df_age`.  
   - Health indicators (e.g. `cardiovascular_death_rate`) stored in `df_health`.  
   - Core country-level data retained in `df_covid`.

4. **Handle missing values**  
   - Dropped rows with missing `median_age` or `female_smokers`.  
   - Median imputation for others like `aged_70_older`.

5. **Match and merge HDI data**  
   - Joined HDI values using a country name mapping (e.g. Greenland → Denmark).  
   - Filled missing HDI values where necessary.
            
6. **Replace remaining missing values**
    - Used a combination of direct values (e.g. manually imputed for Nauru and Somalia) and imputing with median values for others.

7. **Final cleanup**  
   - Removed helper columns like `Entity`, `hdi_source_country`.  
   - Removed duplicates.
""")

# Section: Raw Dataset
st.markdown("#### Raw Dataset Samples")
st.write("**Raw Dataset**")
st.dataframe(df_raw.head(10))

# Section: Dataset Snapshots
st.markdown("#### Cleaned Dataset Samples")
tab1, tab2, tab3 = st.tabs(["Country-Level", "Age-Level", "Health-Level"])

with tab1:
    st.write("**Covid-level Dataset**")
    st.dataframe(df_covid.head(10))

with tab2:
    st.write("**Age-level Dataset**")
    st.dataframe(df_age.head(10))

with tab3:
    st.write("**Health-level Dataset**")
    st.dataframe(df_health.head(10))

# Section: Dataset Sizes
st.markdown("### Dataset Sizes")
col1, col2, col3 = st.columns(3)
col1.metric("Country-Level", f"{df_covid.shape[0]} rows")
col2.metric("Age-Level", f"{df_age.shape[0]} rows")
col3.metric("Health-Level", f"{df_health.shape[0]} rows")

# Section: Missing Value Overview
total_cols = df_raw.shape[1]
empty_cols = (df_raw.isnull().sum() == df_raw.shape[0]).sum()
some_data_cols = total_cols - empty_cols
high_missing_cols = (df_raw.isnull().mean() > 0.5).sum()

st.markdown(f"""
Missing Value Overview (Raw Dataset):
- **Total columns:** {total_cols}  
- **Columns with no data:** {empty_cols}  
- **Columns with some data:** {some_data_cols}  
- **Columns with >50% missing data:** {high_missing_cols}  
""")

# Section: Missing Value Visualization
missing_percent = df_raw.isnull().mean() * 100
missing_percent = missing_percent[(missing_percent > 0) & (missing_percent < 100)].sort_values(ascending=False)

df_missing = pd.DataFrame({
    "Column": missing_percent.index,
    "MissingPercent": missing_percent.values
})

fig = px.bar(
    df_missing,
    x="Column",
    y="MissingPercent",
    labels={"Column": "Columns", "MissingPercent": "Missing Data (%)"},
    title="Percentage of Missing Data by Column (Excluding Empty Columns)"
)
fig.update_layout(xaxis_tickangle=45)
st.plotly_chart(fig)

# Section: Key Features Explained
st.markdown("#### Some Key Features Explained")
feature_info = pd.DataFrame({
    "Feature": [
        "total_deaths", "total_deaths_per_million", "population",
        "median_age", "aged_65_older", "female_smokers",
        "diabetes_prevalence", "life_expectancy", "human_development_index"
    ],
    "Description": [
        "Cumulative confirmed COVID-19 deaths per country.",
        "Deaths per million people — allows fair comparison between countries of different sizes.",
        "Population size of the country.",
        "Median age of the population.",
        "Percentage of the population aged 65 or older.",
        "Percentage of female smokers in the population.",
        "Prevalence of diabetes in the adult population.",
        "Average number of years a person is expected to live.",
        "Human Development Index — a composite of life expectancy, education, and income."
    ]
})
st.dataframe(feature_info, use_container_width=True)

# Section: Dataset Reduction Overview
st.markdown("#### Dataset Reduction Overview")

# Compute row differences
reduction_data = {
    "Dataset": ["Country-Level", "Age-Level", "Health-Level"],
    "Rows Removed": [
        df_raw.shape[0] - df_covid.shape[0],
        df_raw.shape[0] - df_age.shape[0],
        df_raw.shape[0] - df_health.shape[0]
    ],
    "Remaining Rows": [
        df_covid.shape[0],
        df_age.shape[0],
        df_health.shape[0]
    ]
}

reduction_df = pd.DataFrame(reduction_data)

# Display as a table
st.table(reduction_df)

# Section: Final Readiness Checklist
st.markdown("#### Dataset Readiness Checklist")
st.markdown("""
- No fully empty columns  
- Checked for duplicate rows  
- Aggregates (like OWID_WRL) removed  
- Key features cleaned and retained  
- Missing values handled  
- HDI and demographic data merged  
""")

st.markdown("""
<div style='text-align: center; font-size: 20px; font-weight: bold; color: green;'>
Data preparation complete! Cleaned datasets are ready for modeling and analysis.
</div>
""", unsafe_allow_html=True)