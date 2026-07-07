import pandas as pd

df = pd.read_csv("student_result/data/raw/students.csv")

# print (df) // It display the table on output.. 

# print(df.shape) // It display the no. of rows & columns

# print(df.columns) // It display the columns & datatypes of columns

# print(df.head()) // It shows first 5 values of the dataset

# print(df.tail()) // It shows last 5 values of the dataset

# print(df.info()) // It display the datatypes of table

# print(df.describe()) // It shows Avg, Max, Min, Highest Attendance 

print("=" * 60)
print("Student Dataset Loaded Successfully")
print("=" * 60)

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

df.to_csv(
    "student_result/data/processed/student_cleaned.csv",
    index=False
)