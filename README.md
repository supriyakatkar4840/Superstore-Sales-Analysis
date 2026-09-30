# Superstore Sales Analysis & Dashboard

Exploratory data analysis on a retail "Superstore" order dataset (9,994 orders,
2015–2018), answering 9 core business questions and packaging the results
into a formula-driven Excel dashboard.

## Business questions answered

1. Which region has the highest total sales?
2. Which product categories/sub-categories are most profitable?
3. What is the relationship between discount rate and profit margin?
4. Which shipping mode is used most, and how does it correlate with profit?
5. Who are the top 5 customers by total sales?
6. What are the top 10 products by sales volume?
7. Which region has the lowest profitability, and why?
8. Which customer segment (by city) contributes most to sales & profit?
9. Which sub-categories are "loss leaders" — high sales, negative profit?

Full write-up of the answers: [`INSIGHTS.md`](./INSIGHTS.md)

## Repo structure

```
.
├── data/
│   └── Sales_Dataset.xlsx          # Raw source data (sheet: "Sales Dataset")
├── notebooks/
│   └── sales_analysis.py           # Reproducible pandas analysis (all 9 questions)
├── Superstore_Sales_Dashboard.xlsx # Deliverable: formula-driven Excel dashboard w/ charts
├── INSIGHTS.md                     # Written answers & key takeaways
├── requirements.txt
└── README.md
```

## How to reproduce

```bash
git clone <your-repo-url>
cd <repo-name>
pip install -r requirements.txt
python notebooks/sales_analysis.py
```

This prints the answer to every question to the console using pandas
`groupby`/aggregation — no hardcoded numbers, everything is computed from
`data/Sales_Dataset.xlsx`.

## About the Excel dashboard

`Superstore_Sales_Dashboard.xlsx` contains:

- **Dashboard** — KPI summary (total sales, profit, orders, margin) + headline
  insights + region/category charts
- **Sales Dataset** — the raw data table
- **Q1–Q9** — one sheet per question, each with a live formula table
  (`SUMIF`/`SUMIFS`/`AVERAGEIF`/`COUNTIF`/`CORREL`) referencing the raw data,
  a chart, and a written insight. Because the tables are formulas rather than
  pasted values, the whole workbook recalculates if the underlying data
  changes.

## Key insights (summary)

- **West** leads in sales (~$725K); **South** is lowest (~$392K).
- **Technology** and **Office Supplies** drive almost all profit; **Furniture**
  barely breaks even.
- Discount rate and profit margin are strongly negatively correlated
  (≈ **-0.86**) — margins turn negative once discounts exceed ~20%.
- **Standard Class** ships ~60% of orders; **First Class** is the most
  profitable per order.
- **Tables** is the clearest loss leader: $207K in sales but **-$17.7K**
  in profit.

See [`INSIGHTS.md`](./INSIGHTS.md) for the full breakdown.

## Tech stack

- Python 3, pandas, openpyxl
- Excel (formulas + native charts, no external BI tool required)

## Author
Supriya Katkar
