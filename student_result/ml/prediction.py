import joblib
import pandas as pd

print("=" * 60)
print("STUDENT RESULT PREDICTION SYSTEM")
print("=" * 60)

import os
import joblib

# 1. Automatically calculate the folder path where prediction.py lives
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Build the perfect absolute paths to your model files
pass_model_path = os.path.join(script_dir, "models", "pass_fail_model.pkl")
grade_model_path = os.path.join(script_dir, "models", "grade_model.pkl")
marks_model_path = os.path.join(script_dir, "models", "total_marks_model.pkl")

# 3. Load the models safely using the smart paths
pass_model = joblib.load(pass_model_path)
print("✅ Pass/Fail Model loaded successfully!")

# Un-comment these lines when you are ready to use the other models:
grade_model = joblib.load(grade_model_path)
marks_model = joblib.load(marks_model_path)
# Load it directly as total_model
total_model = joblib.load(marks_model_path)

# total_model = joblib.load(total_model_path)

print("\nAll Models Loaded Successfully")

print("\nEnter Student Details\n")

# 1. Collect inputs with clear prompts
maths = float(input("Enter Maths Marks : "))
science = float(input("Enter Science Marks : "))
english = float(input("Enter English Marks : "))
computer = float(input("Enter Computer Marks : "))
attendance = float(input("Enter Attendance : "))

# 2. Create the DataFrame matching your CSV columns perfectly
student_data = pd.DataFrame(
    [
        [
            maths,
            science,
            english,
            computer,
            attendance
        ]
    ],
    columns=[
        "Maths",
        "Science",
        "English",
        "Computer",
        "Attendance"
    ]
)

result = pass_model.predict(student_data)

grade = grade_model.predict(student_data)

total = total_model.predict(student_data)

print("\n" + "=" * 60)
print("PREDICTION RESULT")
print("=" * 60)

print(f"Predicted Result      : {result[0]}")
print(f"Predicted Grade       : {grade[0]}")
print(f"Expected Total Marks  : {total[0]:.2f}")

print("=" * 60)