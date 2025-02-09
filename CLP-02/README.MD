#LabPerformance02-PythonTools

# Problem 1: List - Remove Duplicates and Sort in Ascending Order  
# Goal: Given a list of numbers, remove duplicates and sort the list in ascending order.

number_list = [4, 2, 7, 3, 2, 8, 4, 1]

sorted_list = sorted(set(number_list))

print("Sorted Unique List:", sorted_list)


#   Problem 2: Set - Find Common Elements Between Two Lists  
# Goal: Find the common elements between two lists using sets.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

elements = set(list1) & set(list2)

print("Common Elements:", elements)


#   Problem 3: Tuple - Sort Student Records by Grade  
# Goal: Create a tuple of student records (name, age, grade) and sort them by grade.

students_info = [("Masum", 22, 85), ("Jia", 22, 78), ("Nabil", 22, 92), ("Roy", 22, 88)]

final_students = sorted(students_info, key=lambda x: x[2])

print("Sorted Students by Grade:", final_students)


#   Problem 4: Dictionary - Count Word Occurrences in a Text  
# Goal: Given a text, count the occurrences of each word and store them in a dictionary.

original_text = "This is Masum Jia. Masum is a student. Jia is also a student."

spllited_words = original_text.split()

word_count = {}

for word in spllited_words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word Count Dictionary:", word_count)


#   Problem 5: NumPy - Generate a 5x5 Matrix of Random Integers and Compute Row-Wise Sums  
# Goal: Create a 5×5 matrix of random integers and compute the sum of each row.

import numpy as np

random_matrix = np.random.randint(1, 101, (5, 5))

sum_of_rows = np.sum(random_matrix, axis=1)

print("Random Matrix:\n", random_matrix)
print("Row-wise Sums:", sum_of_rows)


#   Problem 6: NumPy - Create an Array of 100 Random Values and Normalize Them  
# Goal: Generate 100 random values and normalize them between 0 and 1.

random_values = np.random.rand(100)

normal = (random_values - np.min(random_values)) / (np.max(random_values) - np.min(random_values))

print("Normalized Values:\n", normal)


#   Problem 7: Pandas - Compute Total Revenue Per Product from a CSV File  
# Goal: Read a sales dataset and compute total revenue per product.

import pandas as pd

file_for_data = pd.read_csv("CLP-02/local_data.csv")
total_revenue = file_for_data.groupby('Product')['Revenue'].sum()
print("Total Revenue Per Product:\n", total_revenue)


#   Problem 8: Pandas - Fill Missing Values with Column-Wise Means  
# Goal: Handle missing values by replacing them with column-wise means.

file_for_mv = pd.read_csv("CLP-02/missing_value.csv")
file_for_mv.columns = file_for_mv.columns.str.strip()  
file_for_mv['Revenue'] = pd.to_numeric(file_for_mv['Revenue'], errors='coerce')
file_filled = file_for_mv.fillna(file_for_mv.mean(numeric_only=True))
print("Data After Filling Missing Values:\n", file_filled)


#   Problem 9: Matplotlib - Plot a Line Graph for Temperature Variations Over a Week  
# Goal: Visualize temperature changes over a week using a line graph.

import matplotlib.pyplot as plt

days = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]

temperatures = [30, 32, 33, 31, 29, 28, 27]

plt.figure(figsize=(8, 5))
plt.plot(days, temperatures, marker='o', linestyle='-', color='b')
plt.xlabel("Day")
plt.ylabel("Temperature in °C")
plt.title("Temperature Over a Week")
plt.grid()
plt.show()


#   Problem 10: Matplotlib - Create a Bar Chart Comparing Sales Revenue Across Regions  
# Goal: Compare sales revenue across multiple regions using a bar chart.

regions = ["Dhaka", "Sylhet", "Chittagong", "Rajshahi"]
sales_figure = [1500000, 1800000, 1200000, 1700000]

plt.figure(figsize=(8, 5))
plt.bar(regions, sales_figure, color='green')
plt.xlabel("Regions")
plt.ylabel("Sales Revenue in BDT")
plt.title("Sales Revenue Comparison Across Regions")

for i, value in enumerate(sales_figure):
    plt.text(i, value + 50000, f"{value:,}", ha='center', fontsize=10, fontweight='bold')

plt.grid(axis='y')
plt.show()
