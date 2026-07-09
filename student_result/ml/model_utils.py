import pandas as pd


def load_dataset(file_path):
    """
    Load the CSV dataset and return a DataFrame.
    """

    df = pd.read_csv(file_path)

    return df