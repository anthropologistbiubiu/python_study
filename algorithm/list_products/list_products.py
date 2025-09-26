import pandas as pd


def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = products.merge(
        orders,
        on="product_id",
        how="inner"
    )
    merged["date"] = pd.to_datetime(merged["order_date"])
    feb_data = merged[(merged["date"].dt.month == 2) &
                      (merged["date"].dt.year == 2020)]
    agg_data = feb_data.groupby("product_id")[
        "unit"].sum().reset_index()
    top_product = agg_data[agg_data["unit"] >= 100].reset_index()
    result = top_product.merge(
        products,
        on="product_id"
    )[["product_name", "unit"]]
    return result


products = pd.DataFrame({
    "product_id": [1, 2, 3, 4, 5],
    "product_name": ["Leetcode Solutions", "Jewels of Stringology", "HP", "Lenovo", "Leetcode Kit"],
    "product_category": ["Book", "Book", "Laptop", "Laptop", "T-shirt"]
})

orders = pd.DataFrame({
    "product_id": [1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5],
    "order_date": [
        "2020-02-05", "2020-02-10", "2020-01-18", "2020-02-11", "2020-02-17", "2020-02-24",
        "2020-03-01", "2020-03-04", "2020-03-04", "2020-02-25", "2020-02-27", "2020-03-01"
    ],
    "unit": [60, 70, 30, 80, 2, 3, 20, 30, 60, 50, 50, 50]
})


if __name__ == "__main__":
    print(list_products(products, orders))
