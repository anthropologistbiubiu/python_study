import pandas as pd


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    result = (
        daily_sales.groupby(["date_id", "make_name"])
        .agg(
            unique_leads=("lead_id", "nunique"),
            unique_partners=("partner_id", "nunique"),
        )
        .reset_index()
        .sort_values(by=["make_name", "date_id"], ascending=[True, False])
    )
    return result


import pandas as pd

data = {
    "date_id": [
        "2020-12-8",
        "2020-12-8",
        "2020-12-8",
        "2020-12-7",
        "2020-12-7",
        "2020-12-8",
        "2020-12-8",
        "2020-12-7",
        "2020-12-7",
        "2020-12-7",
    ],
    "make_name": [
        "toyota",
        "toyota",
        "toyota",
        "toyota",
        "toyota",
        "honda",
        "honda",
        "honda",
        "honda",
        "honda",
    ],
    "lead_id": [0, 1, 1, 0, 0, 1, 2, 0, 1, 2],
    "partner_id": [1, 0, 2, 2, 1, 2, 1, 1, 2, 1],
}

df = pd.DataFrame(data)

print(daily_leads_and_partners(df))
