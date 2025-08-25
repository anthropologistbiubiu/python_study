import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    counts = (
        actor_director.groupby(["actor_id", "director_id"]
                               ).size().to_frame("count")
    )
    result = counts[counts["count"] >= 3].reset_index()
    return result[["actor_id", "director_id"]]


"""
示例 1：

输入：
ActorDirector 表：
+-------------+-------------+-------------+
| actor_id    | director_id | timestamp   |
+-------------+-------------+-------------+
| 1           | 1           | 0           |
| 1           | 1           | 1           |
| 1           | 1           | 2           |
| 1           | 2           | 3           |
| 1           | 2           | 4           |
| 2           | 1           | 5           |
| 2           | 1           | 6           |
+-------------+-------------+-------------+
输出：
+-------------+-------------+
| actor_id    | director_id |
+-------------+-------------+
| 1           | 1           |
+-------------+-------------+
解释：
唯一的 id 对是 (1, 1)，他们恰好合作了 3 次。

"""


data = {
    "actor_id": [1, 1, 1, 1, 1, 2, 2],
    "director_id": [1, 1, 1, 2, 2, 1, 1],
    "timestamp": [0, 1, 2, 3, 4, 5, 6],
}

pf = pd.DataFrame(data)
print(actors_and_directors(pf))
