# NumPy#2: Create an array of 100 random values and normalize them between 0 and 1.
import numpy as np

random_values = np.random.rand(100)

normal = (random_values - np.min(random_values)) / (np.max(random_values) - np.min(random_values))

print(normal)
