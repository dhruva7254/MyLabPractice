import pandas as pd
d= {'SQL':[1,2,3,4,30],'Python':[11,22,77,88,99],'AA':[12,23,34,45,56]}
df = pd.DataFrame(d,index=[101,109,102,125,110])
print(df)
print(' ')
# print(df.sort_index(axis=1))
# print(' ')
# print(df.sort_index(axis=0))
# print(' ')
# print(df.sort_values(by='Python', ascending=False))
# print(' ')
# print(df.sort_index(axis=1,inplace=True)) # modify original df (inplace=True), if false then return copy...
# print(df)
# print(' ')
# df = pd.DataFrame(rng.standard_normal((6, 4)),
#                   index=dates,
#                   columns=list("ABCD"))
# print(df)
"""print(df.iloc[2:5,])
print(df.loc[102:110,])

print(df.loc[[101,110],'Python'])
print(df.iloc[[0,4],1])

print(df.sort_values(by='AA',ascending=False,inplace=True).iloc[2,2])"""

# Q. write loc syntax to select all students who have recieved more than 23 marks in python
# Q. select all students where sql marks are greater than 29 and advance analytics marks are greater than 20 

print(df.loc[df['Python']>23])
print(df.loc[(df['SQL']>29)&(df['AA']>20)])

a=df.loc[df['Python']>23]
print(a)