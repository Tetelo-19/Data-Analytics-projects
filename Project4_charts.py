import pandas as pd
import matplotlib.pyplot as plt

df = pd. read_csv("cleaned_dataset.csv")


df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

revenue_by_product = df.groupby("product")["TotalPrice"].sum().sort_values(ascending=False)

plt.figure(figsize=(9, 5))
revenue_by_product.plot(kind="bar", color="skyblue")
plt.title("Revenue by product - Top sellers drive the majority of revenue", fontsize=12, fontweight="bold")

plt.xlabel("Product")
plt.ylabel(" Total Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("CHART1,revenue_by_product.png", dpi=150)
plt.close()

plt.figure(figsize=(9, 5))
plt.plot(revenue_over_time.index, revenue_over_time.values, marker="o", color="skyblue", linewidth=2)
plt.title("Monthly Revenue Trend — Tracking growth over time", fontsize=12, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("CHART2_revenue_over_time.png", dpi=150)
plt.close()

orders_by_status = df["OrderStatus"].value_counts()
 
plt.figure(figsize=(7, 5))
orders_by_status.plot(kind="bar", color="orange")
plt.title("Orders by Status — Most orders are successfully delivered", fontsize=12, fontweight="bold")
plt.xlabel("Order status")
plt.ylabel("Number of orders")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("CHART3_orders_by_status.png", dpi=150)
plt.close()


print("All 3 charts saved: chart1_revenue_by_product.png, chart2_revenue_trend.png, chart3_orders_by_status.png")
