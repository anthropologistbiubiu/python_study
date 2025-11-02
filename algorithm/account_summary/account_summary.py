
import pandas as pd


def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    result = transactions.groupby('account').agg(
        balance=("amount", "sum")
    ).reset_index()
    result = result.merge(users, on="account", how="inner")[
        ["name", "balance"]]
    result = result[result["balance"] > 10000]
    return result

    '''
    for account, group in result:
        print(f"📦 Account: {account}")
        print(group)
        print("-----")
    '''


users = pd.DataFrame({
    "account": [900001, 900002, 900003],
    "name": ["Alice", "Bob", "Charlie"]
})

transactions = pd.DataFrame({
    "trans_id": [1, 2, 3, 4, 5, 6, 7],
    "account": [900001, 900001, 900001, 900002, 900003, 900003, 900003],
    "amount": [7000, 7000, -3000, 1000, 6000, 6000, -4000],
    "transacted_on": [
        "2020-08-01", "2020-09-01", "2020-09-02",
        "2020-09-12", "2020-08-07", "2020-09-07", "2020-09-11"
    ]
})


if __name__ == "__main__":
    print(account_summary(users, transactions))
