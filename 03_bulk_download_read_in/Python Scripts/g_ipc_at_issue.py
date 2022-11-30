#Read-in script for International Patent Classification data for all patents (as of publication date)

# Importing necessary packages.
import os
import zipfile as zip
import pandas as pd
import csv
pd.set_option('display.max_columns', None)
# Set up file path:
# Please include the folder path of the file you are reading. Ex: os.chdir("C:/Users/johnsmith/Downloads")
os.chdir("")
# Selecting the zip file.
file_name = "g_ipc_at_issue.tsv.zip"
f_name = "g_ipc_at_issue.tsv"
with zip.ZipFile(file_name) as zf:
    chunksize = 15*(10 ** 5)
    count = 1
    n_obs = 0
    for df in pd.read_csv(zf.open(f_name), delimiter="\t", chunksize=chunksize, quoting=csv.QUOTE_NONNUMERIC):
        print('processing chunk: ' + str(count))
        n_obs += len(df)
        count += 1
# Print summary of data: number of observations, columns, and each variable data type
print(n_obs)
print(df.dtypes)