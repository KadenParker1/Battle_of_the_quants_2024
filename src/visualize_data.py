import pandas as pd

# update this path to be your local path
path='/Users/kadenparker/Desktop/Misc/quant/BOQ_data.parquet'
df=pd.read_parquet(path)
print(df.head())