import pandas as pd


def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    result = cinema[(cinema["description"] != "boring")
                    & (cinema["id"] % 2 == 1)]
    # result = result[result["id"] % 2 == 1]
    return result.sort_values(by="rating", ascending=False)
