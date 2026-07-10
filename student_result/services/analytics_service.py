from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "student_analyzed.csv"


def load_dataset():
    """
    Load the processed dataset.
    """

    df = pd.read_csv(DATA_PATH)

    return df


def total_students(df):
    return len(df)


def total_columns(df):
    return len(df.columns)


def total_departments(df):
    return df["Department"].nunique()