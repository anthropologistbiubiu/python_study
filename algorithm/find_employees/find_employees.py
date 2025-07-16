

import pandas as pd

data = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 80000, 60000, 90000],
    'managerId': [3, 4, None, None]
}
employee = pd.DataFrame(data)

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(
        employee[['id', 'salary']],      # 👈 提取经理信息：id 和工资
        left_on='managerId',             # 👈 员工表中的 managerId
        right_on='id',                   # 👈 经理的 id
        how='inner',
        suffixes=('', '_manager')        # 👈 字段重名时添加后缀
    )
    filtered = merged[merged['salary'] > merged['salary_manager']]
    result = filtered[['name']].rename(columns={'name': 'Employee'})
    return result

reuslt = find_employees(employee)
print(reuslt)