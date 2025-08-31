

import pandas as pd


"""
输入：
Product table:
+------------+--------------+------------+
| product_id | product_name | unit_price |
+------------+--------------+------------+
| 1          | S8           | 1000       |
| 2          | G4           | 800        |
| 3          | iPhone       | 1400       |
+------------+--------------+------------+
Sales table:
+-----------+------------+----------+------------+----------+-------+
| seller_id | product_id | buyer_id | sale_date  | quantity | price |
+-----------+------------+----------+------------+----------+-------+
| 1         | 1          | 1        | 2019-01-21 | 2        | 2000  |
| 1         | 2          | 2        | 2019-02-17 | 1        | 800   |
| 2         | 2          | 3        | 2019-06-02 | 1        | 800   |
| 3         | 3          | 4        | 2019-05-13 | 2        | 2800  |
+-----------+------------+----------+------------+----------+-------+
输出：
+-------------+--------------+
| product_id  | product_name |
+-------------+--------------+
| 1           | S8           |
+-------------+--------------+
解释:
id 为 1 的产品仅在 2019 年春季销售。
id 为 2 的产品在 2019 年春季销售，但也在 2019 年春季之后销售。
id 为 3 的产品在 2019 年春季之后销售。
我们只返回 id 为 1 的产品，因为它是 2019 年春季才销售的产品。

"""


def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    pass


product_data = {
    "product_id": [1, 2, 3],
    "product_name": ["S8", "G4", "iPhone"],
    "unit_price": [1000, 800, 1400]
}
product_df = pd.DataFrame(product_data)

# Sales table DataFrame
sales_data = {
    "seller_id": [1, 1, 2, 3],
    "product_id": [1, 2, 2, 3],
    "buyer_id": [1, 2, 3, 4],
    "sale_date": ["2019-01-21", "2019-02-17", "2019-06-02", "2019-05-13"],
    "quantity": [2, 1, 1, 2],
    "price": [2000, 800, 800, 2800]
}
sales_df = pd.DataFrame(sales_data)
