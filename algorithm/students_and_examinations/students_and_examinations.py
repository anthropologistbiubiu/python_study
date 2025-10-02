import pandas as pd

# Students 表
students = pd.DataFrame({
    "student_id": [1, 2, 13, 6],
    "student_name": ["Alice", "Bob", "John", "Alex"]
})

# Subjects 表
subjects = pd.DataFrame({
    "subject_name": ["Math", "Physics", "Programming"]
})

# Examinations 表
exams = pd.DataFrame({
    "student_id": [1, 1, 1, 2, 1, 1, 13, 13, 13, 2, 1],
    "subject_name": [
        "Math", "Physics", "Programming",
        "Programming", "Physics", "Math",
        "Math", "Programming", "Physics",
        "Math", "Math"
    ]
})


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    cross = students.merge(subjects,  how="cross")
    exams["cnt"] = 1
    merged = cross.merge(exams, on=["student_id", "subject_name"], how="left")
    # result = merged.groupby(
    #   ["student_id", "subject_name"], as_index=False).count().sort_values(["student_id", "subject_name"]).reset_index(drop=True)
    result = merged.groupby(["student_id", "subject_name"], as_index=False).agg(attended_exams=(
        "cnt", "sum")).sort_values(["student_id", "subject_name"]).reset_index(drop=True)

    result = students.merge(result, on="student_id", how="right")
    result.rename(columns={"cnt": "attended_exams"}, inplace=True)
    return result


if __name__ == "__main__":
    print(students_and_examinations(students, subjects, exams))
