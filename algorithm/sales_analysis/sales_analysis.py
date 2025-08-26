"""
   输入：
   Sales 表：
   +---------+------------+------+----------+-------+
   | sale_id | product_id | year | quantity | price |
   +---------+------------+------+----------+-------+
   | 1       | 100        | 2008 | 10       | 5000  |
   | 2       | 100        | 2009 | 12       | 5000  |
   | 7       | 200        | 2011 | 15       | 9000  |
   +---------+------------+------+----------+-------+
   Product 表：
   +------------+--------------+
   | product_id | product_name |
   +------------+--------------+
   | 100        | Nokia        |
   | 200        | Apple        |
   | 300        | Samsung      |
   +------------+--------------+
   输出：
   +--------------+-------+-------+
   | product_name | year  | price |
   +--------------+-------+-------+
   | Nokia        | 2008  | 5000  |
   | Nokia        | 2009  | 5000  |
   | Apple        | 2011  | 9000  |
   +--------------+-------+-------+

   """

import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    result = sales.merge(
        product,
        how="inner",
        on="product_id",
    )
    return result[["product_name", "year", "price"]]
    print(result)


sales = pd.DataFrame(
    {
        "sale_id": [1, 2, 7],
        "product_id": [100, 100, 200],
        "year": [2008, 2009, 2011],
        "quantity": [10, 12, 15],
        "price": [5000, 5000, 9000],
    }
)


product = pd.DataFrame(
    {
        "product_id": [100, 200, 300],
        "product_name": ["Nokia", "Apple", "Samsung"],
    }
)


print(sales_analysis(sales, product))
