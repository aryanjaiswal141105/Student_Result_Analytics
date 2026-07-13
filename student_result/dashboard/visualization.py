import streamlit as st
import os

# --------------------------------------------------
# Get Project Folder
# --------------------------------------------------

CURRENT_DIR = os.path.dirname(__file__)

PROJECT_DIR = os.path.dirname(CURRENT_DIR)

GRAPH_FOLDER = os.path.join(
    PROJECT_DIR,
    "outputs",
    "graphs"
)

# --------------------------------------------------
# Function to Display Graph
# --------------------------------------------------

def show_graph(title, filename):

    path = os.path.join(GRAPH_FOLDER, filename)

    st.subheader(title)

    if os.path.exists(path):

        st.image(
            path,
            use_container_width=True
        )

    else:

        st.warning(f"{filename} not found.")

    st.markdown("---")


# --------------------------------------------------
# Visualization Page
# --------------------------------------------------

def show():

    st.title("📈 Visualization Dashboard")

    st.write(
        "All charts were generated in Phase 5 and are displayed below."
    )

    st.markdown("---")

    # -----------------------------------------

    show_graph(
        "📊 Department Average",
        "bar_department_average.png"
    )

    # -----------------------------------------

    show_graph(
        "🥧 Grade Distribution",
        "pie_grade_distribution.png"
    )

    # -----------------------------------------

    show_graph(
        "📈 Average Marks Histogram",
        "histogram_average_marks.png"
    )

    # -----------------------------------------

    show_graph(
        "📉 Student Marks Line Chart",
        "line_student_marks.png"
    )

    # -----------------------------------------

    show_graph(
        "📦 Department Marks Box Plot",
        "boxplot_department_marks.png"
    )

    # -----------------------------------------

    show_graph(
        "📊 Attendance Bar Chart",
        "attendance_bar_chart.png"
    )

    # -----------------------------------------

    show_graph(
        "📊 Attendance Chart",
        "attendance_chart.png"
    )

    # -----------------------------------------

    show_graph(
        "🏫 Department Average",
        "department_average.png"
    )

    # -----------------------------------------

    show_graph(
        "🏫 Department Students",
        "department_students.png"
    )

    # -----------------------------------------

    show_graph(
        "🎓 Grade Distribution",
        "grade_distribution.png"
    )