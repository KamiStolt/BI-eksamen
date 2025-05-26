import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, explained_variance_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load datasets
df_covid = pd.read_csv("df_covid_cleaned.csv")
df_age = pd.read_csv("df_age_cleaned.csv")
df_health = pd.read_csv("df_health_cleaned.csv")

# Page title and introduction
st.title("Data Modeling: COVID-19 Mortality Analysis")
st.write("""
This section focuses on using regression models to analyze the relationships between various demographic and health-related features and COVID-19 mortality rates. Our goal is to uncover patterns and evaluate hypotheses about the factors influencing pandemic outcomes across countries.
""")

# Feature explanation
st.markdown("### Selected Features")
st.write("""
We explore the following predictors for their potential to explain COVID-19 death rates:

**Demographic Features:**
- `median_age`, `aged_65_older`, `aged_70_older`

**Health Features:**
- `cardiovasc_death_rate`, `diabetes_prevalence`, `female_smokers`, `male_smokers`

**Other Predictors:**
- `life_expectancy`, `human_development_index`, `population`

**Target Variables:**
- `total_deaths`, `total_deaths_per_million`
""")

# Section selector
section = st.selectbox("Choose a Hypothesis to Explore:", [
    "Hypothesis 1: Population vs COVID-19 Deaths",
    "Hypothesis 2: HDI vs COVID-19 Deaths",
    "Hypothesis 3: Age Factors",
    "Hypothesis 4: Health Risk Factors"
])

# ---------------------- Hypothesis 1 ----------------------
if section == "Hypothesis 1: Population vs COVID-19 Deaths":
    st.header("Hypothesis 1: Population Size and COVID-19 Deaths")
    st.write("Linear regression is a statistical method used to analyze the relationship between an independent variable (population) and a dependent variable (number of deaths). The model tries to find the best-fitting straight line that can predict the value of the dependent variable based on the input.")

    st.subheader("Model 1: Total Deaths")
    X = df_covid[['population']]
    y = df_covid[['total_deaths']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=123)
    model1 = LinearRegression().fit(X_train, y_train)
    y_pred = model1.predict(X_test)

    fig1, ax1 = plt.subplots()
    ax1.scatter(X, y, color='green')
    ax1.plot(X, model1.predict(X), color='blue')
    ax1.set_title("Population vs Total Deaths")
    ax1.set_xlabel("Population")
    ax1.set_ylabel("Total Deaths")
    st.pyplot(fig1)

    st.markdown(f"""
    **Equation:** y = {model1.coef_[0][0]:.6f} * x + {model1.intercept_[0]:.2f}  
    **Prediction for x=170:** {model1.predict([[170]])[0][0]:.2f} deaths  
    **R²:** {r2_score(y_test, y_pred):.4f}  
    **MSE:** {mean_squared_error(y_test, y_pred):,.2f}  
    **Explained Variance:** {explained_variance_score(y_test, y_pred):.2f}
    """)

    st.write("The regression line between population and total deaths shows a very weak relationship (R² ≈ 0.0049), meaning that population size explains less than 1% of the variation in COVID-19 deaths across countries. This indicates that other factors play a much more significant role.")


    st.subheader("Model 2: Deaths per Million")
    y2 = df_covid[['total_deaths_per_million']]
    X_train2, X_test2, y_train2, y_test2 = train_test_split(X, y2, test_size=0.15, random_state=123)
    model2 = LinearRegression().fit(X_train2, y_train2)
    y_pred2 = model2.predict(X_test2)

    fig2, ax2 = plt.subplots()
    ax2.scatter(X, y2, color='green')
    ax2.plot(X, model2.predict(X), color='blue')
    ax2.set_title("Population vs Deaths per Million")
    ax2.set_xlabel("Population")
    ax2.set_ylabel("Deaths per Million")
    st.pyplot(fig2)

    st.markdown(f"""
    **Equation:** y = {model2.coef_[0][0]:.8f} * x + {model2.intercept_[0]:.2f}  
    **Prediction for x=170:** {model2.predict([[170]])[0][0]:.2f} deaths/million  
    **R²:** {r2_score(y_test2, y_pred2):.4f}  
    **MSE:** {mean_squared_error(y_test2, y_pred2):,.2f}  
    **Explained Variance:** {explained_variance_score(y_test2, y_pred2):.2f}
    """)
    
    st.write("This plot examines the relationship between population size and COVID-19 deaths per million. Despite the upward regression line caused by outliers, the data points are mostly concentrated at the bottom, suggesting no clear correlation. This supports the idea that population size alone does not predict per capita death rates.")

# ---------------------- Hypothesis 2 ----------------------
elif section == "Hypothesis 2: HDI vs COVID-19 Deaths":
    st.header("Hypothesis 2: Human Development Index and Deaths per Million")
    st.write("Linear regression is a statistical method used to analyze the relationship between an independent variable (population) and a dependent variable (number of deaths). The model tries to find the best-fitting straight line that can predict the value of the dependent variable based on the input.")

    X = df_covid[['human_development_index']]
    y = df_covid[['total_deaths_per_million']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

    model = LinearRegression().fit(X_train, y_train)
    y_pred = model.predict(X_test)

    fig, ax = plt.subplots()
    ax.scatter(X, y, color='green')
    ax.plot(X, model.predict(X), color='blue')
    ax.set_title("HDI vs Deaths per Million")
    ax.set_xlabel("HDI")
    ax.set_ylabel("Deaths per Million")
    st.pyplot(fig)

    st.markdown(f"""
    **Equation:** y = {model.coef_[0][0]:.2f} * x + {model.intercept_[0]:.2f}  
    **MAE:** {mean_absolute_error(y_test, y_pred):.2f}  
    **MSE:** {mean_squared_error(y_test, y_pred):.2f}  
    **RMSE:** {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}  
    **R²:** {r2_score(y_test, y_pred):.4f}
    """)

    st.write("This graph shows a weak positive trend between Human Development Index (HDI) and COVID-19 deaths per million, but the wide spread of data points suggests the relationship is not very strong.")

# ---------------------- Hypothesis 3 ----------------------
elif section == "Hypothesis 3: Age Factors":
    st.header("Hypothesis 3: Age-related Factors")
    st.write("The purpose of multiple linear regression is to model the relationship between one dependent variable and two or more independent variables. It helps identify how each predictor contributes to the outcome while controlling for the influence of other variables. This technique is useful for understanding which factors have the strongest impact and for making informed predictions.")

    feature_cols = ['life_expectancy', 'median_age', 'aged_65_older']
    X = df_age[feature_cols]
    y = df_age['total_deaths_per_million']
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    model = LinearRegression().fit(X_train, y_train)
    y_pred = model.predict(X_test)

    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred, color='green', label='Predicted vs Actual')
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', label='Perfect Prediction')
    ax.set_xlabel('Actual')
    ax.set_ylabel('Predicted')
    ax.set_title('Multiple Linear Regression: Age Factors')
    ax.legend()
    st.pyplot(fig)

    st.markdown(f"""
    **Intercept (b0):** {model.intercept_:.2f}  
    **MAE:** {mean_absolute_error(y_test, y_pred):.2f}  
    **MSE:** {mean_squared_error(y_test, y_pred):.2f}  
    **RMSE:** {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}  
    **R²:** {r2_score(y_test, y_pred):.4f}  
    **Explained Variance:** {explained_variance_score(y_test, y_pred):.2f}
    """)

    st.write("The model shows a clear correlation between age-related factors and COVID-19 death rates. It explains a large part of the variation across countries, but moderate errors (MAE and RMSE) indicate that other factors also play a role. Therefore, the model is useful for identifying overall trends – but not for making precise predictions.")

    st.subheader("Decision Tree")
    st.image("../Data/DecisionTree.png", caption="Decision Tree Visualization", use_column_width=True)
    st.write("Decision Tree Accuracy: 70%. Life expectancy emerged as the top predictor among age-related features.")
    st.write("The decision tree, using demographic features, achieved 70% accuracy and revealed life expectancy as the key factor in predicting COVID-19 death rate categories.")

# ---------------------- Hypothesis 4 ----------------------
elif section == "Hypothesis 4: Health Risk Factors":
    st.header("Hypothesis 4: Health Risk Factors")
    st.write("The purpose of multiple linear regression is to model the relationship between one dependent variable and two or more independent variables. It helps identify how each predictor contributes to the outcome while controlling for the influence of other variables. This technique is useful for understanding which factors have the strongest impact and for making informed predictions.")

    feature_cols = ['cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers', 'male_smokers']
    X = df_health[feature_cols]
    y = df_health['total_deaths_per_million']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=123)
    model = LinearRegression().fit(X_train, y_train)
    y_pred = model.predict(X_test)

    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred, color='green', label='Predicted vs Actual')
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', label='Perfect Prediction')
    ax.set_xlabel('Actual')
    ax.set_ylabel('Predicted')
    ax.set_title('Multiple Linear Regression: Health Factors')
    ax.legend()
    st.pyplot(fig)

    coef_list = list(zip(feature_cols, model.coef_.flatten()))
    
    st.markdown(f"""
    **Intercept (b0):** {model.intercept_:.2f}  
    **MAE:** {mean_absolute_error(y_test, y_pred):.2f}  
    **MSE:** {mean_squared_error(y_test, y_pred):.2f}  
    **RMSE:** {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}  
    **R²:** {r2_score(y_test, y_pred):.4f}  
    **Explained Variance:** {explained_variance_score(y_test, y_pred):.2f}
    """)

    st.write("The green dots show actual COVID-19 death rates by country, while the y-axis shows model predictions. The red dashed line indicates perfect prediction. Since many dots deviate from this line—especially at higher values—it shows that the model struggles to accurately capture the true death rates based on the selected health features.")






