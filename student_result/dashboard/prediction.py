import streamlit as st
import joblib
import pandas as pd
import os

# ----------------------------------------------------
# Locate Models
# ----------------------------------------------------

CURRENT_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.dirname(CURRENT_DIR)

MODEL_FOLDER = os.path.join(
    PROJECT_DIR,
    "ml",
    "models"
)

PASS_MODEL = os.path.join(
    MODEL_FOLDER,
    "pass_fail_model.pkl"
)

GRADE_MODEL = os.path.join(
    MODEL_FOLDER,
    "grade_model.pkl"
)

TOTAL_MODEL = os.path.join(
    MODEL_FOLDER,
    "total_marks_model.pkl"
)

# ----------------------------------------------------
# Load Models
# ----------------------------------------------------

try:
    pass_model = joblib.load(PASS_MODEL)
    grade_model = joblib.load(GRADE_MODEL)
    total_model = joblib.load(TOTAL_MODEL)
except:
    pass_model = None
    grade_model = None
    total_model = None

# ----------------------------------------------------
# Prediction Page
# ----------------------------------------------------

def show():

    st.title("🤖 Student Prediction Dashboard")

    st.markdown("---")

    if (
        pass_model is None
        or grade_model is None
        or total_model is None
    ):
        st.error("Machine Learning models not found.")
        return

    st.header("Enter Student Details")

    department = st.selectbox(
        "Department",
        ["IT","CSE","CE","AI"]
    )

    semester = st.number_input(
        "Semester",
        min_value=1,
        max_value=8,
        value=5
    )

    maths = st.number_input(
        "Mathematics Marks",
        0,
        100,
        70
    )

    science = st.number_input(
        "Science Marks",
        0,
        100,
        70
    )

    english = st.number_input(
        "English Marks",
        0,
        100,
        70
    )

    computer = st.number_input(
        "Computer Marks",
        0,
        100,
        70
    )

    attendance = st.number_input(
        "Attendance",
        0,
        100,
        80
    )

    st.markdown("---")

    if st.button("Predict Result"):

        # Department Encoding
        dept = {
            "IT":0,
            "CSE":1,
            "CE":2,
            "AI":3
        }[department]

        features = pd.DataFrame(
            [[
                maths,
                science,
                english,
                computer,
                attendance
            ]],
            columns=[
                "Maths",
                "Science",
                "English",
                "Computer",
                "Attendance"
            ]
        )

        total_prediction = total_model.predict(features)[0]

        grade_prediction = grade_model.predict(features)[0]

        pass_prediction = pass_model.predict(features)[0]

        st.markdown("---")

        st.header("Prediction Result")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Expected Total",
            round(total_prediction,2)
        )

        c2.metric(
            "Predicted Grade",
            grade_prediction
        )

        c3.metric(
            "Result",
            pass_prediction
        )

        st.success("Prediction Completed Successfully.")