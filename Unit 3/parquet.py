# load packages
import pyarrow.parquet as pq
import pyarrow as pa
import pandas as pd
import numpy as np

# create a pandas DataFrame
df = pd.DataFrame(np.random.randn(100).
                  reshape(25, 4), columns=["one", "two",
                                           "three", "four"])

# convert the pandas DataFrame to a parquet table
tableToWrite = pa.Table.from_pandas(df)

# write the parquet table to file
pq.write_table(tableToWrite, "myPQFile.parquet")
