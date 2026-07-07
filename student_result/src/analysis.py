import pandas as pd

from utils import calculate_grade
from utils import calculate_result


# Load cleaned dataset

df = pd.read_csv("student_result/data/processed/student_cleaned.csv")

print("=" * 60)
print("Student Dataset Loaded Successfully")
print("=" * 60)

# -------------------------------------
# Create Total Marks
# -------------------------------------

df["Total"] = (
    df["Maths"]
    + df["Science"]
    + df["English"]
    + df["Computer"]
)

# -------------------------------------
# Create Average
# -------------------------------------

df["Average"] = df["Total"] / 4

# -------------------------------------
# Create Grade
# -------------------------------------

df["Grade"] = df["Average"].apply(calculate_grade)

# -------------------------------------
# Create Result
# -------------------------------------

df["Result"] = df.apply(
    lambda row: calculate_result(
        row["Maths"],
        row["Science"],
        row["English"],
        row["Computer"],
    ),
    axis=1,
)

print("\nNew Columns Added Successfully!\n")

print(df.head())

# Save new dataset

df.to_csv(
    "student_result/data/processed/student_analyzed.csv",
    index=False,
)

print("\nstudent_analyzed.csv created successfully.")