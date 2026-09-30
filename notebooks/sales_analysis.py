"""
Superstore Sales Dataset — Exploratory Data Analysis
=====================================================
Answers the 9 business questions in the project brief:
  1. Sales by Region
  2. Profit by Category / Sub-Category
  3. Discount vs Profit Margin
  4. Shipping Mode Efficiency
  5. Top 5 Customers by Sales
  6. Top 10 Products by Sales Volume
  7. Regional Profitability (lowest region + drivers)
  8. Customer Segment Analysis by City
  9. Loss Leaders (high sales, negative profit)

Run:
    pip install -r requirements.txt
    python notebooks/sales_analysis.py
"""

import pandas as pd

pd.set_option("display.width", 150)

DATA_PATH = "data/Sales_Dataset.xlsx"


def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    """Load the Superstore dataset (sheet: 'Sales Dataset')."""
    df = pd.read_excel(path, sheet_name="Sales Dataset")
    # Profit Margin = Profit / Sales (already present in source, recomputed here for safety)
    df["Profit Margin"] = df["Profit"] / df["Sales"]
    return df


def q1_sales_by_region(df: pd.DataFrame) -> pd.Series:
    return df.groupby("Region")["Sales"].sum().sort_values(ascending=False)


def q2_profit_by_category(df: pd.DataFrame):
    by_cat = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
    by_subcat = df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False)
    return by_cat, by_subcat


def q3_discount_vs_margin(df: pd.DataFrame):
    summary = df.groupby("Discount Bucket").agg(
        Avg_Discount=("Discount", "mean"),
        Avg_Profit_Margin=("Profit Margin", "mean"),
        Order_Count=("Discount", "size"),
    )
    correlation = df["Discount"].corr(df["Profit Margin"])
    return summary, correlation


def q4_shipping_mode(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Ship Mode").agg(
        Order_Count=("Ship Mode", "size"),
        Total_Profit=("Profit", "sum"),
        Avg_Profit=("Profit", "mean"),
    ).sort_values("Order_Count", ascending=False)


def q5_top_customers(df: pd.DataFrame, n: int = 5) -> pd.Series:
    return df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(n)


def q6_top_products(df: pd.DataFrame, n: int = 10):
    by_qty = df.groupby("Product Name")["Quantity"].sum().sort_values(ascending=False).head(n)
    by_sales = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(n)
    return by_qty, by_sales


def q7_regional_profitability(df: pd.DataFrame):
    by_region = df.groupby("Region")["Profit"].sum().sort_values()
    lowest_region = by_region.index[0]
    drivers = (
        df[df["Region"] == lowest_region]
        .groupby("Product Name")
        .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
        .sort_values("Sales", ascending=False)
        .head(10)
    )
    drivers["Margin"] = drivers["Profit"] / drivers["Sales"]
    return by_region, lowest_region, drivers


def q8_segment_by_city(df: pd.DataFrame):
    by_segment = df.groupby("Segment").agg(Sales=("Sales", "sum"), Profit=("Profit", "sum")).sort_values(
        "Sales", ascending=False
    )
    by_city_segment = (
        df.groupby(["City", "Segment"])
        .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
        .sort_values("Sales", ascending=False)
        .head(10)
    )
    return by_segment, by_city_segment


def q9_loss_leaders(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["Category", "Sub-Category"])
        .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
        .sort_values("Profit")
    )


def main():
    df = load_data()
    print(f"Loaded {len(df):,} rows, {df.shape[1]} columns\n")

    print("Q1 — Sales by Region\n", q1_sales_by_region(df), "\n")

    by_cat, by_subcat = q2_profit_by_category(df)
    print("Q2 — Profit by Category\n", by_cat, "\n")
    print("Q2 — Profit by Sub-Category\n", by_subcat, "\n")

    disc_summary, corr = q3_discount_vs_margin(df)
    print("Q3 — Discount buckets vs avg profit margin\n", disc_summary)
    print(f"Correlation(Discount, Profit Margin) = {corr:.3f}\n")

    print("Q4 — Shipping mode efficiency\n", q4_shipping_mode(df), "\n")

    print("Q5 — Top 5 customers by sales\n", q5_top_customers(df), "\n")

    qty, sales = q6_top_products(df)
    print("Q6 — Top 10 products by quantity\n", qty, "\n")
    print("Q6 — Top 10 products by sales value\n", sales, "\n")

    by_region, lowest, drivers = q7_regional_profitability(df)
    print("Q7 — Profit by region (ascending)\n", by_region)
    print(f"Lowest-profit region: {lowest}\n", drivers, "\n")

    by_segment, by_city_segment = q8_segment_by_city(df)
    print("Q8 — Sales/Profit by segment\n", by_segment)
    print("Q8 — Top city+segment combos\n", by_city_segment, "\n")

    print("Q9 — Sales/Profit by sub-category (ascending profit — loss leaders first)\n", q9_loss_leaders(df))


if __name__ == "__main__":
    main()
