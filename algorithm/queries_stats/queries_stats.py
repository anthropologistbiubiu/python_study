import pandas as pd


def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:

    result = queries.groupby("query_name").apply(
        lambda g: pd.Series(
            {"quality": round((g["rating"]/g["position"]).mean(), 2),
             "poor_query_percentage": round((g["rating"] < 3).mean()*100, 2)
             }
        )
    )

    return result.reset_index()


data = {
    "query_name": ["Dog", "Dog", "Dog", "Cat", "Cat", "Cat"],
    "result": ["Golden Retriever", "German Shepherd", "Mule",
               "Shirazi", "Siamese", "Sphynx"],
    "position": [1, 2, 200, 5, 3, 7],
    "rating": [5, 5, 1, 2, 3, 4]
}

df = pd.DataFrame(data)


print(queries_stats(df))
