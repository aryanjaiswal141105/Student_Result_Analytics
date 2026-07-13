import os
import sys

print("=" * 60)
print("STUDENT RESULT ANALYTICS")
print("PROJECT VERIFICATION")
print("=" * 60)

# -------------------------------------------------
# Project Root
# -------------------------------------------------

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

print("\nProject Location")
print(PROJECT_DIR)

print("\n" + "=" * 60)

# -------------------------------------------------
# Required Folders
# -------------------------------------------------

folders = [

    "dashboard",

    "data",

    "data/raw",

    "data/processed",

    "src",

    "ml",

    "ml/models",

    "outputs",

    "outputs/graphs",

    "outputs/reports",

    "outputs/tables",

    "notebooks"

]

print("CHECKING FOLDERS")

print("-" * 60)

folder_pass = 0

for folder in folders:

    path = os.path.join(PROJECT_DIR, folder)

    if os.path.exists(path):

        print(f"[PASS] {folder}")

        folder_pass += 1

    else:

        print(f"[FAIL] {folder}")

print("-" * 60)

print(f"Folders Verified : {folder_pass}/{len(folders)}")

print("\n" + "=" * 60)

print("CHECKING IMPORTANT FILES")

print("-" * 60)

files = [

    "dashboard/app.py",

    "dashboard/home.py",

    "dashboard/analytics.py",

    "dashboard/visualization.py",

    "dashboard/prediction.py",

    "dashboard/reports.py",

    "src/cleaning.py",

    "src/analysis.py",

    "src/visualization.py",

    "ml/train_model.py",

    "ml/grade_model.py",

    "ml/total_marks_model.py",

    "ml/models/pass_fail_model.pkl",

    "ml/models/grade_model.pkl",

    "ml/models/total_marks_model.pkl",

    "data/raw/students.csv",

    "data/processed/student_cleaned.csv",

    "data/processed/student_analyzed.csv"

]

file_pass = 0

for file in files:

    path = os.path.join(PROJECT_DIR, file)

    if os.path.exists(path):

        print(f"[PASS] {file}")

        file_pass += 1

    else:

        print(f"[FAIL] {file}")

print("-" * 60)

print(f"Files Verified : {file_pass}/{len(files)}")

print("\n" + "=" * 60)

print("PYTHON INFORMATION")

print("-" * 60)

print("Python Version")

print(sys.version)

print("-" * 60)

print("VERIFICATION SUMMARY")

print("-" * 60)

print(f"Folders : {folder_pass}/{len(folders)}")

print(f"Files   : {file_pass}/{len(files)}")

if folder_pass == len(folders) and file_pass == len(files):

    print("\nPROJECT VERIFICATION SUCCESSFUL")

else:

    print("\nPROJECT VERIFICATION COMPLETED")

    print("Some folders/files are missing.")

print("=" * 60)
