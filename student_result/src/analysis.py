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