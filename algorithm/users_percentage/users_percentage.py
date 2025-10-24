import pandas as pd


def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    pass


users = pd.DataFrame({
    "user_id": [1, 2, 3, 4],
    "join_date": ["2020-02-14", "2020-02-14", "2020-03-01", "2020-04-01"]
})

register = pd.DataFrame({
    "user_id": [1, 2, 2, 3],
    "activity_date": ["2020-03-01", "2020-03-02", "2020-03-03", "2020-03-02"]
})
