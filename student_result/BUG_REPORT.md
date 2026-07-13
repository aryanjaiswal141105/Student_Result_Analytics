# Student Result Analytics

# Bug Report

## Project

Student Result Analytics Dashboard

---

## Bug 1

Problem

Prediction page throws:

ValueError:
Feature names should match those that were passed during fit.

Reason

Dashboard passes extra columns:

- Department
- Semester

while the ML models were trained using only:

- Maths
- Science
- English
- Computer
- Attendance

Status

Fixed by ensuring prediction input matches training features.

---

## Bug 2

Problem

ModuleNotFoundError

Reason

Incorrect Python import path.

Status

Fixed.

---

## Bug 3

Problem

CSV File Not Found

Reason

Wrong dataset path.

Status

Fixed using absolute project paths.

---

## Bug 4

Problem

Model File Missing

Reason

Model not trained or wrong path.

Status

Verified using test_ml.py.

---

## Bug 5

Problem

Dashboard page not loading.

Reason

Incorrect Streamlit execution path.

Correct command

python -m streamlit run dashboard/app.py

Status

Fixed.

---

Final Result

Major bugs resolved.

Project ready for deployment.