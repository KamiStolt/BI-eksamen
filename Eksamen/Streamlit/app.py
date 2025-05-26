import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="COVID-19 Global Impact",
    page_icon="🦠",
)

# ---- TITLE SECTION ----
st.markdown("<h1 style='text-align: center; color: #6C63FF;'>🌍 Explaining COVID-19 Death Rates Across Countries:</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>The Role of Demographics, Health, and Development</h4>", unsafe_allow_html=True)
st.write("---")

# ---- INTRODUCTION TEXT ----
with st.container():
    st.markdown("### Project Overview")
    st.write("""
    This project explores **why some countries were hit harder by COVID-19 than others**.

    We examine key factors such as:
    - 🧓 Age distribution  
    - 🏥 Health conditions  
    - 🌐 Human Development Index (HDI)  
    - 🧮 Population metrics

    Our goal is to **uncover patterns that can help identify high-risk populations and support better planning for future pandemics.** Behind the data are real people and by understanding what drives the outcomes, we hope to inform smarter and more compassionate public health decisions.
    """)

# ---- TEAM INFO ----
st.markdown("#### Project Members")
st.markdown("""
- **Juvena**
- **Kamilla**
- **Jeanette**
""")


    


