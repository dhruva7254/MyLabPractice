"""def minion_game(s):
    vowels = 'AEIOU'
    ravi_score = 0
    lata_score = 0
    length = len(s)

    for i in range(length):
        if s[i] in vowels:
            lata_score += length - i
        else:
            ravi_score += length - i

    if ravi_score > lata_score:
        print("Ravi", ravi_score)
    elif lata_score > ravi_score:
        print("Lata", lata_score)
    else:
        print("Draw", ravi_score)

s = "BANANA"
minion_game(s)"""

"""def minion_game(s)
    score_latra = 0
    score_gt = 0
    """

"""r0=[1]
n=5
for row in range(n):
    r=[1]
    for i in range(1,len(r0)):
        r.append(r0[i-1]+r0[i]) #i-1 and i from previous row
    r.append(1)
    print(r)
    r0=r

r0=[1]
n=5
for row in range(n):"""

"""__add__(self,other)
__sub__(self,other)
__mul__(self,other)
"""
"""class parent:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        self.x=self.x+other"""

"""class Parent:
    def __init__(self):
        self.value="cars"
    def __add__(self,other:int):
        self.value=self.value+other
        print(self.value)
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value="bikes"
    def __add__(self, other: int):
        return super().__add__(other)"""

"""class Parent:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return self.x+other
class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x, y)
    def __add__(self, other):
        a = self.y+self.x
#        return super().__add__(other)
        return a
print(Child(2,3).__add__(2))"""

"""class parent:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return(self.x+self.y)
class child(parent):
    def __init__(self, x, y):
        super().__init__(x, y)
    def __add__(self, other):
        super().__add__(other)
        return(self.x+other)
print(child(2,3).__add__(4))"""

"""class point2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        if isinstance(other,point2D) == True:
            x=self.x + other.x
            y=self.y + other.y
        else:
            x=self.x + other
            y=self.y + other
        return point2D(x,y)

    def __radd__(self,other):
        #other will not be object of point
        x=self.x + other
        y=self.y + other
        return point2D(x,y)
"""

"""class Parent(): 
      
    # Constructor 
    def __init__(self): 
        self.value = "Inside Parent"
          
    # Parent's show method 
    def show(self): 
        print(self.value) 
          
# Defining child class 
class Child(Parent): 
      
    # Constructor 
    def __init__(self): 
        self.value = "Inside Child"
          
    # Child's show method 
    def show(self): 
        print(self.value) 
          
          
# Driver's code 
obj1 = Parent() 
obj2 = Child() 
  
obj1.show() 
obj2.show() """

"""class parent:
    def __add__(self,other):
        self.x
"""

"""def odd_num(a):
    if a%2 == 0:
        return False
    else:
        return True
print(odd_num(7))"""

"""sent = "IACSD has brilliant students"
sent = sent.lower() # case insensitive
unique_char = set(sent)
print(unique_char)
char_count={}
for char in unique_char:
    char_count[char]  = sent.count(char)
print(char_count)
"""

"""s1="IACSD has brilliant students"
s2=s1.islower()
s3=set(s2)
print(s3)
count={}
for c in s3:
    count[c] = s2.count(char)
print(count)"""

"""def count_unique_characters(sentence):
    # Creating an empty dictionary to store characters and their counts
    char_count = {}

    # Iterating through each character in the sentence
    for char in sentence:
        # Checking if the character is already in the dictionary
        if char in char_count:
            # If it's in the dictionary, increment its count
            char_count[char] += 1
        else:
            # If it's not in the dictionary, add it with a count of 1
            char_count[char] = 1

    # Printing the unique characters and their counts
    print("Unique characters and their occurrences:")
    for char, count in char_count.items():
        print(f"{char}: {count}")

# Example usage
sentence = input("Enter a sentence: ")
count_unique_characters(sentence)

def cou_uni_cha(a):
    cha_cou={}
    for c in a:
        if c in cha_cou:
            cha_cou[c]+=1
        else:
            cha_cou=1
    for c,count in cha_cou.items():
        print

s = "IACSD is a good place"
cou_uni_cha(s)

sent = "IACSD has brilliant students"
sent = sent.lower() # case insensitive
char_count={}
for char in sent:
    if char in char_count:
        char_count[char] = char_count[char]+1
    else:
        char_count[char]= 1
print(char_count)"""

"""s="IACSD is a super place"
s=s.lower()
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d) """

"""s="IACSD is a super place"
s=s.lower()
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

s="IACSD is a super place"
s=s.lower()
s=s.split()
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

def div11(a):
    if a%2 == 0:
        return False
    else:
        return True
print(div11(4),div11(11))"""

"""def che_div(n):
    def che_num(a):
        if a%n == 0:
            return False
        else:
            return True
    return che_num
b=che_div(5)
print(b(10))

def check_divisibility(n):
    def inner_function(num):
        if num % n == 0:
            return True
        else:
            return False
    return inner_function

my_fun=check_divisibility(5)
print(my_fun(10),my_fun(11))"""

"""def che_qwe(a):
    def che_asd(b):
        if b % a == 0:
            return True
        else:
            return False
    return che_asd
che_zxc=che_qwe(5)
print(che_zxc(10))"""

"""def helo(name,rollno):
    print("Hello ...",name,rollno)
helo('asd',234)"""

print((lambda x : x**2)(3))
print((lambda y: -y)(10))
print((lambda p,q: p*q)(2,4)) # multiply two values
print((lambda l: l[0])([24,56,78])) #return first element of the list
print((lambda s1,s2: s1+s2)("akurdi", "pune"))

print((lambda x:x**2)(3))

func1=(lambda x:x+1) 
































































