import pandas as pd


def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    pass


data = {
    "query_name": ["Dog", "Dog", "Dog", "Cat", "Cat", "Cat"],
    "result": ["Golden Retriever", "German Shepherd", "Mule",
               "Shirazi", "Siamese", "Sphynx"],
    "position": [1, 2, 200, 5, 3, 7],
    "rating": [5, 5, 1, 2, 3, 4]
}

df = pd.DataFrame(data)


print(queries_stats(df))
