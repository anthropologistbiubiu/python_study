
import pandas as pd


def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merged = employees.merge(
        employee_uni,
        on="id",
        how="left"
    )
    result = merged[["unique_id", "name"]]
    return result


# 模拟数据
employees = pd.DataFrame({
    "id": [1, 7, 11, 90, 3],
    "name": ["Alice", "Bob", "Meir", "Winston", "Jonathan"]
})

employee_uni = pd.DataFrame({
    "id": [3, 11, 90],
    "unique_id": [1, 2, 3]
})

if __name__ == "__main__":
    print(replace_employee_id(employees, employee_uni))
