import pandas as pd


def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    group_data = movie_rating.groupby(
        "user_id")["movie_id"].nunique().reset_index(name="cnt")
    max_cnt = group_data["cnt"].max()
    top_users = group_data[group_data["cnt"] == max_cnt].reset_index()
    merge_data = top_users.merge(users, on="user_id")
    top_user_name = merge_data["name"].min()

    feb_data = movie_rating[
        (movie_rating["created_at"].dt.year == 2020)
        & (movie_rating["created_at"].dt.month == 2)
    ]
    raing_data = (
        feb_data.groupby("movie_id")["rating"].mean(
        ).reset_index(name="avg_rating")
    )

    max_rating = raing_data["avg_rating"].max()

    top_rating_movies = raing_data[raing_data["avg_rating"] == max_rating]

    top_rating_movies_merge_data = top_rating_movies.merge(
        movies, on="movie_id")
    top_rating_movie_name = top_rating_movies_merge_data["title"].min()

    return pd.DataFrame({"result": [top_user_name, top_rating_movie_name]})


# 示例数据
movies = pd.DataFrame({
    "movie_id": [1, 2, 3],
    "title": ["Avengers", "Frozen 2", "Joker"]
})

users = pd.DataFrame({
    "user_id": [1, 2, 3, 4],
    "name": ["Daniel", "Monica", "Maria", "James"]
})

movierating = pd.DataFrame({
    "movie_id": [1, 1, 1, 1, 2, 2, 2, 3, 3],
    "user_id":  [1, 2, 3, 4, 1, 2, 3, 1, 2],
    "rating":   [3, 4, 2, 1, 5, 2, 2, 3, 4],
    "created_at": pd.to_datetime([
        "2020-01-12", "2020-02-11", "2020-02-12", "2020-01-01",
        "2020-02-17", "2020-02-01", "2020-03-01",
        "2020-02-22", "2020-02-25"
    ])
})


if __name__ == "__main__":
    print(movie_rating(movies, users, movierating))
