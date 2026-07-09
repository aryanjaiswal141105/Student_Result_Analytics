import joblib
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

from model_utils import load_dataset

print("=" * 60)
print("EXPECTED TOTAL MARKS PREDICTION MODEL")
print("=" * 60)

dataset_path = "student_result/data/processed/student_analyzed.csv"

df = load_dataset(dataset_path)

print("\nDataset Loaded Successfully")

X = df[
    [
        "Maths",
        "Science",
        "English",
        "Computer",
        "Attendance"
    ]
]

y = df["Total"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

model = LinearRegression()

print("Linear Regression Model Created Successfully")

model.fit(X_train, y_train)

print("Model Training Completed Successfully")

y_pred = model.predict(X_test)

print("\nPrediction Completed Successfully")

comparison = pd.DataFrame({
    "Actual Total": y_test.values,
    "Predicted Total": y_pred.round(2)
})

print("\nComparison of Actual and Predicted Totals")
print(comparison)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print(f"Mean Absolute Error : {mae:.2f}")
print(f"R² Score : {r2:.2f}")

import os

# 1. Get the exact folder path where total_marks_model.py is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Build the perfect path to the models folder inside it
final_save_path = os.path.join(script_dir, "models", "total_marks_model.pkl")

# 3. Create the models folder automatically if it is missing
os.makedirs(os.path.dirname(final_save_path), exist_ok=True)

# 4. Save your model without any path issues
joblib.dump(model, final_save_path)
print(f"🎉 Success! Total Marks model saved at: {final_save_path}")

print("\nTotal Marks Model Saved Successfully")

print("\n" + "=" * 60)
print("EXPECTED TOTAL MARKS MODEL COMPLETED")
print("=" * 60)

print("Machine Learning Model is Ready.")