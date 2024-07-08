
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

### DataFrames 

- DataFrame is a two-dimensional labeled data structure provided by the Pandas library. 
- It is similar to a spreadsheet or SQL table, where data is organized into rows and columns. 
- Each column can have a different data type (e.g., integer, float, string)

#### Creating DataFrames
- DataFrames can be created from various data sources such as dictionaries, lists, NumPy arrays, or from external files like CSV, Excel, SQL databases, etc.
- Some commonly used functions for creating DataFrames include pd.DataFrame() and pd.read_csv().
```sh
```

#### Viewing Data:
- **head(n)**: Returns the first n rows of the DataFrame.
- **tail(n)**: Returns the last n rows of the DataFrame.
- **shape**: Returns a tuple representing the dimensionality of the DataFrame (number of rows, number of columns).

```sh
```

#### Accessing and Modifying Data:
- **loc[]**: Accesses a group of rows and columns by labels.
- **iloc[]**: Accesses a group of rows and columns by integer position.
- **[] indexing**: Allows you to select columns or rows using column names or boolean indexing.
- **at[] and iat[]**: Fast scalar value accessors similar to loc[] and iloc[].
```sh
```

#### Data Manipulation:
- **drop()**: Drops specified labels from rows or columns.
- **rename()**: Renames columns or index labels.
- **merge()**, concat(), join(): Combine DataFrames through various methods (e.g., merging on common columns, concatenating along axes, etc.).
- **apply(), applymap(), map()**: Apply functions element-wise or row/column-wise.

#### Data Cleaning and Preparation:
- **fillna()**: Fills missing values with specified methods or values.
- **dropna()**: Drops rows or columns with missing values.
- **astype()**: Converts the data type of a column.
- **duplicated(), drop_duplicates()**: Identifies and removes duplicated rows.

#### Aggregation and Grouping:
- **groupby()**: Groups data based on one or more keys and allows applying aggregate functions.
- **agg(), apply()**: Perform aggregation operations on grouped data.

#### Statistical Summary:
- **describe()**: Generates descriptive statistics for numerical columns.
- **value_counts()**: Counts unique values in a column.


#### Visualization:
- plot(): Creates basic plots such as line plots, scatter plots, histograms, etc.
- hist(), boxplot(), scatter(), etc.: Specific visualization functions for different types of plots


