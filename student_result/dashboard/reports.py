import streamlit as st
import pandas as pd
import os

# ---------------------------------------------------
# Project Paths
# ---------------------------------------------------

CURRENT_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.dirname(CURRENT_DIR)

REPORT_FOLDER = os.path.join(
    PROJECT_DIR,
    "outputs",
    "reports"
)

TABLE_FOLDER = os.path.join(
    PROJECT_DIR,
    "outputs",
    "tables"
)

# ---------------------------------------------------
# Read TXT Report
# ---------------------------------------------------

def read_report(filename):

    path = os.path.join(REPORT_FOLDER, filename)

    if os.path.exists(path):

        with open(path, "r", encoding="utf-8") as file:
            return file.read()

    return None


# ---------------------------------------------------
# Read CSV Table
# ---------------------------------------------------

def read_table(filename):

    path = os.path.join(TABLE_FOLDER, filename)

    if os.path.exists(path):

        return pd.read_csv(path)

    return None


# ---------------------------------------------------
# Reports Page
# ---------------------------------------------------

def show():

    st.title("📄 Reports Dashboard")

    st.markdown("---")

    st.header("Project Reports")

    reports = [
        "attendance_summary.txt",
        "final_project_report.txt"
    ]

    for report in reports:

        content = read_report(report)

        st.subheader(report)

        if content:

            st.text_area(
                label=f"Preview - {report}",
                value=content,
                height=200,
                disabled=True
            )

            with open(
                os.path.join(REPORT_FOLDER, report),
                "rb"
            ) as file:

                st.download_button(
                    label=f"⬇ Download {report}",
                    data=file,
                    file_name=report,
                    mime="text/plain"
                )

        else:

            st.warning(f"{report} not found.")

        st.markdown("---")

    st.header("CSV Reports")

    csv_files = [
        "attendance_report.csv",
        "department_report.csv",
        "grade_distribution.csv",
        "low_attendance_students.csv",
        "top10_students.csv"
    ]

    for csv_file in csv_files:

        st.subheader(csv_file)

        table = read_table(csv_file)

        if table is not None:

            st.dataframe(
                table,
                use_container_width=True
            )

            csv = table.to_csv(index=False)

            st.download_button(
                label=f"⬇ Download {csv_file}",
                data=csv,
                file_name=csv_file,
                mime="text/csv"
            )

        else:

            st.warning(f"{csv_file} not found.")

        st.markdown("---")

    st.success("Reports Dashboard Loaded Successfully.")