import pandas as pd


def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    merge_data = prices.merge(
        units_sold,
        on="product_id",
        how="right",
    )
    merge_data = merge_data[(merge_data["purchase_date"] >= merge_data["start_date"])
                            & (merge_data["purchase_date"] <= merge_data["end_date"])]
    merge_data["total_price"] = merge_data["price"]*merge_data["units"]
    agg_data = merge_data.groupby(["product_id"]).agg(
        total_price_sum=("total_price", "sum"),
        total_unit_sum=("units", "sum")
    ).reset_index()
    agg_data["average_price"] = round(
        agg_data["total_price_sum"] / agg_data["total_unit_sum"], 2)
    result = agg_data[["product_id", "average_price"]]
    return result


prices_data = {
    'product_id': [1, 1, 2, 2],
    'start_date': ['2019-02-17', '2019-03-01', '2019-02-01', '2019-02-21'],
    'end_date': ['2019-02-28', '2019-03-22', '2019-02-20', '2019-03-31'],
    'price': [5, 20, 15, 30]
}
units_sold_data = {
    'product_id': [1, 1, 2, 2],
    'purchase_date': ['2019-02-25', '2019-03-01', '2019-02-10', '2019-03-22'],
    'units': [100, 15, 200, 30]
}

prices_df = pd.DataFrame(prices_data)
units_sold_df = pd.DataFrame(units_sold_data)

print(average_selling_price(prices_df, units_sold_df))
