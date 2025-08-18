import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:

    courses_counts = courses.groupby("class")["student"].count()
    print(courses_counts)
    courses_index = courses_counts[courses_counts >= 1].index
    print(courses_index)
    return pd.DataFrame({"class": courses_index})


# 示例数据
data = {
    "student": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
    "class":   ["Math", "English", "Math", "Biology", "Math", "Computer", "Math", "Math", "Math"]
}
courses = pd.DataFrame(data)
print(find_classes(courses))
