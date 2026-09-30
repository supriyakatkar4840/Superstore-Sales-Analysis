# Insights — Superstore Sales Analysis

Dataset: 9,994 orders | 2015–2018 | Total Sales **$2,297,201** | Total Profit
**$286,397** | Overall margin **12.5%**

---

### 1. Sales by Region
| Region | Total Sales |
|---|---|
| West | $725,458 |
| East | $678,781 |
| Central | $501,240 |
| South | $391,722 |

**West** has the highest total sales; **South** is lowest, at roughly half of West.

### 2. Profit by Category / Sub-Category
Technology ($145,455) and Office Supplies ($122,491) generate nearly all
profit; Furniture contributes only $18,451 despite meaningful sales volume.
Most profitable sub-categories: **Copiers, Phones, Accessories**. Least
profitable: **Supplies, Bookcases, Tables** (all net-negative).

### 3. Discount Impact on Profit Margin
Correlation between discount rate and profit margin: **-0.86** (strong
negative). Orders with no discount average **34.0%** margin; once discounts
pass ~20%, average margin goes negative, bottoming out at **-113.9%** average
margin for 50%+ discounts.

### 4. Shipping Mode Efficiency
| Ship Mode | Orders | Total Profit | Avg Profit/Order |
|---|---|---|---|
| Standard Class | 5,968 | $164,089 | $27.49 |
| Second Class | 1,945 | $57,447 | $29.54 |
| First Class | 1,538 | $48,970 | $31.84 |
| Same Day | 543 | $15,892 | $29.27 |

Standard Class is used most (~60% of orders) and produces the most total
profit by volume; **First Class is the most profitable per order**.

### 5. Top 5 Customers by Sales
1. Sean Miller — $25,043
2. Tamara Chand — $19,052
3. Raymond Buch — $15,117
4. Tom Ashbrook — $14,596
5. Adrian Barton — $14,474

### 6. Top 10 Products
**By quantity sold:** Staples, Staple envelope, Easy-staple paper, Staples in
misc. colors, KI Adjustable-Height Table, Avery Non-Stick Binders, Storex
Dura Pro Binders, GBC Premium Transparent Covers, Situations Contoured
Folding Chairs, Staple-based wall hangings.

**By sales value:** led by the Canon imageCLASS 2200 Advanced Copier
($61,600), followed by the Fellowes PB500 binding machine, Cisco TelePresence
system, and HON 5400 task chairs.

### 7. Regional Profitability
**Central** is the least profitable region ($39,706 total profit — well
below West's $108,418) despite respectable sales. Several of its top-selling
products by value — the Lexmark MX611dhe printer, GBC DocuBind P400, and
Fellowes PB500 binding machine — **sell at a net loss** there, dragging the
region's overall profitability down even though top-line sales look healthy.

### 8. Customer Segment Analysis
| Segment | Sales | Profit |
|---|---|---|
| Consumer | $1,161,401 | $134,119 |
| Corporate | $706,146 | $91,979 |
| Home Office | $429,653 | $60,299 |

**Consumer** is the dominant segment. At the city level, **New York City
Consumer** is the single largest contributor ($136,870 sales / $30,619
profit). **Philadelphia Consumer** is a notable outlier — $63,203 in sales
but a **net loss** of -$6,134.

### 9. Loss Leaders
| Category | Sub-Category | Sales | Profit |
|---|---|---|---|
| Furniture | Tables | $206,966 | **-$17,725** |
| Furniture | Bookcases | $114,880 | -$3,473 |
| Office Supplies | Supplies | $46,674 | -$1,189 |

**Tables** is the clearest loss leader in the catalog — the single largest
sales-vs-profit mismatch in the dataset, consistent with the heavy
discounting pattern identified in Q3.

---

## Recommendations
- Cap discounts on Tables, Bookcases, and Machines at ~15–20%, where margin
  is still positive on average.
- Investigate Central-region pricing/discount policy on printers and binding
  machines specifically.
- Double down on Technology and Office Supplies marketing/inventory — they
  carry the business's profit.
- Look into why Philadelphia's Consumer segment loses money despite strong
  sales (product mix or local discounting practice).
