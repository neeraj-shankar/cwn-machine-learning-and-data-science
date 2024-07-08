import pandas as pd

"""
Some of the mostly used methods in pandas library

1. apply(): to apply a function along an axis of the DataFrame or on a Series (a single column or row).
"""


class CommonPandasMethods:

    def __init__(self):
        pass

    def sum_two_numbers(self, first_number, second_number):

        total = first_number + second_number
        return total
    

    def use_apply_method_series(self):

        # Create a series and use apply addition method to each element in series
        number_series = pd.Series([1, 2, 3])
        # Add adding 5 to each of item in the series by passing arguments
        new_number_series = number_series.apply(self.sum_two_numbers, args=(5,))
        print(new_number_series)

        # Use apply with a lambda function to square each element
        squared_df = number_series.apply(lambda x: x**2)
        print(f"The result of lambda and apply:\n{squared_df}")
    
    def parse_datetime(self, column_data):

        for fmt in ['%d/%m/%y %H:%M', '%y/%m/%d %H:%M', '%Y-%m-%d %H:%M', '%d-%m-%Y %H:%M']:
            try:
                return pd.to_datetime(column_data, format=fmt)
            except ValueError:
                continue
        raise ValueError(f"No valid DateTime Matched....")
    
    def parse_datetime_vectorised(self, df, time_column, parsed_column):

        # Read the CSV file into a DataFrame
        # df = pd.read_csv('your_file.csv')

        # List of date formats to try
        date_formats = ['%d/%m/%y %H:%M', '%y/%m/%d %H:%M', '%Y-%m-%d %H:%M', '%d-%m-%Y %H:%M']

        # Try to convert the dates using the formats listed above
        for fmt in date_formats:
            # Convert dates where possible
            df[parsed_column] = pd.to_datetime(df[time_column], format=fmt, errors='coerce')
            # Keep only the successfully parsed dates and ignore the ones that returned NaT
            df[time_column] = df[time_column].where(df[parsed_column].isna(), None)

        # Drop the rows where the date could not be parsed (if any)
        df.dropna(subset=[parsed_column], inplace=True)

        # Inspect the result
        return df[parsed_column]
        print(df[[time_column, parsed_column]].head())
    
    def clean_data_and_save(self, dataframe, new_file_path):

        # Remove rows where all cells are NaN
        # dataframe = dataframe.dropna(how='all')

        # Remove rows where any cell is NaN
        dataframe = dataframe.dropna(how='any')

        # Inspect the result
        print(dataframe.tail(10))

        # Save the cleaned DataFrame to a new CSV file
        dataframe.to_csv(new_file_path, index=False)






if __name__ == "__main__":

    CommonPandasMethods().use_apply_method_series()
