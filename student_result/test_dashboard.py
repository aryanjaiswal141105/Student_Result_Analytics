import os

print("=" * 60)
print("STUDENT RESULT ANALYTICS")
print("DASHBOARD TESTING")
print("=" * 60)

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

dashboard_files = [

    "dashboard/app.py",

    "dashboard/home.py",

    "dashboard/analytics.py",

    "dashboard/visualization.py",

    "dashboard/prediction.py",

    "dashboard/reports.py"

]

print("\nChecking Dashboard Files\n")

passed = 0

for file in dashboard_files:

    path = os.path.join(PROJECT_DIR, file)

    if os.path.exists(path):

        print(f"[PASS] {file}")

        passed += 1

    else:

        print(f"[FAIL] {file}")

print("\n" + "=" * 60)

print(f"Dashboard Files : {passed}/{len(dashboard_files)}")

print("\nChecking Required Dataset\n")

dataset = os.path.join(
    PROJECT_DIR,
    "data",
    "processed",
    "student_analyzed.csv"
)

if os.path.exists(dataset):

    print("[PASS] student_analyzed.csv")

else:

    print("[FAIL] student_analyzed.csv")

print("\nChecking ML Models\n")

models = [

    "ml/models/pass_fail_model.pkl",

    "ml/models/grade_model.pkl",

    "ml/models/total_marks_model.pkl"

]

model_pass = 0

for model in models:

    path = os.path.join(PROJECT_DIR, model)

    if os.path.exists(path):

        print(f"[PASS] {model}")

        model_pass += 1

    else:

        print(f"[FAIL] {model}")

print()

print(f"Models : {model_pass}/{len(models)}")

print("\nChecking Output Folders\n")

folders = [

    "outputs/graphs",

    "outputs/reports",

    "outputs/tables"

]

folder_pass = 0

for folder in folders:

    path = os.path.join(PROJECT_DIR, folder)

    if os.path.exists(path):

        print(f"[PASS] {folder}")

        folder_pass += 1

    else:

        print(f"[FAIL] {folder}")

print()

print(f"Folders : {folder_pass}/{len(folders)}")

print("\nDashboard Manual Testing Checklist")

print("=" * 60)

print("""
Open Dashboard

python -m streamlit run dashboard/app.py

Verify:

[ ] Home Page Opens

[ ] Sidebar Visible

[ ] Analytics Page Opens

[ ] Visualization Page Opens

[ ] Prediction Page Opens

[ ] Reports Page Opens

[ ] No Red Error Messages

[ ] Charts Visible

[ ] Reports Load

[ ] Download Buttons Work

[ ] Prediction Button Works
""")

print("=" * 60)

if (
    passed == len(dashboard_files)
    and
    model_pass == len(models)
    and
    folder_pass == len(folders)
):

    print("Dashboard Verification PASSED")

else:

    print("Dashboard Verification FAILED")

print("=" * 60)

