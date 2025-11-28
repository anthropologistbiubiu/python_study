import pandas as pd


data = {
    "student_id": [101, 53, 128, 3],
    "name": ["Ulysses", "William", "Henry", "Henry"],
    "age": [13, 10, 6, 11],
}


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, ["name", "age"]]


students = pd.DataFrame(data)

if __name__ == "__main__":
    print(selectData(students))

