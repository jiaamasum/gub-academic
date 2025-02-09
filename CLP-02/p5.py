# NumPy#1: Generate a 5x5 matrix of random integers and compute row-wise sums.

import numpy as np

random_matrix = np.random.randint(1, 101, (5, 5))

sum_of_rows = np.sum(random_matrix, axis=1)

print("Matrix:\n", random_matrix)
print("Sum By Row:", sum_of_rows)