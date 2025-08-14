import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    merged = weather.merge(
        weather[["id", "recordDate", "temperature"]],
        left_on="recordDate",
        right_on=weather["recordDate"] + pd.Timedelta(days=1),
        how="inner",
        suffixes=("", "_y"),
    )
    filtered = merged[merged["temperature"] > merged["temperature_y"]]
    return filtered[["id"]].rename(columns={"id": "Id"})
