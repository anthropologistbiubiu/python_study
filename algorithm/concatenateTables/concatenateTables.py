import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    result = pd.concat([df1, df2], ignore_index=True)
    return result


# df1 数据
data1 = {
    "student_id": [1, 2, 3, 4],
    "name": ["Mason", "Ava", "Taylor", "Georgia"],
    "age": [8, 6, 15, 17],
}

df1 = pd.DataFrame(data1)

# df2 数据
data2 = {"student_id": [5, 6], "name": ["Leo", "Alex"], "age": [7, 7]}

df2 = pd.DataFrame(data2)


if __name__ == "__main__":
    result = concatenateTables(df1=df1, df2=df2)
    print(result)
