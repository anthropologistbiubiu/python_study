import pandas as pd


def sales_person(
    sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame
) -> pd.DataFrame:

    orders_company = orders.merge(
        company,
        how="inner",
    )
    sales_id = orders_company[orders_company["name"] == "RED"]["sales_id"]
    result = sales_person[~sales_person["sales_id"].isin(sales_id)]
    return result["name"].to_frame().reset_index(drop=True)


salesperson = pd.DataFrame(
    {"sales_id": [1, 2, 3, 4], "name": ["Alice", "Bob", "Charlie", "David"]}
)


orders = pd.DataFrame(
    {
        "order_id": [101, 102, 103, 104, 105],
        "sales_id": [1, 2, 2, 3, 4],
        "com_id": [10, 20, 10, 30, 20],
    }
)

company = pd.DataFrame(
    {"com_id": [10, 20, 30], "name": ["RED", "BLUE", "GREEN"]})

new_data = sales_person(salesperson, company, orders)
print(new_data)


"""
输入：
SalesPerson 表:
+----------+------+--------+-----------------+------------+
| sales_id | name | salary | commission_rate | hire_date  |
+----------+------+--------+-----------------+------------+
| 1        | John | 100000 | 6               | 4/1/2006   |
| 2        | Amy  | 12000  | 5               | 5/1/2010   |
| 3        | Mark | 65000  | 12              | 12/25/2008 |
| 4        | Pam  | 25000  | 25              | 1/1/2005   |
| 5        | Alex | 5000   | 10              | 2/3/2007   |
+----------+------+--------+-----------------+------------+
Company 表:
+--------+--------+----------+
| com_id | name   | city     |
+--------+--------+----------+
| 1      | RED    | Boston   |
| 2      | ORANGE | New York |
| 3      | YELLOW | Boston   |
| 4      | GREEN  | Austin   |
+--------+--------+----------+
Orders 表:
+----------+------------+--------+----------+--------+
| order_id | order_date | com_id | sales_id | amount |
+----------+------------+--------+----------+--------+
| 1        | 1/1/2014   | 3      | 4        | 10000  |
| 2        | 2/1/2014   | 4      | 5        | 5000   |
| 3        | 3/1/2014   | 1      | 1        | 50000  |
| 4        | 4/1/2014   | 1      | 4        | 25000  |
+----------+------------+--------+----------+--------+

select s.name from SalesPerson as s where not exists (
    select 1 from Orders as o join Company as c on o.com_id = c.com_id where c.com_name = 'RED' and s.sales_id = o.sales_id 
); 




输出：
+------+
| name |
+------+
| Amy  |
| Mark |
| Alex |
+------+
"""
