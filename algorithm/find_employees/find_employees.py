

import pandas as pd

data = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 80000, 60000, 90000],
    'managerId': [3, 4, None, None]
}
employee = pd.DataFrame(data)
print(employee)

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    pass