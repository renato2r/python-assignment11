import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("db/lesson.db")

# SQL query to get employee revenue
query = """
    SELECT last_name, SUM(price * quantity) AS revenue
    FROM employees e
    JOIN orders o ON e.employee_id = o.employee_id
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY e.employee_id;
"""

# Load data into a DataFrame
employee_results = pd.read_sql_query(query, conn)

# Close connection
conn.close()

# Plotting
plt.figure(figsize=(10, 6))
employee_results.plot(
    kind="bar",
    x="last_name",
    y="revenue",
    color="skyblue",
    legend=False
)

plt.title("Employee Revenue from Orders", fontsize=14)
plt.xlabel("Employee Last Name", fontsize=12)
plt.ylabel("Revenue ($)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
