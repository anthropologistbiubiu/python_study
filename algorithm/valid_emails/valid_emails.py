

import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    r = r"^[A-Za-z]{1,}[a-zA-Z0-9._-]*@leetcode\.com$"
    result = users[users["mail"].str.match(r)]
    return result
