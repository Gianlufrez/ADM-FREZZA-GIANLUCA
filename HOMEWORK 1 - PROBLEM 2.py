#!/usr/bin/env python
# coding: utf-8

# # Birthday Cake Candles

# In[ ]:


import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    c = candles.count(max(candles))
    return c
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


# # Number Line Jumps

# In[ ]:


import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    if v1<v2:
        return 'NO'
    if v1>v2:
        for i in range(100000):
            primo = x1+(v1*i)
            secondo = x2+(v2*i)
            if primo == secondo:
                return 'YES'
        if primo>secondo:
            return 'NO'
    else:
        if x1%2 != x2%2:
            return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# # Viral Advertising

# In[ ]:


import math
import os
import random
import re
import sys

def viralAdvertising(n):
    i = 1
    persone = 5
    cumulative = 2
    while i<n:
        persone = (persone//2)*3
        cumulative = cumulative + persone//2
        i +=1
    return cumulative
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# # Recursive Digit Sum

# In[ ]:


import math
import os
import random
import re
import sys

def superDigit(n, k):
    if int(n) < 10 :
        return n
    somma = 0
    for i in n :
        somma = somma + int(i)
    somma = somma * k
    k = 1
    return superDigit(str(somma) , 1)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# # Insertion Sort - Part 1

# In[ ]:


import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    for i in range((n-1),0,-1):
        if arr[i] < arr[i-1]:
            elemento = arr[i]
            arr[i] = arr[i-1]
            print(*arr)
            arr[i-1] = elemento
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# # Insertion Sort - Part 2

# In[ ]:


import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
    for i in range(1, n):
        for j in range(0, i+1):
            if arr[j] > arr[i]:
                posizione = arr[j]
                arr[j] = arr[i]
                arr[i] = posizione
        print(*arr)
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

