import pandas as pd


def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    activity["activity_date"] = pd.to_datetime(activity["activity_date"])
    user_in_range = activity[(activity["activity_date"] >
                             "2019-06-27") & (activity["activity_date"] <= "2019-07-27")]
    result = user_in_range.groupby(["activity_date"])[
        "user_id"].nunique().reset_index(name="active_users")
    result = result.rename(columns={"activity_date": "day"})

    return result


data = {
    "user_id": [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4],
    "session_id": [1, 1, 1, 4, 4, 4, 2, 2, 2, 3, 3],
    "activity_date": [
        "2019-07-20", "2019-07-20", "2019-07-20",
        "2019-07-20", "2019-07-21", "2019-07-21",
        "2019-07-21", "2019-07-21", "2019-07-21",
        "2019-06-25", "2019-06-25"
    ],
    "activity_type": [
        "open_session", "scroll_down", "end_session",
        "open_session", "send_message", "end_session",
        "open_session", "send_message", "end_session",
        "open_session", "end_session"
    ]
}

pf = pd.DataFrame(data)

print(user_activity(pf))
