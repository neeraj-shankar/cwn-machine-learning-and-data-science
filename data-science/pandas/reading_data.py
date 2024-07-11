import pandas as pd


class ReadingDataFrame:

    def __init__(self, source) -> None:
        
        self.source = source

    def basic_read_operation(self):

        df = pd.read_csv(self.source)

        # Printing the first 5 rows from datafrmae set
        first_five_dataset = df.head(5)
        print(f"First Five Records from Entire Data Frame.\n{first_five_dataset}")

