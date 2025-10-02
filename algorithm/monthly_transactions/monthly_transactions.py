

import pandas as pd


def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    pass


data = {
    "id": [121, 122, 123, 124],
    "country": ["US", "US", "US", "DE"],
    "state": ["approved", "declined", "approved", "approved"],
    "amount": [1000, 2000, 2000, 2000],
    "trans_date": ["2018-12-18", "2018-12-19", "2019-01-01", "2019-01-07"]
}
transactions = pd.DataFrame(data)

print(monthly_transactions(transactions))
