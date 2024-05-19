#30. Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.
#Original Matrix:
#l=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
#Sort the said matrix in ascending order according to the sum of its rows
#[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
#Original Matrix:
l=[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
#Sort the said matrix in ascending order according to the sum of its rows
#[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
def function(x:list):
    s=0
    for e in x:
       s=s+e
    return s   
print(sorted(l,key=lambda x:function(x),reverse=False))