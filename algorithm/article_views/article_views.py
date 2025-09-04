import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:

    viewer_eq_author = views[views["author_id"] == views["viewer_id"]]
    result = viewer_eq_author[["author_id"]].drop_duplicates(
    ).rename(columns={"author_id": "id"})
    sort_df = result.sort_values(by="id", ascending=True)
    return sort_df


data = {
    "article_id": [1, 1, 2, 2, 4, 3, 3],
    "author_id":  [3, 3, 7, 7, 7, 4, 4],
    "viewer_id":  [5, 6, 7, 6, 1, 4, 4],
    "view_date":  [
        "2019-08-01",
        "2019-08-02",
        "2019-08-01",
        "2019-08-02",
        "2019-07-22",
        "2019-07-21",
        "2019-07-21"
    ]
}


df = pd.DataFrame(data)


print(article_views(df))
