import pandas as pd
import sqlite3

# 1. Load your cleaned dataset from Project 1/2
df = pd.read_csv("cleaned_dataset.csv")

# 2. Create an in-memory SQLite database and load the data into a table called 'orders'
conn = sqlite3.connect(":memory:")
df.to_sql("orders", conn, index=False, if_exists="replace")

# 3. Helper function to run a query and print results nicely
def run_query(title, query):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)
    result = pd.read_sql_query(query, conn)
    print(result)
    return result

# ---------- QUERY 1: Basic SELECT + WHERE ----------
run_query(
    "Orders with status 'Delivered'",
    """
    SELECT OrderID, CustomerID, Product, TotalPrice, OrderStatus
    FROM orders
    WHERE OrderStatus = 'Delivered';
    """
)

# ---------- QUERY 2: WHERE with a numeric condition ----------
run_query(
    "Orders above 100 in total price",
    """
    SELECT OrderID, CustomerID, TotalPrice
    FROM orders
    WHERE TotalPrice > 100;
    """
)

# ---------- QUERY 3: ORDER BY ----------
run_query(
    "Top 10 highest value orders",
    """
    SELECT OrderID, CustomerID, TotalPrice
    FROM orders
    ORDER BY TotalPrice DESC
    LIMIT 10;
    """
)

# ---------- QUERY 4: GROUP BY + COUNT ----------
run_query(
    "Number of orders per status",
    """
    SELECT OrderStatus, COUNT(*) AS num_orders
    FROM orders
    GROUP BY OrderStatus;
    """
)

# ---------- QUERY 5: GROUP BY + SUM ----------
run_query(
    "Total revenue per payment method",
    """
    SELECT PaymentMethod, SUM(TotalPrice) AS total_revenue
    FROM orders
    GROUP BY PaymentMethod
    ORDER BY total_revenue DESC;
    """
)

# ---------- QUERY 6: GROUP BY + AVG ----------
run_query(
    "Average order value per product",
    """
    SELECT Product, AVG(TotalPrice) AS avg_order_value, COUNT(*) AS num_orders
    FROM orders
    GROUP BY Product
    ORDER BY avg_order_value DESC;
    """
)

# ---------- QUERY 7: GROUP BY + SUM on quantity ----------
run_query(
    "Total units sold per product",
    """
    SELECT Product, SUM(Quantity) AS total_units_sold
    FROM orders
    GROUP BY Product
    ORDER BY total_units_sold DESC;
    """
)

# ---------- QUERY 8: Combined WHERE + GROUP BY + ORDER BY ----------
run_query(
    "Revenue per product (delivered orders only)",
    """
    SELECT Product, SUM(TotalPrice) AS revenue
    FROM orders
    WHERE OrderStatus = 'Delivered'
    GROUP BY Product
    ORDER BY revenue DESC;
    """
)

conn.close()
print("\nAll queries completed.")

