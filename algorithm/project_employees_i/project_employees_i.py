

import pandas as pd

"""
Project 表：

Employee 表：

输出：
+-------------+---------------+
| project_id  | average_years |
+-------------+---------------+
| 1           | 2.00          |
| 2           | 2.50          |
+-------------+---------------+
解释：第一个项目中，员工的平均工作年限是 (3 + 2 + 1) / 3 = 2.00；第二个项目中，员工的平均工作年限是 (3 + 2) / 2 = 2.50
"""


def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merge = project.merge(
        employee,
        how="inner",
        on="employee_id",
    )
    mean = merge.groupby("project_id").mean(
        "experience_years").round(2).reset_index()
    result = mean[["project_id", "experience_years"]].rename(
        columns={"experience_years": "average_years"})
    return result


project = pd.DataFrame(
    {"project_id": [1, 1, 1, 2, 2], "employee_id": [1, 2, 3, 1, 4]})

employee = pd.DataFrame({"employee_id": [1, 2, 3, 4], "name": [
                        "Khaled", "Ali", "John", "Doe"], "experience_years": [3, 2, 1, 1]})


print(project_employees_i(project=project, employee=employee))
