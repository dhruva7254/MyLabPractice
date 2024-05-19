#19. Write a Python program to find all anagrams of a string in a given list of strings using Lambda.
#Orginal list of strings:
l=['bcda', 'abce', 'cbda',"bcdda", 'cbea', 'adcb']
#Anagrams of 'abcd' in the above string:
#['bcda', 'cbda', 'adcb']
l1=[l[0]]
for idx in range(1,len(l)):
   if (len(l[0])==len(l[idx]))&((set(l[0])-set(l[idx]))==set()):
         l1.append(l[idx])
print(l1)
print(list(filter(lambda x:(len(l[0])==len(x))&((set(l[0])-set(x))==set()),l)))
