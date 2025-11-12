import pandas as pd


df = pd.DataFrame({"user_id": [0, 1, 2, 2], "follower_id": [1, 0, 0, 1]})


print(df)


def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    result = (
        followers.groupby(["user_id"])
        .agg(followers=("follower_id", "count"))
        .reset_index()
    )
    return result


if __name__ == "__main__":
    count_followers(df)
