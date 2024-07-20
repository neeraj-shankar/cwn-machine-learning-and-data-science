from datetime_utils import DateTimeUtils
import pandas as pd

SOURCE_FILE = r'D:\Studyzone\cwn-machine-learning-and-data-science\data-science\data\data-1721210090630.csv'
DESTINATION_FILE = "output_file.csv"

# df = pd.read_csv(SOURCE_FILE, parse_dates=['time'])
# print(df.head(20))

# DateTimeUtils._update_month(df, 'time', DESTINATION_FILE)
DateTimeUtils.generate_synthetic_timeseries_data()