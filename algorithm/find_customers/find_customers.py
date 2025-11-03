

import pandas as pd


def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    transactions = transactions[~transactions["amount"].isnull()]
    merged = visits.merge(transactions, on="visit_id", how="left")
    filter = merged[merged["amount"].isnull()]
    groupby = filter.groupby("customer_id").count().reset_index()
    result = groupby[["customer_id", "visit_id"]].rename(
        columns={"visit_id": "count_no_trans"}
    )
    return result.sort_values(by="count_no_trans", ascending=False)
