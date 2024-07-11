from datetime import datetime, timedelta
import pandas as pd

time = int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds())
print(time)

# Step 2: Generate a new time series index
current_time = datetime.now()
print(current_time)
interval = current_time - timedelta(hours=1)

# Assuming the original data has a frequency, e.g., '5T' for 5 minutes
frequency = '1s'  # Adjust this to match the frequency of your original data
new_index = pd.date_range(start=interval, end=current_time, freq=frequency)
print(type(new_index))

# for data in new_index:
#     print(int(data.timestamp()))


import pandas as pd
from datetime import datetime, timedelta

# Step 2: Generate a new time series index
current_time = datetime.now()
print("Current time:", current_time)
interval = current_time - timedelta(hours=1)
print("One hour ago:", interval)

# Assuming the original data has a frequency, e.g., '5T' for 5 minutes
frequency = '1s'  # Adjust this to match the frequency of your original data
new_index = pd.date_range(start=interval, end=current_time, freq=frequency)

# Print the new index
print("New index:", new_index)
