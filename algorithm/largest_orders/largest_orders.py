import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:

    result = orders.groupby("customer_number")["order_number"].count()
    max = result.max()

    customer_index = result[result == max].index
    result = pd.DataFrame(customer_index)
    return result


"""
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+

"""
datas = {"order_number": [1, 2, 3, 4], "customer_number": [1, 2, 3, 3]}
df = pd.DataFrame(datas)
print(largest_orders(df))
