import pandas as pd


data = {
    "employee_id": [1, 2, 2, 3, 4, 4, 4],
    "department_id": [1, 1, 2, 3, 2, 3, 4],
    "primary_flag": ["N", "Y", "N", "N", "N", "Y", "N"],
}
df = pd.DataFrame(data)


def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    employee["cnt"] = employee.groupby("employee_id")["department_id"].transform(
        "count"
    )
    result = employee[(employee["primary_flag"] == "Y") | (employee["cnt"] == 1)]
    return result[["employee_id", "department_id"]]


if __name__ == "__main__":
    print(find_primary_department(df))
