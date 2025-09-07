import pandas as pd


def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    print(department)
    result = department.pivot(index="id", columns="month", values="revenue")
    result.columns = [f"{col}_Revenue" for col in result.columns]
    months = [f"{month}_Revenue" for month in ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                                               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]]
    result = result.reindex(columns=months).reset_index()
    return result


data = {
    "id": [1, 2, 3, 1, 1],
    "revenue": [8000, 9000, 10000, 7000, 6000],
    "month": ["Jan", "Jan", "Feb", "Feb", "Mar"]


}
df = pd.DataFrame(data)

reformat_table(df)
