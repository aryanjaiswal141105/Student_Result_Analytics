import streamlit as st


def show_home(df):

    st.title("🎓 Student Result Analytics Dashboard")

    st.markdown("---")

    st.subheader("Project Overview")

    st.write("""
Welcome to the Student Result Analytics Dashboard.

This dashboard allows you to:

• Analyze student performance

• View charts

• Predict Pass/Fail

• Predict Grade

• Predict Total Marks

• Download Reports
""")

    st.markdown("---")

    st.subheader("Dataset Preview")

    st.dataframe(df)