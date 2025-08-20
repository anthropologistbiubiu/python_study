
import pandas as pd


def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    number_counts = my_numbers["num"].value_counts()
    single_numbers = number_counts[number_counts == 1]
    max_value = single_numbers.index.max()
    # result = max_value if len(single_numbers) > 0 else None
    return pd.DataFrame({"num": [max_value]})
