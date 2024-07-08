import pandas as pd

SOURCE_FILE = "D:\Studyzone\Data-science-ml\data\dnac_cpu_health_500_records.csv"

class ReadingDataFrame:

    def __init__(self, source) -> None:
        
        self.source = source

    def basic_read_operation(self):

        df = pd.read_csv(self.source)

        # Printing the first 5 rows from datafrmae set
        first_five_dataset = df.head(5)
        print(f"First Five Records from Entire Data Frame.\n{first_five_dataset}")


if __name__ == "__main__":

    # Create the instance of the class

    readingDF = ReadingDataFrame(SOURCE_FILE)

    readingDF.basic_read_operation()