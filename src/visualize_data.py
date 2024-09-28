import pandas as pd
pd.options.display.max_rows=999
pd.options.display.max_columns=999

# update this path to be your local path
path='/Users/kadenparker/Desktop/Misc/quant/BOQ_data.parquet'

df=pd.read_parquet(path)

# print(df.loc[3530000])
print(len(df["PERMNO"].unique()))