import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os



# Indlæs data
df_covid = pd.read_csv("df_covid_cleaned.csv")
df_age = pd.read_csv("df_age_cleaned.csv")
df_health = pd.read_csv("df_health_cleaned.csv")

# st.write("Available columns:", df_covid.columns.tolist())


# DATAMODELLING
menu = "Data Modeling"  
st.title("Data Modeling")
st.write("""
Data modelling is used to understand and quantify relationships between variables in a dataset. 
In this project, we use regression models to identify which factors (such as health or demographics) can help explain the differences in COVID-19 death rates across countries. 
This helps us uncover meaningful patterns and test hypotheses.
""")

st.markdown("### Independent Variables (Features)")
st.write("""
We selected the following independent variables based on their potential link to COVID-19 mortality:
- **cardiovascular_death_rate** – Death rate from cardiovascular disease
- **diabetes_prevalence** – Percentage of population with diabetes
- **female_smokers** – Percentage of female smokers
- **male_smokers** – Percentage of male smokers
- **median_age** – Median age of the population
- **aged_65_older** – Share of population aged 65+
- **aged_70_older** – Share of population aged 70+
- **life_expectancy** – Average life expectancy
- **human_development_index** – UN score for development level

These features were tested against the target variable:
- **total_deaths_per_million** – COVID-19 deaths per million people
- **total_deaths** – Total COVID-19 deaths
- **population** – Total population
""")

#Menu til at vælge sektion,
section = st.selectbox("Jump to section:", [
    "Hypotese 1", 
    "Hypotese 2", 
    "Hypotese 3",
    "Hypotese 4" 
])

#Indhold vises baseret på valg,
if section == "Hypotese 1": 
    st.header("Hypotese 1") 
    st.write("Linear regression is a statistical method used to analyze the relationship between an independent variable (population) and a dependent variable (number of deaths). The model tries to find the best-fitting straight line that can predict the value of the dependent variable based on the input.")
    # Independent variable
    X = df_covid['population'].values.reshape(-1, 1) # Uafhængig variabel
# Dependent variable
    y = df_covid['total_deaths'].values.reshape(-1, 1) # Afhængig variabel

# Train-test split for the regression model for total deaths
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=123, test_size=0.15) 


# Creating an instance of Linear Regression model
    myreg = LinearRegression()

# Fit it to our data for total_deaths
    myreg.fit(X_train, y_train)
    myreg


# Get the calculated coefficients
    a = myreg.coef_
    b = myreg.intercept_

    y_predicted = myreg.predict(X_test)


    # Visualise the Linear Regression 
    fig1, ax1 = plt.subplots()
    ax1.set_title('Linear Regression: Population vs Total Deaths')
    ax1.scatter(X, y, color='green')
    ax1.plot(X_train, a*X_train + b, color='blue')
    ax1.plot(X_test, y_predicted, color='orange')
    ax1.set_xlabel('Population')
    ax1.set_ylabel('Total Deaths')
    st.pyplot(fig1)
    st.write("This graph shows a weak positive linear relationship between population size and total COVID-19 deaths. Although countries with larger populations tend to have more deaths, the wide spread of data points indicates that population alone does not strongly predict total deaths.")


# Independent variable
    X2 = df_covid['population'].values.reshape(-1, 1) # Uafhængig variabel
# Dependent variable
    y2 = df_covid['total_deaths_per_million'].values.reshape(-1, 1) # Afhængig variabel

# Train-test split for the regression model for total deaths per million
    X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, random_state=123, test_size=0.15) 

    myreg2 = LinearRegression()
    myreg2.fit(X2_train, y2_train)
    myreg2

    a2 = myreg2.coef_
    b2 = myreg2.intercept_

    y2_predicted = myreg2.predict(X2_test)

    # Visualise the Linear Regression 
    fig2, ax2 = plt.subplots()
    ax2.set_title('Linear Regression: Population vs Total Deaths per Million')
    ax2.scatter(X2, y2, color='green')
    ax2.plot(X2_train, a2*X2_train + b2, color='blue')
    ax2.plot(X2_test, y2_predicted, color='orange')
    ax2.set_xlabel('Population')
    ax2.set_ylabel('Total Deaths per Million')
    st.pyplot(fig2)
    st.write("The graph shows a nearly flat or slightly negative trend between population size and deaths per million, indicating that there is no strong relationship between the two. This supports the hypothesis that countries with larger populations do not necessarily have higher COVID-19 death rates per capita.")


    # Predict age from length for first model
    death_predicted = myreg.predict([[170]])

    # Predict age from length for second model
    death_predicted2 = myreg2.predict([[170]])

    # For model 1: Population vs Total Deaths
    X = df_covid[['population']]       
    y = df_covid['total_deaths']   

    # For model 2: Population vs Total Deaths per million
    X2 = df_covid[['population']]       
    y2 = df_covid['total_deaths_per_million']    
    # Create and train a model for population vs total deaths
    model = LinearRegression()
    model.fit(X, y)

    # Create and train a model for population vs total deaths pr million
    model2 = LinearRegression()
    model2.fit(X, y)

    # Calculate the R-squared value for the first model
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)

    # Calculate the R-squared value for the second model
    y_pred2 = model2.predict(X)
    r2 = r2_score(y2, y_pred2)

    fig3, ax3 = plt.subplots()
    ax3.scatter(X, y, color='blue', label='Actual data')
    ax3.plot(X, y_pred, color='red', label='Linear regression')
    ax3.set_xlabel('Population')
    ax3.set_ylabel('Total Deaths')
    ax3.set_title('Linear Regression: Population vs Total Deaths')
    ax3.legend()
    st.pyplot(fig3)

    st.write("The regression line between population and total deaths shows a very weak relationship (R² ≈ 0.0049), meaning that population size explains less than 1% of the variation in COVID-19 deaths across countries. This indicates that other factors play a much more significant role.")


    fig4, ax4 = plt.subplots()
    ax4.scatter(X2, y2, color='blue', label='Actual data')
    ax4.plot(X2, y_pred2, color='red', label='Linear regression')
    ax4.set_xlabel('Population')
    ax4.set_ylabel('Total Deaths per million')
    ax4.set_title('Linear Regression: Population vs Total Deaths per million')
    ax4.legend()
    st.pyplot(fig4)

    st.write("This plot examines the relationship between population size and COVID-19 deaths per million. Despite the upward regression line caused by outliers, the data points are mostly concentrated at the bottom, suggesting no clear correlation. This supports the idea that population size alone does not predict per capita death rates.")



elif section == "Hypotese 2": 
    st.header("Hypotese 2") 
    
    # independent
    X = df_covid[['human_development_index']]

    # dependent
    y = df_covid[['total_deaths_per_million']]

    # X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=123, test_size=0.20)

    myreg = LinearRegression()
    # Fit it to our data
    myreg.fit(X_train, y_train)
    myreg

    a = myreg.coef_
    b = myreg.intercept_

    y_predicted = myreg.predict(X_test)

    plt.title('Linear Regression: HDI vs COVID-19 Deaths per Million')
    plt.scatter(X, y, color='green')
    plt.plot(X_train, a*X_train + b, color='blue')
    plt.plot(X_test, y_predicted, color='orange')
    plt.xlabel('HDI')
    plt.ylabel('Deaths per Million')
    st.pyplot(plt)


    st.write("This graph shows a weak positive trend between Human Development Index (HDI) and COVID-19 deaths per million, but the wide spread of data points suggests the relationship is not very strong.")

    # Her kan du tilføje diagrammer
 
elif section == "Hypotese 3": 
    st.header("Hypotese 3") 
    st.write("The purpose of multiple linear regression is to model the relationship between one dependent variable and two or more independent variables. It helps identify how each predictor contributes to the outcome while controlling for the influence of other variables. This technique is useful for understanding which factors have the strongest impact and for making informed predictions.")
    
    # Create a Python list of feature names
    feature_cols = ['life_expectancy', 'median_age', 'aged_65_older']

    # Use the list to select a subset of the original DataFrame
    X = df_age[feature_cols]

    # Select a Series from the DataFrame for y
    y = df_age['total_deaths_per_million']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    # Create a model
    linreg = LinearRegression()

# Fit the model to our training data
    linreg.fit(X_train, y_train)
    # Make predictions on the testing set
    y_predicted = linreg.predict(X_test)


    fig5, ax5 = plt.subplots()
    ax5.set_title('Multiple Linear Regression')
    ax5.scatter(y_test, y_predicted, color='green', label='Predicted vs Actual')
    ax5.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--', label='Perfect Prediction')
    ax5.set_xlabel('Actual Values')
    ax5.set_ylabel('Predicted Values')
    ax5.legend()
    st.pyplot(fig5)

    st.write("The model shows a clear correlation between age-related factors and COVID-19 death rates. It explains a large part of the variation across countries, but moderate errors (MAE and RMSE) indicate that other factors also play a role. Therefore, the model is useful for identifying overall trends – but not for making precise predictions.")


    image = Image.open("../Data/DecisionTree.png")
    st.image(image, caption="Decision Tree Visualization", use_column_width=True)
    st.write("The decision tree, using demographic features, achieved 70% accuracy and revealed life expectancy as the key factor in predicting COVID-19 death rate categories.")



elif section == "Hypotese 4": 
    st.header("Hypotese 4") 
    st.write("The purpose of multiple linear regression is to model the relationship between one dependent variable and two or more independent variables. It helps identify how each predictor contributes to the outcome while controlling for the influence of other variables. This technique is useful for understanding which factors have the strongest impact and for making informed predictions.")



    # Create a list of the features names
    feature_cols = ['cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers', 'male_smokers']
    

# Select only the relevant predictor variables (independent) from the dataframe
    X = df_health[feature_cols]
    y = df_health['total_deaths_per_million']

    # Splitting X and y into Training and Testing Sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=123, test_size=0.20)

    linreg = LinearRegression()
    

    # Fit the model to our training data
    linreg.fit(X_train, y_train)
    linreg

    # Make predictions on the testing set
    y_predicted = linreg.predict(X_test)


    plt.title('Multiple Linear Regression')
    plt.scatter(y_test, y_predicted, color='green', label='Predicted vs Actual')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--', label='Perfect Prediction')
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    st.pyplot(plt)
    # Her kan du tilføje diagrammer

    st.write("The green dots show actual COVID-19 death rates by country, while the y-axis shows model predictions. The red dashed line indicates perfect prediction. Since many dots deviate from this line—especially at higher values—it shows that the model struggles to accurately capture the true death rates based on the selected health features.")






