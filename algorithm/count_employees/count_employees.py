import pandas as pd
import numpy as np


employees = pd.DataFrame(
    {
        "employee_id": [1, 2, 3, 4, 5, 6, 7, 8],
        "name": [
            "Michael",
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eve",
            "Frank",
            "Grace",
        ],
        "reports_to": [None, 1, 1, 2, 2, 3, None, None],
        "age": [45, 38, 42, 34, 40, 37, 50, 48],
    }
)
"""
+-------------+---------+------------+-----+ 
| employee_id | name    | reports_to | age |
|-------------|---------|------------|-----|
| 1           | Michael | null       | 45  |
| 2           | Alice   | 1          | 38  |
| 3           | Bob     | 1          | 42  |
| 4           | Charlie | 2          | 34  |
| 5           | David   | 2          | 40  |
| 6           | Eve     | 3          | 37  |
| 7           | Frank   | null       | 50  |
| 8           | Grace   | null       | 48  |
+-------------+---------+------------+-----+ 
"""

"""
+-------------+---------+---------------+-------------+
| employee_id | name    | reports_count | average_age |
| ----------- | ------- | ------------- | ----------- |
| 1           | Michael | 2             | 40          |
| 2           | Alice   | 2             | 37          |
| 3           | Bob     | 1             | 37          |
+-------------+---------+---------------+-------------+
"""

df = pd.DataFrame(
    {
        "employee_id": [9, 6, 4, 2],
        "name": ["Hercy", "Alice", "Bob", "Winston"],
        "reports_to": [None, 9, 9, None],
        "age": [43, 41, 36, 37],
    }
)


def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    print(employees)
    merged = employees.merge(
        employees,
        left_on="employee_id",
        right_on="reports_to",
        how="inner",
        # suffixes=["_x", "_y"],
    )
    result = (
        merged.groupby(["employee_id_x"]).agg(
            reports_count=("employee_id_y", "count"),
            average_age=("age_y", lambda x: np.mean(x.astype(float))),
        )
        # .astype({"average_age": "float64"})
        .reset_index()
    )
    print(merged)
    result = result.merge(
        employees,
        left_on="employee_id_x",
        right_on="employee_id",
    )
    result = result[["employee_id", "name", "reports_count", "average_age"]]
    return result


if __name__ == "__main__":
    print(count_employees(employees=employees))
