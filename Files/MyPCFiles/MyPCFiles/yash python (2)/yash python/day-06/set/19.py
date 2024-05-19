#19. Write a Python program to find elements in a given set that are not in another set.
s1={1,2,3,4,5,11,13,7,8}
s2={1,2,3,4,5,6,7,12,8,9}
print(s1-s2)
print(((s1|s2)-(s1&s2))-(s2-((s1&s2))))