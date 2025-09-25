import pandas as pd


def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    pass


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
