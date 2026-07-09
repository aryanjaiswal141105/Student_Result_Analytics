import joblib
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from model_utils import load_dataset

# Header File of the grade_model

print("=" * 60)
print("GRADE PREDICTION MODEL")
print("=" * 60)

dataset_path = r"C:\Users\Aryan\OneDrive\Desktop\Project\Data Analytics & ML\student_result\data\processed\student_analyzed.csv"

df = load_dataset(dataset_path)

print("\nDataset Loaded Successfully\n")

# Load Dataset

X = df[
    [
        "Maths",
        "Science",
        "English",
        "Computer",
        "Attendance"
    ]
]

y = df["Grade"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

model = DecisionTreeClassifier(
    random_state=42
)

print("Decision Tree Created")

model.fit(
    X_train,
    y_train
)

print("Grade Model Training Completed")

y_pred = model.predict(
    X_test
)

print("\nPrediction Completed")

print("\nActual Grades")

print(y_test.values)

print("\nPredicted Grades")

print(y_pred)

accuracy = accuracy_score(
    y_test,
    y_pred
)

print(f"\nAccuracy : {accuracy * 100:.2f}%")

import os

# 1. Automatically calculate the exact path of the folder where this script lives
script_directory = os.path.dirname(os.path.abspath(__file__))

# 2. Build the correct path to the models folder inside it
save_path = os.path.join(script_directory, "models", "grade_model.pkl")

# 3. Double check and create the folder if Python still cannot see it
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# 4. Save your model safely
joblib.dump(model, save_path)
print(f"🎉 Success! Model saved perfectly at: {save_path}")

print("\nGrade Model Saved Successfully")

print("\n" + "=" * 60)
print("GRADE PREDICTION MODEL COMPLETED")
print("=" * 60)

