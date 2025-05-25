import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import seaborn as sns  


# Load datasets
try:
    df_covid = pd.read_csv("df_covid_cleaned.csv")
    df_age = pd.read_csv("df_age_cleaned.csv")
    st.success("Datasets successfully loaded!")
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()


st.title("Data Visualization")

st.write("""This section presents visual insights into the relationships between various demographic, 
        health-related, and socio-economic factors and COVID-19 death rates. Through scatter plots, histograms,
        box plots, and correlation matrices, we explore potential patterns that help us understand which variables 
         may influence the impact of the pandemic across countries.""")


# Menu to jump to section
section = st.selectbox("Jump to section:", [
    "Histograms",
    "Box Plots",
    "Scatter Plots",
    "Correlation Matrix"
])


# Function used in hypothesis 3 for histograms
def visualize_selected_histograms(df):
    """
    Visualizes the distribution of selected numeric columns from df_age_cleaned with histograms.
    """
    selected_cols = [
        'total_deaths_per_million',
        'life_expectancy',
        'median_age',
        'aged_65_older',
        'aged_70_older'
    ]

    n = len(selected_cols)
    n_cols = 3
    n_rows = (n + n_cols - 1) // n_cols 

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(10, 3 * n_rows))
    axes = axes.flatten()

    for i, col in enumerate(selected_cols):
        sns.histplot(df[col], kde=True, ax=axes[i], color='green')
        axes[i].set_title(f'Distribution of {col}')
        axes[i].set_xlabel(col.replace('_', ' ').title())

    # Hide unused axes if any
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    st.pyplot(plt)



if section == "Histograms":
    st.header("Histograms")
    st.write("This section presents histograms that help us understand the distribution of the data and identify any potential outliers or skewness.")
    st.write("") 


    plt.title('Visualizes the distribution of selected numeric columns from df_age_cleaned with histograms')
    visualize_selected_histograms(df_age)
    st.write("The above histograms show the distribution of key variables. Most are right-skewed, especially age-related factors and total deaths per million, while life expectancy appears more normally distributed ") 


elif section == "Box Plots":
    st.header("Box Plots")
    st.write("This section presents box plots that visualize the distribution and highlight potential outliers in COVID-19 death rates and related variables across countries.")
    st.write("") 


    # Total deaths pr milion from hypothesis 1
    df_covid.boxplot(column='total_deaths_per_million')
    plt.title('Outliers in total deaths pr million')
    st.pyplot(plt)
    st.write("""The box plot above shows the distribution of total deaths per million across countries. The outliers indicate a few countries with moderately higher death rates.""")
    st.write("")  
    st.write("") 

    # Total deathsfrom hypothesis 1
    df_covid.boxplot(column='total_deaths') 
    plt.title('Outliers in total deaths')
    st.pyplot(plt)
    st.write("""The box plot above shows the distribution of total deaths across countries. The outliers indicate many extreme values, likely from large countries with high populations.""")



elif section == "Scatter Plots":
    st.header("Scatter Plots")
    st.write("This section presents scatter plots that explore the relationships between key variables and COVID-19 death rates, helping to identify possible trends or correlations across countries.")
    st.write("")  


    # Visualise the features and the response using scatterplots from hypothesis 3
    sns.pairplot(df_age, x_vars=['life_expectancy', 'median_age', 'aged_65_older'], y_vars='total_deaths_per_million', height=5, aspect=1)
    plt.title('Scatterplot')
    st.pyplot(plt)
    st.write("""These scatter plots reveal positive relationships between age-related variables and COVID-19 death rates, indicating that older populations tend to experience higher death rates per million.""")



elif section == "Correlation Matrix":
    st.header("Correlation Matrix")
    st.write("This section presents a correlation matrix that shows the relationships between key variables, helping to identify which factors are most strongly associated with COVID-19 death rates across countries.")
    st.write("") 

    # Correlation matrix from hypothesis 2
    corr_matrix = df_covid[['human_development_index', 'total_deaths_per_million']].corr()
    sns.heatmap(corr_matrix, annot=True)
    st.pyplot(plt)
    st.write("The matrix above shows a moderate positive correlation (0.47) between HDI and COVID-19 deaths per million — contrary to expectations. This suggests HDI alone doesn’t explain the variation in death rates.") 
    st.write("")  
    st.write("")  

    # Correlation matrix from hypothesis 1
    corr_df = df_covid[['population', 'total_deaths', 'total_deaths_per_million']]
    corr_matrix = corr_df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    st.pyplot(plt)
    st.write("The correlation matrix above shows a moderate link between population size and total deaths, but very weak correlation with deaths per million — suggesting population size doesn't strongly affect per capita death rates.") 





