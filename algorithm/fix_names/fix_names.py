

import pandas as pd


data = {
    'user_id': [1, 2],
    'name': ['aLice', 'bOB']
}

df = pd.DataFrame(data)


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str.capitalize()
    users.sort_values(by=["name"], inplace=True)
    return users


if __name__ == "__main__":
    print(fix_names(df))
