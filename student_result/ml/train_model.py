import pandas as pd

from sklearn.model_selection import train_test_split

from model_utils import load_dataset

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score

import joblib

dataset_path = r"C:\Users\Aryan\OneDrive\Desktop\Project\Data Analytics & ML\student_result\data\processed\student_analyzed.csv"


# dataset_path = "C:\Users\Aryan\OneDrive\Desktop\Project\Data Analytics & ML\student_result\data\processed\student_analyzed.csv"

df = load_dataset(dataset_path)

print("Dataset Loaded Successfully")

print(df.head())

print("\nDataset Information")

df.info()

print("\n" + "=" * 60)
print("STEP 11 : SELECT FEATURES")
print("=" * 60)

X = df[
    [
        "Maths",
        "Science",
        "English",
        "Computer",
        "Attendance"
    ]
]

print("\nFeature Columns")

print(X.head())

print("\n" + "=" * 60)
print("STEP 12 : SELECT TARGET")
print("=" * 60)

y = df["Result"]

print("\nTarget Column")

print(y.head())

print("\n" + "=" * 60)
print("STEP 13 : TRAIN TEST SPLIT")
print("=" * 60)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Feature Shape")

print(X_train.shape)

print("\nTesting Feature Shape")

print(X_test.shape)

print("\nTraining Target Shape")

print(y_train.shape)

print("\nTesting Target Shape")

print(y_test.shape)

print("\n" + "=" * 60)
print("DATASET PREPARATION COMPLETED")
print("=" * 60)

print("\nMachine Learning Dataset is Ready.")

# Part 2 Begin 

print("\n" + "=" * 60)
print("STEP 14 : CREATE DECISION TREE MODEL")
print("=" * 60)

model = DecisionTreeClassifier(random_state=42)

print("Decision Tree Model Created Successfully.")

# Train these Model

print("\n" + "=" * 60)
print("STEP 15 : TRAIN MODEL")
print("=" * 60)

model.fit(X_train, y_train)

print("Model Training Completed Successfully.")

# Test the Model 

print("\n" + "=" * 60)
print("STEP 16 : TEST MODEL")
print("=" * 60)

y_pred = model.predict(X_test)

print("Prediction Completed.")

# Compare the Prediction

print("\nActual Result")

print(y_test.values)

print("\nPredicted Result")

print(y_pred)

# Calculate the accuracy

print("\n" + "=" * 60)
print("STEP 17 : MODEL ACCURACY")
print("=" * 60)

accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy : {accuracy * 100:.2f}%")

print("\n" + "=" * 60)
print("STEP 18 : SAVE MODEL")
print("=" * 60)

joblib.dump(
    model,
    "models/pass_fail_model.pkl"
)

print("Pass/Fail Model Saved Successfully.")

# save the model

print("\n" + "=" * 60)
print("PASS / FAIL MODEL COMPLETED")
print("=" * 60)

print("Machine Learning Model is Ready.")

# Final Message for prediciton 