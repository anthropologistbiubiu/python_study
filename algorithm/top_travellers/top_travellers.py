

import pandas as pd


def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    users["user_id"] = users["id"]
    result = rides.groupby(["user_id"]).agg(
        travelled_distance=("distance", "sum")
    )
    result = users.merge(
        result,
        on="user_id",
        how="left"
    ).fillna(0)
    result = result[["name", "travelled_distance"]]
    result = result.sort_values(["travelled_distance", "name"], ascending=[
                                False, False]).reset_index(drop=True)
    return result


users = pd.DataFrame({
    "id": [1, 2, 3, 4, 7, 13, 19],
    "name": ["Alice", "Bob", "Alex", "Donald", "Lee", "Jonathan", "Elvis"]
})

rides = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "user_id": [1, 2, 3, 7, 13, 19, 7, 19, 7],
    "distance": [120, 317, 222, 100, 312, 50, 120, 400, 230]
})


if __name__ == "__main__":
    print(top_travellers(users, rides))
