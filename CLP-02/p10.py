#Matplotlib#2: Create a bar chart comparing sales revenue across different regions.

import matplotlib.pyplot as plt

regions = ["Dhaka", "Sylhet", "Chittagong", "Rajshahi"]
sales_figure = [1500000, 1800000, 1200000, 1700000]

plt.bar(regions, sales_figure, color='green')

plt.xlabel("Regions")
plt.ylabel("Sales Revenue in BDT")
plt.title("Sales Revenue Comparison Across Regions")

for i, value in enumerate(sales_figure):
    plt.text(i, value + 50000, f"{value:,}", ha='center', fontsize=10, fontweight='bold')

plt.show()
