import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    try:
        employees["total_time"] = employees["out_time"] - employees["in_time"]

        result = (
            employees.groupby(["emp_id", "event_day"])
            .agg(total_time=("total_time", "sum"))
            .reset_index()
            .rename(columns={"event_day": "day"})
        )
        result = result[["day", "emp_id", "total_time"]]
        result = result.sort_values(by=["day"])
        return result

    except KeyError as e:
        print(f"KeyError: {e}")
    return None
