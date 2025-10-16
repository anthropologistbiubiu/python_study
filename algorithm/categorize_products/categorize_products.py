

import pandas as pd

# 模拟输入数据
data = {
    'sell_date': ['2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30'],
    'product':   ['Headphone', 'Pencil', 'Mask', 'Basketball', 'Bible', 'Mask', 'T-shirt']
}

df = pd.DataFrame(data)


result = df.groupby("sell_date")['product'].apply(
    lambda x: ','.join(sorted(x))
).reset_index(drop=True)

print(result)
