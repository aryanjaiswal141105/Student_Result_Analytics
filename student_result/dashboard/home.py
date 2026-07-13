import streamlit as st
import pandas as pd
import os

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

def load_dataset():

    current_dir = os.path.dirname(__file__)

    project_dir = os.path.dirname(current_dir)

    csv_path = os.path.join(
        project_dir,
        "data",
        "processed",
        "student_analyzed.csv"
    )

    if os.path.exists(csv_path):

        return pd.read_csv(csv_path)

    return None


# -------------------------------------------------------
# Home Page
# -------------------------------------------------------

def show():

    st.title("Student Result Analytics Dashboard")

    st.markdown("---")

    st.header("Project Overview")

    st.write("""
This project is developed as a Data Analytics and Machine Learning Internship Project.

The dashboard helps analyse students' academic performance,
visualize results,
and predict future performance using Machine Learning.
""")

    st.markdown("---")

    df = load_dataset()

    if df is None:

        st.error("student_analyzed.csv not found.")

        return

    st.header("Project Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Students",
            len(df)
        )

    with col2:

        st.metric(
            "Departments",
            df["Department"].nunique()
        )

    with col3:

        st.metric(
            "Columns",
            len(df.columns)
        )

    st.markdown("---")

    st.header("Dataset Information")

    st.write("Rows :", df.shape[0])

    st.write("Columns :", df.shape[1])

    # st.write("Column Names")

    # st.write(list(df.columns))

    st.markdown("---")

    st.header("Dataset Preview")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.markdown("---")

    st.header("Project Workflow")

    st.code("""
students.csv
        ↓
cleaning.py
        ↓
student_cleaned.csv
        ↓
analysis.py
        ↓
student_analyzed.csv
        ↓
Dashboard
""")

    st.markdown("---")

    st.header("Developer")

    st.success("Aryan Jaiswal & Dattav Shukla")

    st.write("Data Analytics & Machine Learning Internship Project")