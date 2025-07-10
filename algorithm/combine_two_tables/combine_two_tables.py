import pandas as pd



persons = pd.DataFrame({
    'PersonId':[1,2,3,4],
    'FirstName': ['John', 'Jane', 'Alice', 'Bob'],
    'LastName':  ['Doe',  'Smith','Johnson','Brown']
})


addresses = pd.DataFrame({
    'AddressId': [101, 102, 103],
    'PersonId':  [1,   2,   4],
    'City':      ['New York', 'Los Angeles', 'Chicago'],
    'State':     ['NY',       'CA',          'IL']
})

result = pd.merge(
    persons,
    addresses[['PersonId', 'City', 'State']],  # 只取需要的列
    on='PersonId',
    how='left'  # 保留 persons 中所有记录，address 缺失时 City/State 为 NaN
)


result = result[['LastName', 'FirstName', 'City', 'State']]

# --- 打印结果 ---
print(result.to_string(index=False))