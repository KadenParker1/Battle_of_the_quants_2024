import pandas as pd
import numpy as np
pd.options.display.max_rows=999
pd.options.display.max_columns=999

# update this path to be your local path
path='/Users/andrewcriddle/Desktop/Battle_of_the_quants_2024/data/Battle of the Quants Students/BOQ_data.parquet'

df=pd.read_parquet(path)

df = df[df['PERMNO'].isin(df[df["DATE"] == np.datetime64('2023-12-31')]['PERMNO'])]
df = df[df['PERMNO'].isin(df[df["DATE"] == np.datetime64('2005-01-31')]['PERMNO'])]
# print(df[df["PRC"].isna()]['PERMNO'].unique())
df = df[df['PERMNO'].isin(df[df["PRC"].isna()]['PERMNO'])]
# [["PERMNO","DATE","RET",'ME','PRC']]
print(df[["PERMNO","DATE","RET",'ME','PRC']])
print(len(df["PERMNO"].unique()))
# df = df[df["PRC"].notna()]
# df = df[df["DATE"] >= np.datetime64('2005-01-31')]
# df = df.reset_index()


# print(df)
# print(len(df['PERMNO'].unique()))
# print(df[["PERMNO","DATE","RET",'ME','PRC']].head(999))