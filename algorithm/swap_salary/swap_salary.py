import pandas as pd


def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary["sex"].replace({"m": "f", "f": "m"}, inplace=True)
    return salary


if __name__ == "__main__":
    data = pd.DataFrame(
        {
            "id": [1, 2, 3, 4],
            "name": ["A", "B", "C", "D"],
            "sex": ["m", "f", "m", "f"],
            "salary": [2500, 1500, 5500, 500],
        }
    )
    print(swap_salary(data))
