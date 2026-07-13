import pandas as pd
import os

print("=" * 60)
print("STUDENT RESULT ANALYTICS")
print("DATASET TESTING")
print("=" * 60)

# -------------------------------------------------
# Dataset Location
# -------------------------------------------------

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_PATH = os.path.join(
    PROJECT_DIR,
    "data",
    "processed",
    "student_analyzed.csv"
)

print("\nDataset Path")
print(DATASET_PATH)

print("\n" + "=" * 60)

# -------------------------------------------------
# Check Dataset Exists
# -------------------------------------------------

if os.path.exists(DATASET_PATH):

    print("✓ Dataset Found")

else:

    print("✗ Dataset Not Found")
    exit()

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------

df = pd.read_csv(DATASET_PATH)

print("\nDataset Loaded Successfully")

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print("Rows :", df.shape[0])
print("Columns :", df.shape[1])

print("\nColumn Names")

for column in df.columns:
    print("-", column)

print("\nData Types")

print(df.dtypes)

print("\n" + "=" * 60)
print("CHECKING MISSING VALUES")
print("=" * 60)

missing = df.isnull().sum()

print(missing)

if missing.sum() == 0:

    print("\n✓ No Missing Values")

else:

    print("\n✗ Missing Values Found")

print("\n" + "=" * 60)
print("CHECKING DUPLICATES")
print("=" * 60)

duplicates = df.duplicated().sum()

print("Duplicate Rows :", duplicates)

if duplicates == 0:

    print("✓ No Duplicate Rows")

else:

    print("✗ Duplicate Rows Found")

print("\n" + "=" * 60)
print("CHECKING MARKS RANGE")
print("=" * 60)

subjects = [

    "Maths",

    "Science",

    "English",

    "Computer"

]

for subject in subjects:

    minimum = df[subject].min()

    maximum = df[subject].max()

    print(f"{subject}")

    print("Minimum :", minimum)

    print("Maximum :", maximum)

    if minimum >= 0 and maximum <= 100:

        print("✓ Valid")

    else:

        print("✗ Invalid")

    print()

print("\n" + "=" * 60)
print("CHECKING ATTENDANCE")
print("=" * 60)

minimum = df["Attendance"].min()

maximum = df["Attendance"].max()

print("Minimum :", minimum)

print("Maximum :", maximum)

if minimum >= 0 and maximum <= 100:

    print("✓ Attendance Valid")

else:

    print("✗ Attendance Invalid")

print("\n" + "=" * 60)
print("CHECKING TOTAL MARKS")
print("=" * 60)

minimum = df["Total"].min()

maximum = df["Total"].max()

print("Minimum Total :", minimum)

print("Maximum Total :", maximum)

if minimum >= 0:

    print("✓ Total Marks Valid")

else:

    print("✗ Invalid Total Marks")

print("\n" + "=" * 60)
print("CHECKING RESULT VALUES")
print("=" * 60)

print(df["Result"].value_counts())

print("\n" + "=" * 60)
print("CHECKING GRADE VALUES")
print("=" * 60)

print(df["Grade"].value_counts())

print("\n" + "=" * 60)
print("DATASET SUMMARY")
print("=" * 60)

print(df.describe())

print("\nDataset Testing Completed Successfully")

print("=" * 60)

