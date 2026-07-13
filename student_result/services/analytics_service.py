from pathlib import Path
import pandas as pd

from src.analysis import *

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "student_analyzed.csv"

def load_dataset():
    return pd.read_csv(DATA_PATH)

def get_dashboard_data():
    df = load_dataset()

    return {
        "total_students": get_total_students(df),
        "total_departments": get_total_departments(df),
        "pass_count": get_pass_count(df),
        "fail_count": get_fail_count(df),
        "highest_scorer": get_highest_scorer(df),
        "lowest_scorer": get_lowest_scorer(df),
        "class_average": get_class_average(df),
        "department_average": get_department_average(df),
        "top10": get_top10_students(df),
        "bottom10": get_bottom10_students(df)
    }