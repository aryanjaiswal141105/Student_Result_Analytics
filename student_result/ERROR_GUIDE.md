# Student Result Analytics

# Error Handling Guide

---

## File Not Found

Check

- Dataset exists
- Model exists
- Graph exists

---

## Model Error

Retrain model if .pkl file is missing.

---

## Prediction Error

Ensure prediction uses exactly these features:

Maths

Science

English

Computer

Attendance

---

## Streamlit Error

Run

python -m streamlit run dashboard/app.py

---

## Module Error

Run project from project root.

---

## Dataset Error

Check

student_analyzed.csv

---

## Dashboard Error

Verify

dashboard/

contains

app.py

home.py

analytics.py

prediction.py

visualization.py

reports.py

---

## ML Error

Verify

ml/models/

contains

pass_fail_model.pkl

grade_model.pkl

total_marks_model.pkl

---

## Final Recommendation

Always run

verify_project.py

before deployment.