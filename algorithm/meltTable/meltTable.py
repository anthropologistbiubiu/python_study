import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    result = report.melt(
        id_vars="product",
        var_name="quarter",
        value_vars=["quarter_1", "quarter_2", "quarter_3", "quarter_4"],
        value_name="sale",
    )
    return result


data = {
    "product": ["Umbrella", "SleepingBag"],
    "quarter_1": [417, 800],
    "quarter_2": [224, 936],
    "quarter_3": [379, 93],
    "quarter_4": [611, 875],
}

"""
+-------------+-----------+-------+
| product     | quarter   | sales |
+-------------+-----------+-------+
| Umbrella    | quarter_1 | 417   |
| SleepingBag | quarter_1 | 800   |
| Umbrella    | quarter_2 | 224   |
| SleepingBag | quarter_2 | 936   |
| Umbrella    | quarter_3 | 379   |
| SleepingBag | quarter_3 | 93    |
| Umbrella    | quarter_4 | 611   |
| SleepingBag | quarter_4 | 875   |
+-------------+-----------+-------+

"""
report = pd.DataFrame(data)
print(report)


if __name__ == "__main__":
    print(meltTable(report=report))

