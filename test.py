# load in dataset as pandas
import pandas as pd
import numpy as np

# create a dataframe 
data_jan = pd.read_parquet("data/yellow_tripdata_2012-02.parquet", engine='pyarrow')
data_feb = pd.read_parquet("data/yellow_tripdata_2012-01.parquet", engine='pyarrow')

# combine the two dataframes
data = pd.concat([data_jan, data_feb])

# save the dataframe to paquet file
data.to_parquet("data/yellow_tripdata_2012-01.parquet", engine='pyarrow')