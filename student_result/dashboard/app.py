import streamlit as st

from services.analytics_service import (
    load_dataset,
    total_students,
    total_columns,
    total_departments
)

from dashboard.home import show_home


st.set_page_config(
    page_title="Student Result Analytics",
    page_icon="🎓",
    layout="wide"
)

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.title("Student Result Analytics")

st.sidebar.success("Dashboard Running")

# ----------------------------
# Load Dataset
# ----------------------------

try:

    df = load_dataset()

except Exception as e:

    st.error(f"Dataset Loading Error\n\n{e}")

    st.stop()

# ----------------------------
# Show Home Page
# ----------------------------

show_home(df)

# ----------------------------
# Dashboard Summary
# ----------------------------

st.markdown("---")

st.subheader("Dashboard Summary")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Total Students",
        total_students(df)
    )

with col2:

    st.metric(
        "Columns",
        total_columns(df)
    )

with col3:

    st.metric(
        "Departments",
        total_departments(df)
    )

st.markdown("---")

st.success("Setup is Completed Successfully")