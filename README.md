# BI-eksamen
## **Title of the project:** Explaining COVID-19 Death Rates Across Countries: The Role of Demographics, Health, and Development

---

**Course:** Business Intelligence 

**Group:** Group 7

**Group Members:** Kamilla, Juvena og Jeanette

---

**Motivation**

The COVID-19 pandemic affected countries differently, and this sparked our curiosity: why did some nations experience far higher death rates than others? Was it just about wealth and healthcare, or also about deeper factors like age, population size, and health conditions?

We chose this topic because it combines data with real human impact. Our goal was to understand what contributed to the differences in death tolls, so we can help inform better protection for vulnerable groups in future pandemics.

This project allowed us to use our analytical skills to explore something meaningful, reminding us that behind every number is a life.

---

**Problem Statement**

What key demographic, health-related, and socio-economic factors best explain the variation in COVID-19 death rates across countries? 

Specifically, how do variables such as population size, age distribution, existing health conditions and the Human Development Index (HDI) contribute to differences in total and per capita COVID-19 deaths?  

---

**Purpose**

The goal of this project is to identify key factors that help explain why some countries experienced higher COVID-19 death rates than others. By analyzing variables like age, population size, existing health conditions, and socio-economic development, we aim to highlight patterns that could support better protection of high-risk populations and improve planning for future pandemics.

---

**Hypotheses**

1. Higher population size is associated with higher total COVID-19 deaths, but not necessarily with higher deaths per capita. 

2. Countries with a higher Human Development Index (HDI) have experienced lower COVID-19 death rates per capita. 

3. Countries with a higher life expectancy and older populations (e.g. higher median age, % aged 65+, etc.) have experienced higher COVID-19 death rates.

4. Countries with higher prevalence of chronic health conditions (e.g. cardiovascular death rate, diabetes, smoking) have higher COVID-19 death rates

---

**A brief annotation of our project, explaining:** 

- which challenge you would like to address? 
- why is this challenge important or interesting research goal? 
- what is the expected solution your project would provide? 
- what would be the positive impact of the solution, which category of users could benefit from it? 

We aim to investigate which demographic, health-related, and socio-economic factors best explain differences in COVID-19 death rates across countries. This is important to understand why some countries were more affected than others and to improve future pandemic preparedness. By analyzing factors like population size, age, health conditions, and HDI, we hope to identify key patterns. The findings could help governments and health organizations protect vulnerable populations and plan better responses.

---

**Running the Streamlit App**

To run the Streamlit dashboard locally, follow these steps:

Open Anaconda Navigator Launch Anaconda and open VSCode from within Anaconda.

Navigate to the Streamlit Folder In VSCode, open a terminal and make sure you're in the Streamlit directory of the project.


Install Required Packages In the terminal, run the following command to install all necessary packages:

pip install streamlit

pip install plotly

pip install scikit-learn

pip install matplotlib

python -m pip install seaborn


Once dependencies are installed, launch the app with:

streamlit run app.py

This will open a local Streamlit web app in your browser.