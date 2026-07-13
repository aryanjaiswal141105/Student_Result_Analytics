import streamlit as st
import pandas as pd
import os

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------

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


# -------------------------------------------------
# Analytics Page
# -------------------------------------------------

def show():

    st.title("📊 Student Analytics Dashboard")

    st.markdown("---")

    df = load_dataset()

    if df is None:
        st.error("student_analyzed.csv not found.")
        return

    # -----------------------------------------
    # Required Column Check
    # -----------------------------------------

    required_columns = [
        "Name",
        "Department",
        "Total",
        "Result"
    ]

    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        st.error(
            f"Missing columns in dataset: {', '.join(missing_columns)}"
        )
        return

    # -----------------------------------------
    # Dashboard Cards
    # -----------------------------------------

    total_students = len(df)

    total_departments = df["Department"].nunique()

    pass_students = len(df[df["Result"] == "Pass"])

    fail_students = len(df[df["Result"] == "Fail"])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Students", total_students)
    col2.metric("Departments", total_departments)
    col3.metric("Pass", pass_students)
    col4.metric("Fail", fail_students)

    st.markdown("---")

    # -----------------------------------------
    # Highest Scorer
    # -----------------------------------------

    highest = df.loc[df["Total"].idxmax()]

    st.subheader("🏆 Highest Scorer")

    st.write("Name :", highest["Name"])
    st.write("Department :", highest["Department"])
    st.write("Total Marks :", highest["Total"])

    st.markdown("---")

    # -----------------------------------------
    # Lowest Scorer
    # -----------------------------------------

    lowest = df.loc[df["Total"].idxmin()]

    st.subheader("📉 Lowest Scorer")

    st.write("Name :", lowest["Name"])
    st.write("Department :", lowest["Department"])
    st.write("Total Marks :", lowest["Total"])

    st.markdown("---")

    # -----------------------------------------
    # Class Average
    # -----------------------------------------

    class_average = round(df["Total"].mean(), 2)

    st.subheader("📈 Class Average")

    st.success(class_average)

    st.markdown("---")

    # -----------------------------------------
    # Department Average
    # -----------------------------------------

    st.subheader("🏫 Department-wise Average")

    department_average = (
        df.groupby("Department")["Total"]
        .mean()
        .round(2)
        .reset_index()
    )

    st.dataframe(
        department_average,
        use_container_width=True
    )

    st.markdown("---")

    # -----------------------------------------
    # Top 10 Students
    # -----------------------------------------

    st.subheader("🥇 Top 10 Students")

    top10 = (
        df.sort_values(
            "Total",
            ascending=False
        )
        .head(10)
    )

    st.dataframe(
        top10,
        use_container_width=True
    )

    st.markdown("---")

    # -----------------------------------------
    # Bottom 10 Students
    # -----------------------------------------

    st.subheader("📉 Bottom 10 Students")

    bottom10 = (
        df.sort_values(
            "Total"
        )
        .head(10)
    )

    st.dataframe(
        bottom10,
        use_container_width=True
    )