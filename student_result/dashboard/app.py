import streamlit as st

import home
import analytics
import visualization
import prediction
import reports

st.set_page_config(
    page_title="Student Result Analytics",
    page_icon="",
    layout="wide"
)

st.sidebar.title("Student Result Analytics")

page = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "Analytics",
        "Visualization",
        "Prediction",
        "Reports"
    ]
)

if page == "Home":
    home.show()

elif page == "Analytics":
    analytics.show()

elif page == "Visualization":
    visualization.show()

elif page == "Prediction":
    prediction.show()

elif page == "Reports":
    reports.show()