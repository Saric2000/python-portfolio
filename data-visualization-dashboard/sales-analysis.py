import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data-visualization-dashboard/sales_data.csv')

# Add a column for total sales
df["Total Sales (€)"] = df["Price"] * df["Quantity"]

# Display first few rows
print("Data Preview:\n", df.head())

# Total sales by product
sales_by_product = df.groupby("Product")["Total Sales (€)"].sum().sort_values(ascending=False)
print("\nTotal Sales by Product:\n", sales_by_product)

# Total sales by category
sales_by_category = df.groupby("Category")["Total Sales (€)"].sum()
print("\nTotal Sales by Category:\n", sales_by_category)

# Sales by product
plt.figure(figsize=(8,5))
sales_by_product.plot(kind="bar", color="teal")
plt.title("Total Sales by Product")
plt.ylabel("Total Sales (€)")
plt.xlabel("Product")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Sales by category
plt.figure(figsize=(6,4))
sales_by_category.plot(kind="pie", autopct="%1.1f%%", startangle=9)
plt.title("Sales Share by Category")
plt.ylabel("")
plt.show()

# Daily sales trend
daily_sales = df.groupby("Date")["Total Sales (€)"].sum()
plt.figure(figsize=(8,5))
daily_sales.plot(kind="line", marker="o", color="orange")
plt.title("Daily Sales Trend")
plt.ylabel("Total Sales (€)")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
