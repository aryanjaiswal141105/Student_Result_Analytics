import os
import joblib
import pandas as pd

print("=" * 60)
print("STUDENT RESULT ANALYTICS")
print("MACHINE LEARNING TESTING")
print("=" * 60)

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(PROJECT_DIR, "ml", "models")

print("\nModel Folder")

print(MODEL_DIR)

print("\n" + "=" * 60)

print("CHECKING MODEL FILES")

print("=" * 60)

models = [

    "pass_fail_model.pkl",

    "grade_model.pkl",

    "total_marks_model.pkl"

]

loaded_models = {}

count = 0

for model in models:

    path = os.path.join(MODEL_DIR, model)

    if os.path.exists(path):

        print(f"[PASS] {model}")

        loaded_models[model] = joblib.load(path)

        count += 1

    else:

        print(f"[FAIL] {model}")

print()

print(f"Loaded Models : {count}/{len(models)}")

print("\n" + "=" * 60)

print("CREATING SAMPLE STUDENT")

print("=" * 60)

sample = pd.DataFrame(

    [

        [

            80,

            85,

            78,

            90,

            95

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

print(sample)

print("\n" + "=" * 60)

print("PASS / FAIL PREDICTION")

print("=" * 60)

try:

    prediction = loaded_models["pass_fail_model.pkl"].predict(sample)

    print("Prediction")

    print(prediction)

    print("\nPASS")

except Exception as error:

    print("FAIL")

    print(error)

print("\n" + "=" * 60)

print("GRADE PREDICTION")

print("=" * 60)

try:

    prediction = loaded_models["grade_model.pkl"].predict(sample)

    print("Prediction")

    print(prediction)

    print("\nPASS")

except Exception as error:

    print("FAIL")

    print(error)

print("\n" + "=" * 60)

print("TOTAL MARKS PREDICTION")

print("=" * 60)

try:

    prediction = loaded_models["total_marks_model.pkl"].predict(sample)

    print("Prediction")

    print(prediction)

    print("\nPASS")

except Exception as error:

    print("FAIL")

    print(error)

print("\n" + "=" * 60)

print("INVALID INPUT TEST")

print("=" * 60)

wrong = pd.DataFrame(

    [

        [

            80,

            90

        ]

    ],

    columns=[

        "Maths",

        "Science"

    ]

)

for model_name in loaded_models:

    print(f"\nTesting {model_name}")

    try:

        loaded_models[model_name].predict(wrong)

        print("Unexpected Success")

    except Exception as error:

        print("PASS")

        print("Invalid input correctly rejected.")

print("\n" + "=" * 60)

print("MACHINE LEARNING TEST SUMMARY")

print("=" * 60)

print(f"Models Found : {count}/{len(models)}")

if count == len(models):

    print("All Models Loaded Successfully")

else:

    print("Some Models Missing")

print()

print("Testing Completed Successfully")

print("=" * 60)

