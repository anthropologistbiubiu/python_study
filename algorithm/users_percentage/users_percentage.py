import pandas as pd


def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    register_user = register.groupby(
        ["contest_id"])["user_id"].count().reset_index()

    register_user["total"] = users["user_id"].nunique()
    register_user["percentage"] = register_user["user_id"] / \
        register_user["total"] * 100
    register_user["percentage"] = register_user["percentage"].round(2)
    register_user = register_user.sort_values(
        by=["percentage", "contest_id"], ascending=[False, True])
    result = register_user[["contest_id", "percentage"]]
    return result


users = pd.DataFrame({
    "user_id": [6, 2, 7],
    "user_name": ["Alice", "Bob", "Alex"]
})

register = pd.DataFrame({
    "contest_id": [215, 209, 208, 210, 208, 209, 209, 215, 208, 210, 207, 210],
    "user_id":    [6,  2,  2,  6,  6,  7,  6,  7,  7,  2,  2,  7]
})


print(users_percentage(users=users, register=register))
