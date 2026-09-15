from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

REQUIRED = {"date", "product", "category", "quantity", "unit_price", "unit_cost"}

def load_and_clean(path):
    df = pd.read_csv(path)
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    for col in ["quantity", "unit_price", "unit_cost"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["date", "product", "category", "quantity", "unit_price", "unit_cost"]).copy()
    df = df[(df["quantity"] > 0) & (df["unit_price"] >= 0) & (df["unit_cost"] >= 0)].copy()

    df["revenue"] = df["quantity"] * df["unit_price"]
    df["cost"] = df["quantity"] * df["unit_cost"]
    df["profit"] = df["revenue"] - df["cost"]
    return df

def run_analysis(data_path, output_dir):
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    df = load_and_clean(data_path)

    total_revenue = df["revenue"].sum()
    total_cost = df["cost"].sum()
    total_profit = df["profit"].sum()
    total_units = int(df["quantity"].sum())
    orders = len(df)
    margin = (total_profit / total_revenue * 100) if total_revenue else 0

    category = (
        df.groupby("category", as_index=False)
        .agg(revenue=("revenue", "sum"), profit=("profit", "sum"), units=("quantity", "sum"))
        .sort_values("revenue", ascending=False)
    )

    product = (
        df.groupby("product", as_index=False)
        .agg(revenue=("revenue", "sum"), profit=("profit", "sum"), units=("quantity", "sum"))
        .sort_values("revenue", ascending=False)
    )

    monthly = (
        df.assign(month=df["date"].dt.to_period("M").astype(str))
        .groupby("month", as_index=False)
        .agg(revenue=("revenue", "sum"), profit=("profit", "sum"))
    )

    category.to_csv(out / "category_summary.csv", index=False)
    product.to_csv(out / "product_summary.csv", index=False)
    monthly.to_csv(out / "monthly_summary.csv", index=False)

    plt.figure(figsize=(9, 5))
    plt.bar(category["category"], category["revenue"])
    plt.title("Revenue by Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(out / "revenue_by_category.png", dpi=160)
    plt.close()

    plt.figure(figsize=(9, 5))
    plt.plot(monthly["month"], monthly["revenue"], marker="o")
    plt.title("Monthly Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(out / "monthly_revenue.png", dpi=160)
    plt.close()

    report = f"""SALES ANALYSIS REPORT

Orders: {orders:,}
Units sold: {total_units:,}
Revenue: ${total_revenue:,.2f}
Cost: ${total_cost:,.2f}
Profit: ${total_profit:,.2f}
Profit margin: {margin:.2f}%

Top category by revenue: {category.iloc[0]["category"]}
Top product by revenue: {product.iloc[0]["product"]}
"""
    (out / "report.txt").write_text(report, encoding="utf-8")

    print(report)
    print(f"Outputs saved to: {out.resolve()}")

if __name__ == "__main__":
    run_analysis("data/sales.csv", "reports")
