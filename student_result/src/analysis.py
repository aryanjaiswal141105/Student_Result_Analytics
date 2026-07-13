import pandas as pd
import matplotlib.pyplot as plt

from src.utils import (
    calculate_grade,
    calculate_result,
    calculate_total,
)

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

print("\n" + "=" * 60)
print("STUDENT PERFORMANCE ANALYSIS")
print("=" * 60) 

total_students = len(df)

print(f"\nTotal Students : {total_students}")

#  from 63 to 73 line code it represent number of the students 

highest_scorer = df.loc[df["Total"].idxmax()]

print("\nHighest Scorer")

print("-----------------------")

print(highest_scorer)

# It shows highest scorer on the dataset from data folder

lowest_scorer = df.loc[df["Total"].idxmin()]

print("\nLowest Scorer")

print("-----------------------")

print(lowest_scorer)

#  It will describe the lowest score of the dataset table

class_average = df["Average"].mean()

print(f"\nOverall Class Average : {class_average:.2f}")

# It Calculate the Average of all data in dataset not 1 data of the dataset 

highest_average = df["Average"].max()

print(f"\nHighest Average : {highest_average}")

# It shows the highest average of dataset

lowest_average = df["Average"].min()

print(f"\nLowest Average : {lowest_average}")

# It shows the lowest average of dataset

top10 = df.sort_values(
    by="Total",
    ascending=False
).head(10)

print("\nTop 10 Students")

print("-----------------------")

print(
    top10[
        [
            "Roll_No",
            "Name",
            "Department",
            "Total",
            "Average",
            "Grade"
        ]
    ]
)

#  It will call the highest average students in ascending order format 

bottom10 = df.sort_values(
    by="Total",
    ascending=True
).head(10)

print("\nBottom 10 Students")

print("-----------------------")

print(
    bottom10[
        [
            "Roll_No",
            "Name",
            "Department",
            "Total",
            "Average",
            "Grade"
        ]
    ]
)

# It will call the bottom students according average system

pass_students = len(
    df[df["Result"] == "Pass"]
)

pass_percentage = (
    pass_students / total_students
) * 100

print(
    f"\nPass Percentage : {pass_percentage:.2f}%"
)

# It show the ratio of student, How many student were passed on given dataset

fail_students = len(
    df[df["Result"] == "Fail"]
)

fail_percentage = (
    fail_students / total_students
) * 100

print(
    f"Fail Percentage : {fail_percentage:.2f}%"
)

# It show the ratio of student, How many student were failed on given dataset

top10.to_csv(
    "student_result/outputs/tables/top10_students.csv",
    index=False
)

# It create new .csv file of the Top 10 student on tables folder of outputs

bottom10.to_csv(
    "student_result/outputs/tables/bottom10_students.csv",
    index=False
)

# It create new .csv file of the bottom 10 student on tables folder of outputs

print("\n" + "="*60)
print("DEPARTMENT PERFORMANCE ANALYSIS")
print("="*60)

# It Show the department performance analysis

departments = df["Department"].unique()

print("\nDepartments Available:")

for dept in departments:
    print(dept)

print(f"\nTotal Departments : {len(departments)}")

#  Total number of department are dataset

department_count = df["Department"].value_counts()

print("\nStudents in Each Department")

print("-----------------------------")

print(department_count)

#  Number of students are each department 

department_average = df.groupby("Department")["Average"].mean()

print("\nDepartment Average Marks")

print("---------------------------")

print(department_average)

# Average of all the department students in givne dataset 

department_attendance = df.groupby("Department")["Attendance"].mean()

print("\nDepartment Attendance")

print("-------------------------")

print(department_attendance)

#  Department Wise students attendence list 

print("\nDepartment Toppers")

print("----------------------")

for department in departments:

    topper = df[df["Department"] == department]

    topper = topper.loc[topper["Total"].idxmax()]

    print("\nDepartment :", department)

    print("Name :", topper["Name"])

    print("Total :", topper["Total"])

    print("Average :", topper["Average"])

    print("Grade :", topper["Grade"])

    #  Department wise student topper

best_department = department_average.idxmax()

best_average = department_average.max()

print("\nBest Performing Department")

print("------------------------------")

print("Department :", best_department)

print("Average :", round(best_average,2))

#  Best performing  department students

lowest_department = department_average.idxmin()

lowest_average = department_average.min()

print("\nLowest Performing Department")

print("------------------------------")

print("Department :", lowest_department)

print("Average :", round(lowest_average,2))

# lowest performing department students

department_summary = pd.DataFrame({

    "Average Marks": department_average,

    "Average Attendance": department_attendance,

    "Student Count": department_count

})

department_summary.to_csv(

    "student_result/outputs/tables/department_report.csv"

)

# create new .csv file of department summary

print("\n" + "=" * 60)
print("ATTENDANCE ANALYTICS")
print("=" * 60)

# Attendance analytics

df["Attendance_Status"] = df["Attendance"].apply(
    lambda attendance: "Good" if attendance >= 75 else "Low"
)

print("\nAttendance Status Added Successfully.")

# It show the attendance status for given dataset

average_attendance = df["Attendance"].mean()

print(
    f"\nOverall Average Attendance : {average_attendance:.2f}%"
)

#  Overall average attendance of given dataset

highest_attendance = df.loc[
    df["Attendance"].idxmax()
]

print("\nHighest Attendance Student")

print("----------------------------")

print(highest_attendance[
    [
        "Roll_No",
        "Name",
        "Department",
        "Attendance"
    ]
])

# Highest number of student in attendance 

lowest_attendance = df.loc[
    df["Attendance"].idxmin()
]

print("\nLowest Attendance Student")

print("---------------------------")

print(
    lowest_attendance[
        [
            "Roll_No",
            "Name",
            "Department",
            "Attendance"
        ]
    ]
)

# Lowest number of student in attendance

low_attendance = df[
    df["Attendance"] < 75
]

print("\nStudents Below 75% Attendance")

print("--------------------------------")

print(
    low_attendance[
        [
            "Roll_No",
            "Name",
            "Department",
            "Attendance"
        ]
    ]
)

# Student who has attendance below 75%

attendance_summary = df[
    "Attendance_Status"
].value_counts()

print("\nAttendance Summary")

print("---------------------")

print(attendance_summary)

# counting the number student has has good/bad attendance summary

department_attendance_report = (
    df.groupby("Department")["Attendance"]
    .agg(["count", "mean", "max", "min"])
)

department_attendance_report.columns = [
    "Total Students",
    "Average Attendance",
    "Highest Attendance",
    "Lowest Attendance"
]

print("\nDepartment Attendance Report")
print("--------------------------------")
print(department_attendance_report)

# We create the format of department attendance report 

department_attendance_report.to_csv(
    "student_result/outputs/tables/attendance_report.csv"
)

# It store the department attendance report in folder of output/tables

low_attendance.to_csv(
    "student_result/outputs/tables/low_attendance_students.csv",
    index=False
)

# it will store the data of the low attendance student to .csv format

with open(
    "student_result/outputs/reports/attendance_summary.txt",
    "w"
) as file:

    file.write("="*50 + "\n")
    file.write("ATTENDANCE ANALYTICS REPORT\n")
    file.write("="*50 + "\n\n")

    file.write(
        f"Average Attendance : {average_attendance:.2f}%\n"
    )

    file.write(
        f"Highest Attendance : {highest_attendance['Name']} ({highest_attendance['Attendance']}%)\n"
    )

    file.write(
        f"Lowest Attendance : {lowest_attendance['Name']} ({lowest_attendance['Attendance']}%)\n"
    )

    file.write(
        f"\nStudents Below 75% : {len(low_attendance)}\n"
    )

print("\nAttendance Summary Report Generated Successfully.")

# It will ATTENDANCE ANALYTICS REPORT and saved to the folder of reports

df.to_csv(
    "student_result/data/processed/student_analyzed.csv",
    index=False
)

#  it will update the table format of the student_analyzed.csv on folder of processed/data

print("\n" + "=" * 60)
print("GRADE DISTRIBUTION")
print("=" * 60)

grade_distribution = df["Grade"].value_counts()

print(grade_distribution)

# It describe the grade distribution

grade_distribution.to_csv(
    "student_result/outputs/tables/grade_distribution.csv"
)

# It create new file of grade distribution.csv

department_average.plot(
    kind="bar",
    title="Department Average Marks"
)

plt.ylabel("Average Marks")

plt.tight_layout()

plt.savefig(
    "student_result/outputs/graphs/department_average.png"
)

plt.close()

#  Create the img of department average plot \

department_attendance.plot(
    kind="bar",
    title="Department Attendance"
)

plt.ylabel("Attendance")

plt.tight_layout()

plt.savefig(
    "student_result/outputs/graphs/attendance_chart.png"
)

plt.close()

# create the img of department attendance 

grade_distribution.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Grade Distribution")

plt.ylabel("")

plt.tight_layout()

plt.savefig(
    "student_result/outputs/graphs/grade_distribution.png"
)

plt.close()

#  create the img of grade distribution 

department_count.plot(
    kind="bar"
)

plt.title("Students per Department")

plt.tight_layout()

plt.savefig(
    "student_result/outputs/graphs/department_students.png"
)

plt.close()

#  create the counting as per department wise

with open(
    "student_result/outputs/reports/final_project_report.txt",
    "w"
) as report:

    report.write("=" * 60 + "\n")
    report.write("STUDENT RESULT ANALYTICS REPORT\n")
    report.write("=" * 60 + "\n\n")

    report.write(f"Total Students : {total_students}\n")
    report.write(f"Overall Average : {class_average:.2f}\n")
    report.write(f"Highest Average : {highest_average:.2f}\n")
    report.write(f"Lowest Average : {lowest_average:.2f}\n")
    report.write(f"Pass Percentage : {pass_percentage:.2f}%\n")
    report.write(f"Fail Percentage : {fail_percentage:.2f}%\n")
    report.write(f"Average Attendance : {average_attendance:.2f}%\n")
    report.write(f"Best Department : {best_department}\n")
    report.write(f"Lowest Department : {lowest_department}\n")

print("\nFinal Project Report Generated Successfully.")

# final report of the student result analytics.

df.to_csv(
    "student_result/data/processed/student_analyzed.csv",
    index=False
)

print("\nFinal Dataset Saved Successfully.")

# it will update the final dataset on student_analyzed.csv

def get_total_students(df):
    return len(df)

def get_total_departments(df):
    return df["Department"].nunique()

def get_pass_count(df):
    return len(df[df["Result"] == "Pass"])

def get_fail_count(df):
    return len(df[df["Result"] == "Fail"])

def get_highest_scorer(df):
    return df.loc[df["Total"].idxmax()]

def get_lowest_scorer(df):
    return df.loc[df["Total"].idxmin()]

def get_class_average(df):
    return round(df["Total"].mean(), 2)

def get_department_average(df):
    return (
        df.groupby("Department")["Total"]
        .mean()
        .round(2)
        .reset_index()
    )

def get_top10_students(df):
    return (
        df.sort_values("Total", ascending=False)
        .head(10)
    )

def get_bottom10_students(df):
    return (
        df.sort_values("Total")
        .head(10)
    )