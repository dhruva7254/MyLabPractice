#8. Write a Python program to extract year, month, date and time using Lambda.
#Sample Output:
s="2020-01-15 09:03:32.744178"
#2020
##1
#15
#09:03:32.744178
"""def function():
    import datetime
    now=datetime.datetime.now()
    year=lambda x:x.year
    month = lambda x:x.month
    date= lambda x:x.date()
    time=lambda x:x.time()
    print(year(now))
    print(month(now))
    print(date(now))
    print(time(now))
function()
"""
def function():
    import datetime
    now=str(datetime.datetime.now())
    y=lambda x:x[0:4]
    m=lambda x:x[5:7]
    print(int(y(now)))
    print(int(m(now)))
function()
    