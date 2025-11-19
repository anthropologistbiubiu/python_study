import pandas as pd


data = {
    "product_id": [0, 1],
    "store1": [95, 70],
    "store2": [100, None],
    "store3": [105, 80],
}


df = pd.DataFrame(data)


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    result = pd.melt(
        products,
        id_vars="product_id",
        var_name="store",
        value_vars=["store1", "store2", "store3"],
        value_name="price",
    )
    result = (
        result[result["price"].notnull()]
        .sort_values(by=["product_id", "store"])
        .reset_index(drop=True)
    )
    return result


if __name__ == "__main__":
    print(rearrange_products_table(df))
