import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_result/data/processed/student_analyzed.csv")

print(df.head())

department_average = df.groupby("Department")["Average"].mean()

plt.figure(figsize=(8,5))

department_average.plot(kind="bar")

plt.title("Department Average Marks")

plt.xlabel("Department")

plt.ylabel("Average Marks")

plt.tight_layout()

plt.savefig("student_result/outputs/graphs/bar_department_average.png")

plt.close()

print("Bar Chart Created")

# It create the bar graph img of given dataset 

grade_distribution = df["Grade"].value_counts()

plt.figure(figsize=(7,7))

grade_distribution.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Grade Distribution")

plt.tight_layout()

plt.savefig(
    "student_result/outputs/graphs/pie_grade_distribution.png"
)

plt.close()

print("Pie Chart Created")

# It create the Pie chart img of given dataset 

plt.figure(figsize=(8,5))

plt.hist(
    df["Average"],
    bins=10
)

plt.title("Distribution of Average Marks")

plt.xlabel("Average Marks")

plt.ylabel("Number of Students")

plt.tight_layout()

plt.savefig(
    "student_result/outputs/graphs/histogram_average_marks.png"
)

plt.close()

print("Histogram Created")

# It create the histogram img of given dataset

plt.figure(figsize=(12,5))

plt.plot(
    df["Roll_No"],
    df["Average"],
    marker="o"
)

plt.title("Student Average Marks")

plt.xlabel("Roll Number")

plt.ylabel("Average Marks")

plt.tight_layout()

plt.savefig(
    "student_result/outputs/graphs/line_student_marks.png"
)

plt.close()

print("Line Chart Created")

# It create the line chart img of given dataset

plt.figure(figsize=(8,5))

df.boxplot(
    column="Average",
    by="Department"
)

plt.title("Department-wise Average Marks")

plt.suptitle("")

plt.xlabel("Department")

plt.ylabel("Average Marks")

plt.tight_layout()

plt.savefig(
    "student_result/outputs/graphs/boxplot_department_marks.png"
)

plt.close()

print("Box Plot Created")

# It create the Box plot img of given dataset

attendance = df.groupby("Department")["Attendance"].mean()

plt.figure(figsize=(8,5))

attendance.plot(kind="bar")

plt.title("Department Attendance")

plt.xlabel("Department")

plt.ylabel("Attendance (%)")

plt.tight_layout()

plt.savefig(
    "student_result/outputs/graphs/attendance_bar_chart.png"
)

plt.close()

print("Attendance Chart Created")

# It create attendance img of given dataset
