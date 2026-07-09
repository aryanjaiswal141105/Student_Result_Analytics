import pandas as pd

from sklearn.model_selection import train_test_split

from model_utils import load_dataset

dataset_path = r"C:\Users\Aryan\OneDrive\Desktop\Project\Data Analytics & ML\student_result\data\processed\student_analyzed.csv"


# dataset_path = "C:\Users\Aryan\OneDrive\Desktop\Project\Data Analytics & ML\student_result\data\processed\student_analyzed.csv"

df = load_dataset(dataset_path)

print("Dataset Loaded Successfully")

print(df.head())

print("\nDataset Information")

df.info()