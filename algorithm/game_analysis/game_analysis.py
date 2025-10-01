

import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['event_date'] = pd.to_datetime(activity['event_date'])
    result = activity.groupby(
        "player_id")['event_date'].min().reset_index(name='first_login')
    return result
    pass


if __name__ == "__main__":

    data = {
        'player_id': [1, 1, 2, 3, 3],
        'device_id': [2, 2, 3, 1, 4],
        'event_date': ['2016-03-01', '2016-05-02', '2017-06-25', '2016-03-02', '2018-07-03'],
        'games_played': [5, 6, 1, 0, 5]
    }

    df = pd.DataFrame(data)
    print(game_analysis(df))
