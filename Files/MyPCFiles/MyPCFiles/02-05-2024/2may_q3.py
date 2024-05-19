import numpy as np
import pandas as pd
#Create Series using list here default integer index is created
s = pd.Series([1, 3, 5, np.nan, 6, 8]) # data type = float becoz of np.nan
print(s)
a = pd.Series([1, 3, 5,  6, 8]) # data type = int 
print(a)
#all elements in a series can have ONLY single data type 
s1 = pd.Series((1, 'IACSD', 5, np.nan, 6, 8))
print(s1)
#Creating a DataFrame by passing a NumPy array, with a datetime index using date_range() and labeled columns:
dates = pd.date_range("20230315",periods=6)
print(dates)

from numpy.random import default_rng
rng = default_rng()
df = pd.DataFrame(rng.standard_normal((6, 4)), index=dates, columns=list("ABCD"))
print(df)  # 6 sigma rule, +3sig to -3sig range of normal distribution

# create a dataframe using list of list
b = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
c = pd.DataFrame(b)
print(c)
print(" ")
# data broadcasting in list of lists...

d = pd.DataFrame(b,columns=['c1','c2','c3'])
print(d)
print(" ")
e = pd.DataFrame(b,columns=list('ABC'))
print(e)
print(" ")
f = pd.DataFrame(b,index=[101,102,103,104],columns=list('ABC'))
print(f)
print(" ")
g = pd.DataFrame(b,index=range(12,16),columns=list('ABC'))
print(g)
print(" ")

#Creating a DataFrame by passing a dictionary of objects that can be converted into a series-like structure:
# in this dictionary one key will represent one column and value of that key will contain all elements of 
# that column

h = {'c1':[1,2,3],
     'c2':[77,88,99]}
k = pd.DataFrame(h)
print(k)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20220102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df2)

#The columns of the resulting DataFrame have different dtypes:
print(df2.dtypes)

# head
# get first 5 rows from dataframe
# if n is passed then first n rows
print(df2.head())

#tail
# get last 5 rows
# if n is passed then last n rows
print(df2.tail(3))

#index
print(df2.index)

#columns
print(df2.columns)

# object are string with fixed category

b = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
c = pd.DataFrame(b)
print(c)
print(" ")
n_arr = c.to_numpy()
print(type(n_arr))
print(n_arr)

print(c.describe())

# count = count of valid values expluding NaN values...
# standard deviation formula
# 25% - 25 % of the data is below this 
