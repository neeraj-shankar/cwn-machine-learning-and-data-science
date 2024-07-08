import pandas as pd
import numpy as np
import time

"""
Vectorized Operation
---------------------------------------------------------------------------------------------------
Vectorized operations are performed element-wise on an entire array (Series or DataFrame column) 
at once, leveraging low-level optimizations and native code execution, often via NumPy. 

These operations are highly optimized and can be significantly faster than iterating through elements one by one.


apply operation
---------------------------------------------------------------------------------------------------
The apply method is more flexible than vectorized operations. It allows you to apply a custom function
to each element, row, or column of a DataFrame. 

Because apply involves a Python-level function call for each operation, it's generally slower than
vectorized operations but is more flexible, as it can handle operations that cannot be vectorized directly.
"""

# Use Case for Vectorized Operations:
# Create  dataframe with random numbers
df = pd.DataFrame(np.random.rand(1000000, 3), columns=["A", "B", "C"])
print(df)

# Vectorized operation to add two columns
df['D'] = df['A'] + df['B']
print(df['D'])

# Vectorized operation to calculate the logarithm of a column
df['log_A'] = np.log(df['A'])
print(df['log_A'])


# Define a custom function that applies non-vectorizable logic
def custom_logic(row):
    if row['A'] > 0.5 and row['B'] < 0.5:
        return 'Condition 1'
    elif row['A'] < 0.5 and row['C'] > 0.5:
        return 'Condition 2'
    else:
        return 'Other'

# Use apply with a custom function across rows (axis=1)
start_time_vect = time.time()
df['Custom_Condition'] = df.apply(custom_logic, axis=1)
end_time_vect = time.time()
time_taken_vect = end_time_vect - start_time_vect
# print(f"Total time taken: {time_taken_vect} seconds")


# Vectorized operation to calculate the mean of two columns
start_time_vect = time.time()
df['mean_AB'] = (df['A'] + df['B']) / 2
end_time_vect = time.time()
time_taken_vect = end_time_vect - start_time_vect
print(f"Total time taken for mean calculation: {time_taken_vect} seconds")

# An equivalent, but less efficient approach using apply
start_time_apply = time.time()
df['mean_AB'] = df[['A', 'B']].apply(lambda row: (row['A'] + row['B']) / 2, axis=1)
end_time_apply = time.time()
time_taken_apply = end_time_apply - start_time_apply
print(f"Total time taken for mean calculation: {time_taken_apply} seconds")



