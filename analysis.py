import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype
from matplotlib.ticker import PercentFormatter


def main() -> None:
    # 1) Read data (file path stays Chinese,与绘图无关)
    df = pd.read_csv("出库单托盘数据统计.csv", encoding="gb18030")

    # 2) Pallet count per outbound order
    order_times = df["出库单号"].value_counts().rename("pallet_count")
    df = df.join(order_times, on="出库单号")

    # 3) Bucket "SKU count per pallet" into ordered ranges
    bucket_type = CategoricalDtype(
        categories=["0-5", "5-10", "10-15", "15+"], ordered=True
    )

    def sku_bucket(n: int) -> str:
        if 0 < n <= 5:
            return "0-5"
        elif 5 < n <= 10:
            return "5-10"
        elif 10 < n <= 15:
            return "10-15"
        else:
            return "15+"

    df["托盘下的sku数"] = pd.to_numeric(df["托盘下的sku数"], errors="coerce")
    df = df.dropna(subset=["托盘下的sku数"])
    df["sku_range"] = (
        df["托盘下的sku数"].astype(int).map(sku_bucket).astype(bucket_type)
    )

    # 4) Pivot table
    pivot_counts = (
        df.groupby(["pallet_count", "sku_range"])
        .size()
        .unstack(fill_value=0)
        .sort_index()
    )
    pivot_pct = pivot_counts.div(pivot_counts.sum(axis=1), axis=0)

    # 5) Plot
    fig, ax = plt.subplots(figsize=(14, 6), constrained_layout=True)
    pivot_pct.plot(kind="bar", stacked=True, ax=ax, width=0.8)

    # Show every N-th x-tick
    N = 2
    for i, lbl in enumerate(ax.xaxis.get_ticklabels()):
        lbl.set_visible(i % N == 0)

    plt.setp(ax.get_xticklabels(), rotation=0, ha="center", fontsize=9)

    ax.set_xlabel("Pallet Count", fontsize=12, labelpad=12)          # ASCII only
    ax.set_ylabel("Percentage", fontsize=12)                         # ASCII only
    ax.set_title("SKU Range Distribution by Pallet Count", fontsize=14)  # ASCII only
    ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    ax.legend(title="SKU Range", bbox_to_anchor=(1.02, 1), loc="upper left")

    plt.show()


if __name__ == "__main__":
    main()