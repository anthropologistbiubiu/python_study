

import pandas as pd


def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:

    is_triangle = (triangle['a'] + triangle['b'] > triangle['c']) & (
        triangle['a'] + triangle['c'] > triangle['b']) & (
        triangle['b'] + triangle['c'] > triangle['a']
    )
    triangle['triangle'] = is_triangle.map(lambda x: 'Yes' if x else 'No')

    return triangle


triangle = pd.DataFrame({
    "a": [3, 1, 2],
    "b": [4, 2, 3],
    "c": [5, 3, 5]
})

print(triangle_judgement(triangle))
