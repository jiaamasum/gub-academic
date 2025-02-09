# Pandas#1: Load a CSV file of sales data and compute total revenue per product.

import pandas as pd

file_for_data = pd.read_csv("CLP-02/local_data.csv")

total_revenue = file_for_data.groupby('Product')['Revenue'].sum()

print(total_revenue)
