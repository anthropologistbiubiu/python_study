

import pandas as pd

# 模拟输入数据
data = {
    'sell_date': ['2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30'],
    'product':   ['Headphone', 'Pencil', 'Mask', 'Basketball', 'Bible', 'Mask', 'T-shirt']
}

df = pd.DataFrame(data)


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:

    activities = activities.drop_duplicates()

    '''
    result = activities.groupby("sell_date").apply(lambda x: pd.DataFrame(
        {'products': [','.join(sorted(x['product']))]}))
    '''

    result = activities.groupby("sell_date")['product'].apply(
        lambda x: ','.join(sorted(x))
    ).reset_index(drop=True)

    result['num_sold'] = result["products"].apply(lambda x: len(x.split(",")))
    result = result.sort_values("sell_date")
    result = result[['sell_date', 'num_sold', 'products']]
    return result


print(categorize_products(df))
