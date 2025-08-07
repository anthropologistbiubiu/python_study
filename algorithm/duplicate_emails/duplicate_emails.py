import pandas as pd

# 输入数据
data = {
    'id': [1, 2, 3],
    'email': ['a@b.com', 'c@d.com', 'a@b.com']
}
df = pd.DataFrame(data)

# 统计邮箱出现次数
email_counts = df['email'].value_counts()

# 取出重复的邮箱地址
duplicate_emails = email_counts[email_counts > 1].index
# 构建结果 DataFrame 并按要求重命名列
result = pd.DataFrame(duplicate_emails, columns=['Email'])

