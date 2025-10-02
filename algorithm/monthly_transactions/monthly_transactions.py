

import pandas as pd


"""
+----------+---------+-------------+----------------+--------------------+-----------------------+
| month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
+----------+---------+-------------+----------------+--------------------+-----------------------+
"""

"""
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | DE      | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+
"""


def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:

    transactions["date"] = pd.to_datetime(transactions["trans_date"])
    transactions["month"] = transactions["date"].dt.strftime("%Y-%m")
    transactions["cnt"] = transactions["state"] == "approved"
    transactions["total"] = 1
    result1 = transactions.groupby(["month", "country"], dropna=False).agg(
        trans_count=("total", "sum"),
        trans_total_amount=("amount", "sum"),
    ).reset_index()
    result2 = transactions.groupby(["month", "country", "state"], dropna=False).agg(
        approved_count=("cnt", "sum"),
        approved_total_amount=("amount", "sum")
    ).reset_index()
    result2 = result2[result2["approved_count"] > 0]
    result = result1.merge(result2, on=["month", "country"], how="left")[
        ["month", "country", "trans_count", "approved_count", "trans_total_amount", "approved_total_amount"]].fillna({"approved_count": 0, "approved_total_amount": 0})

    result = result.sort_values(
        by=["month", "country"],   # 先按 country，再按 month
        ascending=[True, False]     # 两个都升序（默认就是 True）
    ).reset_index(drop=True)
    return result


data = {
    "id": [121, 122, 123, 124],
    "country": ["US", "US", "US", "DE"],
    "state": ["approved", "declined", "approved", "approved"],
    "amount": [1000, 2000, 2000, 2000],
    "trans_date": ["2018-12-18", "2018-12-19", "2019-01-01", "2019-01-07"]
}
transactions = pd.DataFrame(data)

print(monthly_transactions(transactions))
