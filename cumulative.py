import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the lesson.db database
conn = sqlite3.connect("db/lesson.db")

# SQL query to get order_id and total_price per order
query = """
    SELECT o.order_id, SUM(li.quantity * p.price) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
"""

# Load data into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Optional: define custom cumulative function (for understanding)
# def cumulative(row):
#     totals_above = df['total_price'][0:row.name + 1]
#     return totals_above.sum()
# df['cumulative'] = df.apply(cumulative, axis=1)

# Efficient built-in cumulative sum
df['cumulative'] = df['total_price'].cumsum()

# Plotting the cumulative revenue
plt.figure(figsize=(10, 6))
df.plot(
    kind='line',
    x='order_id',
    y='cumulative',
    legend=False,
    marker='o',
    color='green'
)

plt.title("📈 Cumulative Revenue Over Orders", fontsize=14)
plt.xlabel("Order ID", fontsize=12)
plt.ylabel("Cumulative Revenue ($)", fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()
