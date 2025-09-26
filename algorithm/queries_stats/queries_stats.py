import pandas as pd


def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:

    queries["ration"] = queries["rating"] / queries["position"]
    queries["ration"] = queries["rating"] / queries["position"]
    queries["is_poor"] = queries["rating"] < 3
    result = queries.groupby("query_name").agg(
        quality=("ration", "mean"),
        poor_query_percentage=("is_poor", "mean"),
    )
    result["quality"] = result["quality"].round(2)
    result["poor_query_percentage"] = (
        result["poor_query_percentage"]*100).round(2)
    result = result.sort_values("query_name")
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
