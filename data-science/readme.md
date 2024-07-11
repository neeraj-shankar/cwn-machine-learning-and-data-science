
## A Quick Quide to use Jupyter

## Useful shortcuts

1. To Run code in a shell

```sh
SHIFT + ENTER
```

2. Switch from code to markdown text

```sh
ESC and then M
```

4. Switch to Command mode from code edit mode

```sh
ESC
```

5. To get a new shell above or below current shell

```sh
a or b
```

5. To import an image to jupyter notebook

```sh
! [](image_file_name)
```

5. To run terminal command in Jupyter

```sh
!ls
```

# Notes on Pandas Library

## DataFrames 

- DataFrame is a two-dimensional labeled data structure provided by the Pandas library. 
- It is similar to a spreadsheet or SQL table, where data is organized into rows and columns. 
- Each column can have a different data type (e.g., integer, float, string)

### Creating DataFrames
- DataFrames can be created from various data sources such as dictionaries, lists, NumPy arrays, or from external files like CSV, Excel, SQL databases, etc.
- Some commonly used functions for creating DataFrames include pd.DataFrame() and pd.read_csv().
```sh
```

### Viewing Data:
- **head(n)**: Returns the first n rows of the DataFrame.
- **tail(n)**: Returns the last n rows of the DataFrame.
- **shape**: Returns a tuple representing the dimensionality of the DataFrame (number of rows, number of columns).

```sh
```

### Accessing and Modifying Data:
- **loc[]**: Accesses a group of rows and columns by labels.
- **iloc[]**: Accesses a group of rows and columns by integer position.
- **[] indexing**: Allows you to select columns or rows using column names or boolean indexing.
- **at[] and iat[]**: Fast scalar value accessors similar to loc[] and iloc[].
```sh
```

### Data Manipulation:
- **drop()**: Drops specified labels from rows or columns.
- **rename()**: Renames columns or index labels.
- **merge()**, concat(), join(): Combine DataFrames through various methods (e.g., merging on common columns, concatenating along axes, etc.).
- **apply(), applymap(), map()**: Apply functions element-wise or row/column-wise.

### Data Cleaning and Preparation:
- **fillna()**: Fills missing values with specified methods or values.
- **dropna()**: Drops rows or columns with missing values.
- **astype()**: Converts the data type of a column.
- **duplicated(), drop_duplicates()**: Identifies and removes duplicated rows.

### Aggregation and Grouping:
- **groupby()**: Groups data based on one or more keys and allows applying aggregate functions.
- **agg(), apply()**: Perform aggregation operations on grouped data.

### Statistical Summary:
- **describe()**: Generates descriptive statistics for numerical columns.
- **value_counts()**: Counts unique values in a column.


### Visualization:
- plot(): Creates basic plots such as line plots, scatter plots, histograms, etc.
- hist(), boxplot(), scatter(), etc.: Specific visualization functions for different types of plots


## Common Useful Methods in Pandas

### sort_values():
- The sort_values method in pandas is used to sort a DataFrame by the values of one or more columns.

```sh
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'time': ['2023-01-03', '2023-01-01', '2023-01-02'],
    'value': [10, 20, 30]
})

# Convert the 'time' column to datetime objects
df['time'] = pd.to_datetime(df['time'])

# Sort the DataFrame by the 'time' column in ascending order
df.sort_values('time', inplace=True)

print(df)

        time  value
1 2023-01-01     20
2 2023-01-02     30
0 2023-01-03     10

```
- When you call df.sort_values('time', inplace=True), you are instructing pandas to sort the DataFrame df based on the values in the 'time' column.

- **inplace**: The inplace parameter is a boolean that determines whether to return a new DataFrame or to modify the original DataFrame
-  If **inplace=True**, the method will sort the DataFrame in place, meaning the original DataFrame df is modified and nothing is returned. 
- If **inplace=False** (which is the default), the method will return a new sorted DataFrame, and the original DataFrame will remain unchanged.
- **ascending**: This optional parameter specifies the sorting order. If ascending=True (which is the default), the data is sorted in ascending order (from smallest to largest). If ascending=False, the data is sorted in descending order (from largest to smallest)
- **na_position:** This optional parameter determines the position of NaN values (missing data) in the sorted DataFrame. The default is na_position='last', which means that NaN values will be placed at the end of the DataFrame. If na_position='first', NaN values will be placed at the beginning.


### date_range() Method
- Versatile function that can be used to create a range of datetime values with a specified frequency, starting and ending at particular datetime points.

```sh
import pandas as pd
from datetime import datetime, timedelta

# Define the start and end times
current_time = datetime.now()
one_hour_ago = current_time - timedelta(hours=1)

# Define the frequency
frequency = '5T'  # Every 5 minutes

# Generate the datetime index
new_index = pd.date_range(start=one_hour_ago, end=current_time, freq=frequency)

print(new_index)

```