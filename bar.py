import pandas as pd
import matplotlib.pyplot as plt

# 1) 读取 CSV
df = pd.read_csv(
    "出库单托盘数据统计.csv",
    encoding="gb18030",
    sep=","
)

# 2) 计算每个出库单号的出库次数
order_times = df["出库单号"].value_counts().rename("outbound_times")
df = df.join(order_times, on="出库单号")

# 3) 将 “托盘下的sku数” 分区
def sku_bucket(n: int) -> str:
    if 0 < n <= 5:
        return "0-5"
    elif 5 < n <= 10:
        return "5-10"
    elif 10 < n <= 15:
        return "10-15"
    else:
        return "15+"

df["sku_range"] = df["托盘下的sku数"].astype(int).map(sku_bucket)

# 4) 统计：不同出库次数 × 不同 SKU 区间 的记录数
pivot = (
    df.groupby(["outbound_times", "sku_range"])
      .size()
      .unstack(fill_value=0)
      .sort_index()
)

# 5) 计算占比
pivot_prop = pivot.div(pivot.sum(axis=1), axis=0)

# 6) 绘制堆积条形图
fig, ax = plt.subplots()
bottom = pd.Series([0] * len(pivot_prop), index=pivot_prop.index)

for col in pivot_prop.columns:
    ax.bar(pivot_prop.index.astype(str), pivot_prop[col], bottom=bottom, label=col)
    bottom += pivot_prop[col]

ax.set_xlabel('出库次数')
ax.set_ylabel('占比')
ax.set_title('不同出库次数下各 SKU 区间占比')
ax.legend(title='SKU 区间', loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()