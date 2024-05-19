import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("D:\Dhruva\EmployeeAttrition.csv")
df.info()
#df['Age'].hist() #bins=50
for col in df.columns:
    df[col].hist()