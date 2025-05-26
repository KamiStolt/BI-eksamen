import streamlit as st

# Page config
st.set_page_config(page_title="Conclusion", page_icon="📌")

# Title
st.title("Conclusion")
st.markdown("---")

# Main body
st.markdown("""
This study explored why COVID-19 death rates varied across countries by analyzing **demographic**, **health**, and **socio-economic** factors. 
The aim was not to predict outcomes, but to uncover patterns that help explain these global differences in mortality.

##### Key Findings

- The most consistent finding was that **age-related demographics** - especially median age and the proportion of people aged 65+ - **strongly correlate** with higher COVID-19 death rates. 
   This was confirmed through both statistical analysis and classification models, which effectively identified countries at greater risk **based on age structure**.

- **Population size**, while moderately related to total deaths, had no meaningful link to deaths per capita. 
   This shows that **per capita metrics** are more useful for comparing severity across countries than raw totals, which can be **misleading** due to large population sizes.


- Contrary to expectations, the **Human Development Index (HDI)**, surprisingly, was **not a strong predicto** of COVID-19 mortality. 
   Countries with similar HDI scores often had very different death rates, suggesting that **HDI does not capture** critical pandemic-specific variables like healthcare capacity or policy response.

- **Health-related** factors such as smoking and chronic conditions showed only **weak correlations** with national death rates. 
   While these increase **individual risk**, they alone cannot explain country-level outcomes—further emphasizing the **role of broader** structural and policy-related factors.

##### Summary

The strongest explanation for differences in COVID-19 death rates lies in **demographics**, especially aging populations. 
However, **healthcare capacity**, **policy response**, and **reporting accuracy** also played key roles.

> For future pandemics, countries must focus on **protecting vulnerable age groups**,  
> strengthening **health systems**, and using **comparable per capita measures** for global analysis.
""")