

import pandas as pd


def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    start_df = activity[activity["activity_type"] == "start"].copy()
    end_df = activity[activity["activity_type"] == "end"].copy()

    merged = pd.merge(
        start_df, end_df, on=["machine_id", "process_id"], suffixes=["_start", "_end"]
    )

    merged["duration"] = merged["timestamp_end"] - merged["timestamp_start"]

    result = merged.groupby("machine_id")["duration"].mean().round(3).reset_index()
    result.rename(columns={"duration": "processing_time"}, inplace=True)
    return result
    

data = [
    [0, 0, 'start', 0.712],
    [0, 0, 'end', 1.520],
    [0, 1, 'start', 3.140],
    [0, 1, 'end', 4.120],
    [1, 0, 'start', 0.550],
    [1, 0, 'end', 1.550],
    [1, 1, 'start', 0.430],
    [1, 1, 'end', 1.420],
    [2, 0, 'start', 4.100],
    [2, 0, 'end', 4.512],
    [2, 1, 'start', 2.500],
    [2, 1, 'end', 5.000],
]

df = pd.DataFrame(data, columns=['machine_id',
                  'process_id', 'activity_type', 'timestamp'])

print(get_average_time(df))
