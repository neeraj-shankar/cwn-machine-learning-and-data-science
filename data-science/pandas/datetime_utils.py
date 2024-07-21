import pandas as pd
from datetime import datetime, timedelta
import calendar
import numpy as np
import pytz

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
        """
        Updates the month in the specified time column of the DataFrame to the previous month.
        If the current month is January, the previous month is set to December of the previous year.
        Days that exceed the last day of the previous month are adjusted to the last valid day.
        
        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the time data to be updated.
        time_column (str): The name of the column in the DataFrame that contains datetime objects.
        destination_file_path (str): The file path where the updated CSV will be saved.
        
        Returns:
        None: The method writes the updated DataFrame to a CSV file and does not return anything.
        """    

        # Get the current month
        current_month = datetime.now().month
        current_year = datetime.now().year
        print(f"Current Month: {current_month}")

        # Calculate the previous month
        previous_month = current_month - 1 if current_month > 1 else 12
        previous_year = current_year if  current_month > 1 else current_year - 1
        print(f"Previous Month: {previous_month}")

        # Find the last day of the previous month
        last_day_of_month = calendar.monthrange(previous_year, previous_month)[1]
        print(f"Last Day of the month: {last_day_of_month}")

        # Update the time column to the previous month, adjusting the year and day as necessary
        dataframe[time_column] = dataframe[time_column].apply(lambda dt: dt.replace(month=previous_month, year=dt.year if current_month > 1 else dt.year - 1, day=min(dt.day, last_day_of_month)))
        print(f"Updated Time: {dataframe[time_column]}")

        # Write the updated DataFrame back to the CSV file
        dataframe.to_csv(destination_file_path, index=False)
    
    def generate_synthetic_timeseries_data():


        # Define your KPIs and indexes
        kpis = ['KPI1', 'KPI2', 'KPI3']
        indexes = ['Index1', 'Index2', 'Index3']

        # User-defined parameters for time series generation
        past_time_hours = 24  # How many hours in the past to start the time series
        interval_minutes = 5  # Time interval in minutes
        value_range = (0, 100)  # Range for generating random values

        # Generate a time series index from the current time to the user-defined past time with the given interval
        current_time = datetime.now()
        start_time = current_time - timedelta(days=0, hours=0, minutes=10)
        print(start_time)
        time_index = pd.date_range(start=start_time, end=current_time, freq=f'{interval_minutes}T')

        # Choose a timezone (e.g., 'US/Eastern', 'Europe/Berlin', 'UTC')
        timezone = pytz.timezone('UTC')
        current_time = datetime.now(tz=timezone).replace(microsecond=0)
        print(f"Current Time: {timezone}")
        interval = current_time - timedelta(days=0, hours=1, minutes=0)

        # Assuming the original data has a frequency, e.g., '5T' for 5 minutes
        frequency = '1T'  # Adjust this to match the frequency of your original data
        time_index = pd.date_range(start=interval, end=current_time, freq=frequency)

        # Generate random values for each KPI and index combination
        data = []
        for kpi in kpis:
            for index in indexes:
                # Generate random values for the current KPI and index
                random_values = np.random.uniform(value_range[0], value_range[1], len(time_index))
                random_values = np.round(random_values, 2)
                for timestamp, value in zip(time_index, random_values):
                    print(value, timestamp)
                    data.append({'node_name': 'device', 'kpi_name': kpi, 'index': index, 'time': str(timestamp), 'value': value})

        # Create a DataFrame with the generated data
        df = pd.DataFrame(data)
        print(df.head(10))

        # Write the DataFrame to a CSV file
        df.to_csv('generated_data.csv', index=False)
    
    


    