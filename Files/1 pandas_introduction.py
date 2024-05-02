import numpy as np
import pandas as pd


#Create Series 
# using list
# here default integer index is created
s = pd.Series([1, 3, 5, np.nan, 6, 8])

s

#all elements in a series can have 
# ONLY single data type 
s1 = pd.Series((1, 'IACSD', 5, np.nan, 6, 8))

s1



#Creating a DataFrame by passing a NumPy array, 
#with a datetime index using date_range() 
#and labeled columns:

dates = pd.date_range("20230315", 
                      periods=6)

dates


from numpy.random import default_rng
rng = default_rng()
    
df = pd.DataFrame(rng.standard_normal((6, 4)), 
                  index=dates, 
                  columns=list("ABCD"))

df

#Creating a DataFrame by passing a dictionary of objects 
#that can be converted into a series-like structure:

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

df2

#The columns of the resulting DataFrame have different dtypes:
df2.dtypes


# head
# get first 5 rows from dataframe
# if n is passed then first n rows
df.head()

#tail
# get last 5 rows
# if n is passed then last n rows
df.tail(3)


#index
df.index

#columns
df.columns

# Data frame to numpy array
"""
DataFrame.to_numpy() gives a NumPy representation 
of the underlying data. 

DataFrame.to_numpy() does not include 
the index or column labels in the output.

Note that this can be an expensive operation 
when your DataFrame has columns with different data types, 
which comes down to a fundamental difference between 
pandas and NumPy
NumPy arrays have one dtype for the entire array, 
while pandas DataFrames have one dtype per column. 
When you call DataFrame.to_numpy(), pandas will find 
the NumPy dtype that can hold all of the dtypes 
in the DataFrame. This may end up being object, 
which requires casting every value to a Python object.
"""
"""
For DataFrame of all floating-point values, 
DataFrame.to_numpy() is fast  
Also it doesn’t require copying data:
"""
df.to_numpy()
"""
For DataFrame with multiple dtypes, 
DataFrame.to_numpy() is relatively expensive:
"""
df2.to_numpy()


# statistic summary of data
df.describe()

# Transpose of DataFrame
# Here index and column names are swapped
df.T

# Sort by an axis
# axis 0 is row direction
# axis 1 is column direction

df.sort_index(axis=1, ascending=False)


# Sort by values in given column 
#or list of columns
df.sort_values(by="B")

# Accessing 
# Access a column
df['A']

# Access list of columns
# Doesn't create a copy
df[['B', 'C']]

# Slice the rows using row number
# here end is excluded
# Doesn't create a copy
df[0:3]

# Slice the rows using row labels (index)
# Here end is included
# Doesn't create a copy
df["20230315":"20230318"]


# Create shallow copy of data frame
df2 = df.copy()

# loc
# selection by label
# uses rows labels and column labels
# This returns data frame / series
# End is included 

df.loc["20230315":"20230318", ["A", "B"]]

# Access Single cell (return scalar value)
df.loc[dates[0], "A"]

# Fast Access Single cell (return scalar value)
df.at[dates[0], "A"]


# iloc
# Selection by position
# uses rows number and column number
# This returns a data frame / series
# End is excluded 

df.iloc[3:5, 0:2]


# Selecting By lists of integer position locations, 
#similar to the NumPy/Python style:

df.iloc[[1, 2, 4], [0, 2]]


# Access Single cell (return scalar value)
df.iloc[1,1]

# Fast Access Single cell (return scalar value)
df.iat[1,1]


# Add new column
# Direct assignment
df["E"] = ["one", "one", "two", 
           "three", "four", "three",
           ]

df['E']=10 # Works

df['E']=[10] # error

df

# Add new column
#Using Series object with index
s1 = pd.Series([1, 2, 3, 4, 5, 6], 
               index=pd.date_range("20230316", periods=6))
s1

df["F"] = s1

df



# Boolean Indexing (Filtering)
# Select rows by Condition
df[df["A"] > 0]

# Select Cells by condition
# Cells which fulfill condition are returned as it is
# Cells which don't fulfill condition are given value NaN

df[df > 0]

# Filter using multiple values
df["E"] = ["one", "one", "two", 
           "three", "four", "three",
           ]
df[df["E"].isin(["two", "four"])]


# Update single cell
#using label -> date and column "A"
df.at[dates[0], "A"] = 0

df

#using index -> first row and third column
df.iat[0, 2] = 0

df

# Using Numpy array
df.loc[:, "D"] = np.array([5] * len(df))

df

# Update using condition
df2 = df.copy()
df2['E']=10
df2[df2 <= 0] = -df2

df2

# Mean median Mode of All columns

df.mean(axis=1)

df.median()

# Mode
# Mode may return multiple values
df1 = pd.DataFrame()
df1['cat1'] = ['A','B','B','B','C','D']
df1['cat2'] = [1,1,2,2,3,4]
df1['rno'] = [1,2,3,4,5,6]

df1.mode()


# Missing value handling

df1= df.copy()

df1['E'] = [5,np.nan,100,np.nan,200,500]

# Check which cells are Missing (NaN)
df1.isna()
df1.isnull()

# Drop all rows containing any missing (NaN) value
df1.dropna(how="any")

# Drop all columns containing any missing (NaN) value
df1.dropna(axis=1)


# Fill Missing values
# Fill constant value
df1.fillna(value=9999)

# Fill Median value of that column
# Used in Industry
df1.fillna(value=df1.median())


# Apply user defined function to data
df1 =df[['A','B','C']].copy()

df1.apply(lambda x: x.max() - x.min())

# String column handling
s = pd.Series([10.2,"A", "B", "C", "Aaba", "Baca", 
                np.nan, "CABA", "dog", 
               "cat"])

s.str.lower()

s.str.endswith("a")

#Cocat operation
# Create Data frame with 10 rows and 4 columns
# with random values
df = pd.DataFrame(np.random.randn(10, 4))

df


df_list = [df[:3], df[3:7], df[7:]]

pd.concat(df_list)

# Join using merge function
left = pd.DataFrame({"key": ["foo", "bar"], 
                     "lval": [1, 2]})

right = pd.DataFrame({"key": ["foo", "bar"], 
                      "rval": [4, 5]})

left

right

pd.merge(left, right, on="key")


# GroupBy

df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar",
              "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", 
              "three", "two", "two", 
              "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)


df

# Group By Single Column
df.groupby("A")[["C", "D"]].sum()

df.groupby("A")[["C"]].sum()

# Group By Multiple Columns
df.groupby(["A", "B"]).sum()
df.groupby(["A", "B"])['D'].sum()



# Categorical Data Handling

df = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], 
     "raw_grade": 
         ["a", "b", "b", "a", "a", "e"]}
)

df["grade"] = df["raw_grade"].astype("category")

df["grade"]

# Rename the categories
# rename  a as very good
# b as good
# c as very bad
new_categories = ["very good", "good", "very bad"]

df["grade"] = df["grade"].cat.rename_categories(new_categories)

# Change order of the categories
df["grade"] = df["grade"].cat.set_categories(
    ["very bad", "bad", "medium", "good", "very good"]
)

df["grade"]

# Sort by categorical column
df.sort_values(by="grade")


# Groupby on Categorical column
# Get group size
df.groupby("grade").size()
# get row count for every column
df.groupby("grade").count()


# Importing and Exporting Data

#CSV 
df.to_csv("file1.csv")

pd.read_csv("file1.csv")


#HDF5
# Store df as HDF file
# two parameters filename and key
df.to_hdf("foo.h5", "df") 

# Read HDF file in data frame
# two parameters filename and key
# Key is optional if only one object in file
pd.read_hdf("foo.h5", "df")


#Excel

# Store df as excel file
# two parameters filename and sheet name
df.to_excel("foo.xlsx", sheet_name="Sheet1")

#Read Excel in df
# two parameters filename and sheet name
# sheet name is optional if only one sheet in file
pd.read_excel("foo.xlsx", "Sheet1", index_col=None, 
              na_values=["NA"])


# If condition with pandas 
#series / dataframe

# Comparison operators return 
#True or False
# for every cell in Series or Dataframe

df1 = pd.DataFrame()
df1['num1'] = [100,3,500,57,89,90]
df1['num2'] = [10,1,200,245,30,4]

print(df1 < 50)


S1= pd.Series([200,202,405,607,566,234])
print(S1 < 300)

# So, comparison inside if statement 
#will give error
# Here PVM cannot determine the output

# Following statement gives ValueError
S1= pd.Series([200,202,405,607,566,234])
if(S1 < 300):
    print("Less")
else:
    print("more")

# Right Way to check this
# Use any() or all() function
S1= pd.Series([200,202,405,607,566,234])
if ((S1 < 300).any() == True) :
    print("Any one value from series is Less then 300")
else:
    print("No value from series is Less then 300") 

# Check empty with empty attribute
e = pd.Series([])
if(e.empty == True):
    print("It is Empty")
else:
    print("It has elements")


# using 'in' operator vs 'isin' function

# in operator works on index in series
# because series is dictionary with index as key
# in operator works on column names in dataframe
# because dataframe is dictionary with 
# column name as key

# So, use isin function for right results

S1= pd.Series([200,202,405,607,566,234])
print(202 in S1)

S1.isin([202])    

df1 = pd.DataFrame()
df1['num1'] = [100,3,500,57,89,90]
df1['num2'] = [10,1,100,245,30,4]

print(100 in df1)

df1.isin([100])


# Difference in pandas and Numpy
"""For Series and DataFrame objects, pandas var() 
normalizes by N-1 to produce unbiased estimates 
of the population variance, 
while NumPy’s numpy.var() normalizes by N, 
which measures the variance of the sample. 
Note that cov() normalizes by N-1 in 
both pandas and NumPy."""



# basic Statistics 

S1= pd.Series([200,202,405,607,566,234])
S1.skew()
S1.kurtosis()

S1.quantile([0.05,0.25,0.5,0.75,0.95])



# How to Sample the data

df = pd.read_csv("lung_data.csv")
df.shape
df.shape[0] # rows
df.shape[1] # columns

df_r = df.sample(100, random_state=7)

df_r.shape

df_r.mean()

