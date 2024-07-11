import pandas as pd


class FileMerger:

    def __init__(self, source_paths):
        self.source_paths = source_paths

    def merge_multiple_csv(self):

        # Read each CSV file into a DataFrame and store them in a list
        dataframes = [pd.read_csv(file) for file in self.source_paths]

        # Concatenate all DataFrames into one DataFrame
        merged_df = pd.concat(dataframes, ignore_index=True)

        # Save the merged DataFrame to a new CSV file
        merged_df.to_csv('thousands_eye_kpi_data.csv', index=False)


