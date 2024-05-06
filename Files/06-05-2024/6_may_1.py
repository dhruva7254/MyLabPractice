import pandas as pd
import numpy as np
df = pd.read_csv("D:\Dhruva\MarketArrivals.csv")
print(df.shape)
print(df.columns)
print(df['market'].nunique(),df['market'].unique())
print(df['market'].mode())
print(df.groupby('state')['market'].count())





