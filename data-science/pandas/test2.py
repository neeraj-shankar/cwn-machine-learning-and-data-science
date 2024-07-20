import numpy as np


# Generate 10 random values from a uniform distribution between 0 and 100
random_values = np.random.uniform(0, 100, 10)

print(random_values)
# Round the values to 2 decimal places using list comprehension
rounded_values = [round(value, 2) for value in random_values]

print(rounded_values)
