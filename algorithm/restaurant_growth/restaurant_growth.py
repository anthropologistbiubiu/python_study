

import pandas as pd


"""
Customer 表:
+-------------+--------------+--------------+-------------+
| customer_id | name         | visited_on   | amount      |
+-------------+--------------+--------------+-------------+
| 1           | Jhon         | 2019-01-01   | 100         |
| 2           | Daniel       | 2019-01-02   | 110         |
| 3           | Jade         | 2019-01-03   | 120         |
| 4           | Khaled       | 2019-01-04   | 130         |
| 5           | Winston      | 2019-01-05   | 110         | 
| 6           | Elvis        | 2019-01-06   | 140         | 
| 7           | Anna         | 2019-01-07   | 150         |
| 8           | Maria        | 2019-01-08   | 80          |
| 9           | Jaze         | 2019-01-09   | 110         | 
| 1           | Jhon         | 2019-01-10   | 130         | 
| 3           | Jade         | 2019-01-10   | 150         | 
+-------------+--------------+--------------+-------------+

"""


def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    daily = customer.groupby("visited_on")[
        "amount"].sum().reset_index(name="amount").sort_values("visited_on")

    daily["amount7"] = daily["amount"].rolling(window=7, min_periods=7).sum()
    # average_amount
    daily["average_amount"] = (daily["amount7"]/7).round(2)

    result = daily[["visited_on", "amount7", "average_amount"]].reset_index(
        drop=True).rename(columns={"amount7": "amount"})

    result = result[result["average_amount"].notnull()].reset_index(drop=True)
    return result


data = {
    "customer_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3],
    "name": [
        "Jhon", "Daniel", "Jade", "Khaled", "Winston",
        "Elvis", "Anna", "Maria", "Jaze", "Jhon", "Jade"
    ],
    "visited_on": [
        "2019-01-01", "2019-01-02", "2019-01-03", "2019-01-04", "2019-01-05",
        "2019-01-06", "2019-01-07", "2019-01-08", "2019-01-09", "2019-01-10", "2019-01-10"
    ],
    "amount": [100, 110, 120, 130, 110, 140, 150, 80, 110, 130, 150]


}

df = pd.DataFrame(data)
print(restaurant_growth(df))
