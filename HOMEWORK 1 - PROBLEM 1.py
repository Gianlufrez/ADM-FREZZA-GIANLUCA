#!/usr/bin/env python
# coding: utf-8

# # INTRODUCTION

# #### Say "Hello, World!" With Python

# In[ ]:


world = 'Hello, World!'
print(world)


# #### Python If-Else

# In[ ]:


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2 == 1:
        print('Weird')
    elif n%2==0 and 2 <= n <= 5:
        print('Not Weird')
    elif n%2 == 0 and 6 <= n <=20:
        print('Weird')
    elif n%2 == 0 and n> 20:
        print('Not Weird')


# #### Arithmetic Operators

# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a + b)
print(a - b)
print(a*b)


# #### Python: Division

# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a//b)
print(a/b)


# #### Loops

# In[ ]:


if __name__ == '__main__':
    n = int(input())
i = 0
while i < n:
    print(i**2)
    i +=1


# #### Write a function

# In[ ]:


def is_leap(year):
    leap = False
    if year%4 == 0:
        leap = True
        if year%100 == 0:
            leap = False
            if year%400 == 0 :
                leap = True 
    return leap
        
year = int(input())
print(is_leap(year))


# #### Print Function

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    
stringa = ''
for i in range(1,n+1):
    stringa = stringa + str(i)
print(stringa)


# # BASIC DATA TYPES

# #### List Comprehensions

# In[ ]:


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

l = []    
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            l.append([i,j,k])
c = []
for i in l:
    if sum(i) != n:
        c.append(i)
print(c)


# #### Find the Runner-Up Score!

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
x = set(arr)
a = sorted(x)
a.reverse()
print(a[1])


# #### Nested Lists

# In[ ]:


if __name__ == '__main__':
    lista = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append([name,score])
lista1 = []
for i in range(len(name)):
    lista.sort(key = lambda x: (x[1], x[0]))
for i in lista:
    lista1.append(i[1])
lista1 = set(lista1)
lista1 = list(lista1)
penultimo = lista1[1]
lista2 = []
for i in lista:
    if i[1] == penultimo:
        lista2.append(i[0])
for i in lista2:
    print (i)


# #### Finding the percentage

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
for k,v in student_marks.items():
    if k == query_name:
        name1 = k
l = student_marks[name1]
lung = len(l)
somma = 0
for i in range(len(l)):
    somma = somma + l[i] 
output = "{0:.2f}".format(somma/lung)
print(output)


# #### Lists

# In[ ]:


if __name__ == '__main__':
    N = int(input())
l = []
for i in range(N):
    inp = input().split()
    if inp[0] == 'insert':
        l.insert(int(inp[1]),int(inp[2]))
    if inp[0] == 'remove':
        l.remove(int(inp[1]))
    if inp[0] == 'append':
        l.append(int(inp[1]))
    if inp[0] == 'sort':
        l.sort()
    if inp[0] == 'pop':
        l.pop()
    if inp[0] == 'reverse':
        l.reverse()
    if inp[0] == 'print':
        print(l)


# #### Tuples

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tupla = tuple(integer_list)
    print(hash(tupla))


# # STRINGS

# #### sWAP cASE

# In[ ]:


def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# #### String Split and Join

# In[ ]:


def split_and_join(line):
    line = line.replace(" ", "-")
    return line
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# #### What's Your Name?

# In[ ]:


def print_full_name(first, last):
    print('Hello', first, last+'!', 'You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# #### Mutations

# In[ ]:


def mutate_string(string, position, character):
    stringnew = string [:position] + character + string [position + 1:]
    return stringnew

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# #### Find a string

# In[ ]:


def count_substring(string, sub_string):
    i = 0
    c=0
    while i < len(string)+1:
        if string[i:i+ len(sub_string)] == sub_string:
            c+=1
        i +=1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# #### String Validators

# In[ ]:


if __name__ == '__main__':
    s = input()

print(any(i.isalnum() for i in s))
print(any(i.isalpha() for i in s))
print(any(i.isdigit() for i in s))
print(any(i.islower() for i in s))
print(any(i.isupper() for i in s))


# #### Text Alignment

# In[ ]:


thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# #### Text Wrap

# In[ ]:


import textwrap

def wrap(string, max_width):
    return

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# #### Designer Door Mat

# In[ ]:


N, M = map(int, input().split())
i = 1
while i< len(range(N))+1:
    if i< N/2:
        print('-'*(int(M - 3*(i*2 - 1))//2) + '.|.'*(i*2 - 1) + '-'*(int(M - 3*(i*2 - 1))//2))
    if i == ((N+1)//2):
        print('-'*int((M-7)//2) + 'WELCOME' + '-'*int((M-7)/2))
    if i > (N/2)+1:
        print('-'*(i- (N+1)//2)*3 + '.|.'*((int(M) - 2*(i-(N+1)//2)*3)//3) + '-'*(i-(N+1)//2)*3)
    i = i + 1    


# #### String Formatting

# In[ ]:


def print_formatted(number):
    i = 1
    while i <= number:
        octal = str(oct(i))[2:]
        hexadecimal = str(hex(i))[2:]
        binary = str(bin(i))[2:]
        print( i,  octal,  hexadecimal, binary)
        i +=1

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# #### Alphabet Rangoli

# In[ ]:


def print_rangoli(size):
    import string
    design = string.ascii_lowercase
    L = []
    for i in range(n):
        s = "-".join(design[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
    print('\n'.join(L[:0:-1]+L))
    
#for this exercise I searched the solution in internet and tried to understand it because i couldn't solve it alone
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# #### Capitalize!

# In[ ]:


def solve(s):
    if 0 < len(s) < 1000:
        s = s.split(" ")
        l = []
        for i in s:
            l.append(i.capitalize())
    return " ".join(l)        
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# #### Merge the Tools!

# In[ ]:


def merge_the_tools(string, k):
    l = []
    lung = len(string)
    for i in range(0,lung,k):
        l.append(string[i:i+k])
    for i in range(len(l)):
        s=[]
        for j in l[i]:
            if j not in s:
                s.append(j)
        s1 = "".join(s)
        print(s1)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# # SETS

# #### Introduction to Sets

# In[ ]:


def average(array):
    array = set(array)
    N = len(array)
    somma = 0
    for i in array:
        somma = somma +i
    avarage = somma/N 
    return avarage
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# #### No Idea!

# In[ ]:


n, m= map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happy = 0
for i in arr:
    if i in A:
        happy +=1
    if i in B:
        happy -=1
print(happy)


# #### Symmetric Difference

# In[ ]:


M = int(input())
MS = set(map(int, input().split(' ')))
N = int(input())
NS = set(map(int, input().split(' ')))
A = MS.union(NS) - MS.intersection(NS)
A = list(A)
A.sort()
for i in A:
    print(i)


# #### Set .add()

# In[ ]:


N = int(input())
M = set()
for i in range(N):
    M.add(input())
print(len(M))


# #### Set .discard(), .remove() & .pop()

# In[ ]:


n = int(input())
s = set(map(int, input().split()))
N = input()
Q=[]
for i in range(int(N)):
    Q.append(input().split())
    if Q[i][0] == 'pop':
        s.remove(list(s)[0])
    elif Q[i][0] == 'remove':
        s.remove(int(Q[i][1]))
    elif Q[i][0] == 'discard':
        s.discard(int(Q[i][1]))
somma = sum(s)
print(somma)


# #### Set .union() Operation

# In[ ]:


n = int(input())
A = set(map(int,input().split()))
b = int(input())
M = set(map(int,input().split()))
C = A.union(M)
print(len(C))


# #### Set .intersection() Operation

# In[ ]:


n=int(input())
N = set(map(int,input().split()))
b = int(input())
B = set(map(int,input().split()))
Q = N.intersection(B)
print(len(Q))


# #### Set .difference() Operation

# In[ ]:


n = int(input())
N = set(map(int,input().split()))
m = int(input())
M = set(map(int,input().split()))
Q = N.difference(M)
print(len(Q))


# #### Set .symmetric_difference() Operation

# In[ ]:


a = int(input())
A = set(map(int,input().split()))
b = int(input())
B = set(map(int,input().split()))
Q = A.symmetric_difference(B)
print(len(Q))


# #### Set Mutations

# In[ ]:


n = len(set(map(int,input().split())))
A = set(map(int,input().split()))
N = int(input())
for i in range(N):
    comandi = input().split()
    s = set(map(int,input().split()))
    if comandi[0] == 'intersection_update':
        A.intersection_update(s)
    if comandi[0] == 'update':
        A.update(s)
    if comandi[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(s)
    if comandi[0] == 'difference_update':
        A.difference_update(s)
print(sum(A))


# #### The Captain's Room

# In[ ]:


from collections import Counter #using Counter because at the beginning i couldn't do this exercise, then 
# i moved on and discovered Counter from collections exercises!
c = Counter()
k= int(input())
data = input().split()
data1 = Counter(data)
for i in data1:
    if data1[i] == 1:
        print(i)


# #### Check Subset

# In[ ]:


T=int(input())
for i in range(T):
    a = len(set(map(int, input().split())))
    A = set(map(int, input().split()))
    b = len(set(map(int, input().split())))
    B = set(map(int, input().split()))
    if B.union(A) == B:
        print('True')
    else: 
        print('False')


# #### Check Strict Superset

# In[ ]:


A = set(map(int, input().split()))
n = int(input())
l = []
for i in range(n):
    a = set(map(int,input().split()))
    l.append(A.intersection(a) == a)
if False in l:
    print('False')
else:
    print('True')


# # COLLECTIONS

# #### collections.Counter()

# In[ ]:


from collections import Counter
X = int(input())
A = map(int,input().split())
Q = Counter(A)
N =int(input())
somma = 0
for i in range(N):
    taglia, prezzo = map(int,input().split())
    if taglia in Q and Q[taglia] > 0:
        somma += prezzo
        Q[taglia] -=1
print(somma)


# #### DefaultDict Tutorial

# In[ ]:


from collections import defaultdict
n, m = input().split()
d = defaultdict(list)
B = []
for i in range (int(n)):
    s = input()
    d[s].append(i+1)
for i in range(int(m)):
    B.append(input())
for i in B:
    if i in d.keys():
        print(*d[i])
    else:
        print(-1)


# #### Collections.namedtuple()

# In[ ]:


from collections import namedtuple
N = int(input())
somma=0
l = []
for i in range(N+1):
    Q = list(map(str,input().split()))
    l.append(Q)
for i in range(len(l[0])):
        if l[0][i] == 'MARKS':
            for j in l[1:]:
                somma = somma + int(j[i]) 
media = somma/N
dec = round(media,2)
print(dec)


# #### Collections.OrderedDict()

# In[ ]:


from collections import OrderedDict
N = int(input())
d = OrderedDict()
for i in range(N):
    item, spazio, price = input().rpartition(' ')
    d[item] = d.get(item,0) + int(price)
for item, price in d.items():
    print(item,price)


# #### Word Order

# In[ ]:


from collections import Counter
n = int(input())
l = []
for i in range(n):
    m = list(map(str,input().split('\n')))
    for j in m:
        l.append(j)
s = set(l)
print(len(s))
conta = Counter(l)
print(*conta.values())


# #### Collections.deque()

# In[ ]:


from collections import deque
N = int(input())
arr = []
d = deque()
for i in range(N):
    arr.append(input().split())
for i in range(N):
    if arr[i][0] == 'append':
        d.append(arr[i][1])
    if arr[i][0] == 'appendleft':
        d.appendleft(arr[i][1])
    if arr[i][0] == 'pop':
        d.pop()
    if arr[i][0] == 'popleft':
        d.popleft()
d = list(d)
print(*d)


# #### Company Logo

# In[ ]:


import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input()
    l = []
    for i in s:
        l.append(i)
    a = Counter(l)
    q = []
    for i in a:
        q.append((i, a[i]))
    q = sorted(q, key = lambda x:x[0], reverse = False)
    q = sorted(q, key = lambda x:x[1], reverse = True)
    q = q[:3]
    for i in q:
        print(*i, sep = ' ')


# # DATE AND TIME

# #### Calendar Module

# In[ ]:


import calendar
data = input().split()
giorno = calendar.weekday(int(data[2]),int(data[0]),int(data[1]))
if giorno == 0:
    print('MONDAY')
elif giorno == 1:
    print('TUESDAY')
elif giorno == 2:
    print('WEDNESDAY')
elif giorno == 3:
    print('THURSDAY')
elif giorno == 4:
    print('FRIDAY')
elif giorno == 5:
    print('SATURDAY')
else:
    print('SUNDAY')


# #### Time Delta

# In[ ]:


import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
    from datetime import datetime
    t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2= datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return str(int(abs((t1-t2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')

    fptr.close()


# # ERROR AND EXCEPTIONS

# #### Exceptions

# In[ ]:


T = input()
for i in range(int(T)):
    a, b = input().split()
    try:
        print(int(int(a)/int(b)))
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')
    except ValueError as e:
        print('Error Code:', e)


# # BUILT-INS

# #### Zipped!

# In[ ]:


N, X = input().split()
l = []
for i in range(int(X)):
    voti = input().split()
    l.append(voti)
A = list(zip(*l))
for i in A:
    somma = 0
    for j in i:
        somma = somma + float(j)
    lung = len(i)
    print(somma/lung)


# #### Athlete Sort

# In[ ]:


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
from operator import itemgetter
arr = sorted(arr,key=itemgetter(k))
for i in arr:
    print(*i)


# #### ginortS

# In[ ]:


s = input()
s1 = ''
s2 = ''
s3 = ''
s4 = ''
for i in s:
    if i.isalpha() == True and i.isupper() == False:
        s1 = s1 + i
    if i.isupper() == True:
        s2 = s2 + i
    if i.isnumeric() == True:
        if int(i)%2 == 1:
            s3 = s3 + i
        elif int(i)%2 == 0:
            s4 = s4 + i    
s1 = sorted(s1)
s1 = ''.join(s1)
s2 = sorted(s2)
s2 = ''.join(s2)
s3 = sorted(s3)
s3 = ''.join(s3)
s4 = sorted(s4)
s4 = ''.join(s4)
print(s1+s2+s3+s4)


# # PYTHON FUNCTIONALS

# #### Map and Lambda Function

# In[ ]:


cube = lambda x: x**3

def fibonacci(n):
    l = []
    i = 0
    n1 = 0
    n2 = 1
    while i < n:
        l.append(n1)
        n3 = n1+n2
        n1=n2
        n2 = n3
        i +=1
    return l        
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# # REGEX AND PARSING

# #### Detect Floating Point Number

# In[ ]:


import re
T = input()
for i in range(int(T)):
    x = re.match('^[+-]{0,1}[\d]{0,}\.\d+$', input())
    if x:
        print('True')
    else:
        print('False')

#searched on google how to perform the pattern


# #### Re.split()

# In[ ]:


regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))


# #### Group(), Groups() & Groupdict()

# In[ ]:


s = str(input())
i = 0
l=[]
while i<len(s)-1:
    if s[i] == s[i+1] and (s[i].isdigit() or s[i].isalpha()):
        l.append(s[i])
    i +=1
if len(l)>=1:
    print(l[0])
else:
    print('-1')


# #### Re.findall() & Re.finditer()

# In[ ]:


import re
stringa = input()
pattern = re.compile(r"(?<![AEIOU])([AEIOU]{2,})(?![AEIOU]).",re.I)
lista = pattern.findall(stringa)
if len(lista)>0:
    print(*lista,sep='\n')
else:
    print(-1)
#searched the web for the pattern 


# #### Re.start() & Re.end()

# In[ ]:


import re
s = str(input())
k = str(input())
l =[]
for i in range(len(s)):
    if s[i:i+len(k)] == k:
        l.append((i,i+len(k)-1))
if len(l)>=1:
    print(*l, sep = '\n')
else:
    print((-1,-1))


# #### Regex Substitution

# In[ ]:


import re
for i in range(int(input())):
    s = re.sub("(?<=\s)&&(?=\s)", "and", input())
    print(re.sub("(?<=\s)\|\|(?=\s)", "or", s))
#searched the web for the pattern 


# #### Validating Roman Numerals

# In[ ]:


regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	
# Do not delete 'r'

import re
print(str(bool(re.match(regex_pattern, input()))))
#just searched for the beginning of the pattern and then completed the rest by myself


# #### Validating phone numbers

# In[ ]:


import re
N = input()
for i in range(int(N)):
    s = input()
    if re.match(r"7|8|9",s) and len(s) == 10 and s.isdigit():
        print('YES')
    else:
        print('NO')


# #### Validating and Parsing Email Addresses

# In[ ]:


import re
n = int(input())
pattern = r'<[a-zA-Z][\w.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}>'
for i in range(n):
    email = input().split()
    if re.match(pattern,email[1]):
        print(*email)
#searched the web for the pattern 


# #### Hex Color Code

# In[ ]:


import re 
N = int(input())
for i in range(N):
    s = input()
    c = re.findall(r'[\s:](#[0-9a-fA-F]{3,6})',s)
    for k in c:
        if len(k) == 7 or len(k) == 4:
            print(k)
#searched the web for the pattern 


# #### Validating UID

# In[ ]:


import re
T = int(input())
pattern = r"^(?=(?:.*[A-Z]){2})(?=(?:.*[0-9]){3})(?:([a-zA-Z0-9])(?!.*\1)){10}$"
for i in range(T):
    if re.match(pattern, input()):
        print('Valid')
    else:
        print('Invalid')
#searched the web for the pattern 


# # XML

# #### XML 1 - Find the Score

# In[ ]:


import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    sum=len(node.attrib)
    for i in node:
        sum+=get_attr_number(i)
    return sum
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# #### XML2 - Find the Maximum Depth

# In[ ]:


import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    for i in elem:
        depth(i, level+1)
    maxdepth = max(level+1, maxdepth)
    return maxdepth
    
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


# # CLOSURES AND DECORATORS

# #### Standardize Mobile Number Using Decorators

# In[ ]:


def wrapper(f):
    def fun(l):
        lista =  []
        for i in l:
            lista.append('+91 '+i[-10:-5]+' '+ i[-5:])
        return f(lista)
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


# #### Decorators 2 - Name Directory

# In[ ]:


import operator

def person_lister(f):
    def inner(people):
        people.sort(key = lambda x:int(x[2]))
        l = []
        for i in people:
            l.append(f(i))
        return l
    return inner
    
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


# # NUMPY

# #### Arrays

# In[ ]:


import numpy

def arrays(arr):
    arr.reverse()
    arr1 = numpy.array(arr, float)
    return arr1
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# #### Shape and Reshape

# In[ ]:


import numpy
n = list(map(int, input().split()))
arr = numpy.array(n)
arr.shape = (3,3)
print(arr)


# #### Transpose and Flatten

# In[ ]:


import numpy
N, M =input().split()
l = []
for i in range(int(N)):
    a = list(map(int, input().split()))
    l.append(a)
arr=numpy.array(l)
print (numpy.transpose(arr))
print (arr.flatten())


# #### Concatenate

# In[ ]:


import numpy
N, M, P = map(int, input().split())
l = []
l1 = []
for i in range(N):
    s = list(map(int, input().split()))
    l.append(s)
    arr=numpy.array(l)
for i in range(M):
    s = list(map(int, input().split()))
    l1.append(s)
    arr1=numpy.array(l1)
print(numpy.concatenate((arr,arr1)))


# #### Zeros and Ones

# In[ ]:


import numpy
N = list(map(int,input().split()))
print(numpy.zeros(N, dtype = numpy.int))
print(numpy.ones(N, dtype = numpy.int))


# #### Eye and Identity

# In[ ]:


import numpy
numpy.set_printoptions(legacy = '1.13')
n, m= map(int, input().split())
print(numpy.eye(n,m))


# #### Array Mathematics

# In[ ]:


import numpy
N, M = input().split()
arr1 = numpy.array([list(map(int, input().split())) for i in range(int(N))])
arr2 = numpy.array([list(map(int, input().split())) for i in range(int(N))])
print(numpy.add(arr1,arr2))
print(numpy.subtract(arr1,arr2))
print(numpy.multiply(arr1,arr2))
print(numpy.floor_divide(arr1,arr2))
print(numpy.mod(arr1,arr2))
print(numpy.power(arr1,arr2))


# #### Floor, Ceil and Rint

# In[ ]:


import numpy
numpy.set_printoptions(legacy = '1.13')
A = input().split()
arr = numpy.array(list(map(float, A)))
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))


# #### Sum and Prod

# In[ ]:


import numpy
N, M = (input().split())
arr = numpy.array([list(map(int, input().split())) for i in range(int(M))])
print(numpy.prod(numpy.sum(arr, axis=0), axis=None))


# #### Min and Max

# In[ ]:


import numpy
N,M= input().split()
arr = numpy.array([list(map(int, input().split())) for i in range(int(N))])
print(numpy.max(numpy.min(arr, axis = 1), axis = None))


# #### Mean, Var, and Std

# In[ ]:


import numpy
N, M = list(map(int, input().split()))
l = []
for i in range(N):
    s = list(map(int, input().split()))
    l.append(s)
    arr = numpy.array(l)
print (numpy.mean(arr, axis = 1))
print (numpy.var(arr, axis=0))
stan = round(numpy.std(arr), 11)
print(stan)


# #### Dot and Cross

# In[ ]:


import numpy
N = int(input())
arr1 = numpy.array([list(map(int, input().split())) for i in range(N)])
arr2 = numpy.array([list(map(int, input().split())) for i in range(N)])
print(numpy.dot(arr1,arr2))


# #### Inner and Outer

# In[ ]:


import numpy
arr1 = list(map(int, numpy.array(input().split())))
arr2 = list(map(int, numpy.array(input().split())))
print(numpy.inner(arr1,arr2))
print(numpy.outer(arr1,arr2))


# #### Polynomials

# In[ ]:


import numpy
P = list(map(float, input().split()))
x = float(input())
print(numpy.polyval(P,x))


# #### Linear Algebra

# In[ ]:


import numpy
N = int(input())
arr = numpy.array([list(map(float, input().split())) for i in range(N)])
print(round(numpy.linalg.det(arr),2))

