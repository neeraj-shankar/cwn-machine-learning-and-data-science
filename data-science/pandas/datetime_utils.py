import pandas as pd
from datetime import datetime, timedelta
import calendar

class DateTimeUtils:
    """
    Contains common utility method based date and time module.
    
    """

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def _create_new_timestamp_for_historic_data(df):


        # Ensuring the time column is sorted
        df.sort_values('time', inplace=True)
        

        print(f"Time Column after duplicate handling.")
        print(df['time'])
        # Step 2: Generate a new time series index
        current_time = datetime.now(tz=df['time'].dt.tz)
        interval = current_time - timedelta(hours=1)

        # Assuming the original data has a frequency, e.g., '5T' for 5 minutes
        frequency = '1ms'  # Adjust this to match the frequency of your original data
        new_index = pd.date_range(start=interval, end=current_time, freq=frequency)

        # Option 1: Drop rows from the DataFrame if it has more rows than new_index
        if len(df) > len(new_index):
            df = df.iloc[:len(new_index)].copy()

        # Option 2: Drop values from new_index if it has more values than the number of rows in df
        if len(new_index) > len(df):
            new_index = new_index[:len(df)]

        # Now that both df and new_index have the same number of rows, you can add the new_index as a column
        df['time'] = new_index

        # Step 4: Write the updated DataFrame back to the CSV file
        data_path = r'data-science/processed_data/historic_data_selected_for_all_indexes_.csv'
        df.to_csv(data_path, index=False)

    @staticmethod
    def _update_month(dataframe, time_column, destination_file_path):

        # Step 2: Update the month in the time column to the current month minus one
        # Get the current month
        current_month = datetime.now().month
        current_year = datetime.now().year
        print(f"Current Month: {current_month}")

        # Calculate the previous month
        previous_month = current_month - 1 if current_month > 1 else 12
        previous_year = current_year if  current_month > 1 else current_year - 1
        print(f"Previous Month: {previous_month}")

        # Last day of the month
        last_day_of_month = calendar.monthrange(previous_year, previous_month)[1]
        print(f"Last Day of the month: {last_day_of_month}")

        # Use the minimum of the original day and the last day of the target month
       # new_day = min(time_column.day, last_day_of_month)

        dataframe[time_column] = dataframe[time_column].apply(lambda dt: dt.replace(month=previous_month, year=dt.year if current_month > 1 else dt.year - 1, day=min(dt.day, last_day_of_month)))
        print(f"Updated Time: {dataframe[time_column]}")

        # Step 3: Write the updated DataFrame back to the CSV file
        dataframe.to_csv(destination_file_path, index=False)

    