import pandas as pd


def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    print(department)


data = {
    "id": [1, 2, 3, 1, 1],
    "revenue": [8000, 9000, 10000, 7000, 6000],
    "month": ["Jan", "Jan", "Feb", "Feb", "Mar"]
}

df = pd.DataFrame(data)


reformat_table(df)
