# import library

import streamlit as st
from web_function import load_data

from Tabs import home, predict, visualise

Tabs = {
    "Home" : home,
    "Prediction" : predict,
    "Visualisation" : visualise
}

# membuat sidebar
st.sidebar.title("Navigasi")

# membuat radio option
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# load dataset
aids_df, x, y = load_data

# kondisi call app function
if page in ["Prediction", "visualitation"]:
    Tabs[page].app(aids_df, x, y)
else:
    Tabs[page].app()
