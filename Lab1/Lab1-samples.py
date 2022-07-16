# ----------------------------------------------------------
# Sample 1 

# 2 3.14159265359 abcd!@#$
# 5.14159265359 15.93480220054533 1 3
# a=2, b=3.14159265359, c=abcd!@#$ next b=3.14 end
#     2,3.1416    ,abcd!@#$
"""
a,b,c = 2, 3.14159265359, 'abcd!@#$'
print(a,b,c)

n1,n2 = a+b, (b**a)/2.0+11
print(n1, n2, int(b//a), 15%4)

print('a={0}, b={1}, c={2} next'.format(a,b,c),'b={0:.2f} end'.format(b))
print('{0:>5d},{1:<10.4f},{2}'.format(a,b,c))
"""

# ----------------------------------------------------------
# Sample 2 - IF Sample

# Enter Number: -7
# Negative number
# Enter a One-Digit number: 89
# It's not a one-digit number
"""
num=int(input('Enter Number: '))

if num > 0:
    print('Positive number')

if num==0:
    print('Zero')
elif num>0:
    print('Positive number')
else:
    print('Negative number')

num=int(input('Enter a One-Digit number: '))

# num >= 0 and num < 10
if 0 <= num < 10:
    print('This one-digit number')
else:
    print("It's not a one-digit number")
"""

# ----------------------------------------------------------
# Sample 3 - Loop Sample

# Enter number[1-9]: 7
#
# 0123456
# -------
#       1
#      12
#     123
#    1234
#   12345
#  123456
# 1234567
# -------
# 7654321
# 1|2|3|4|5|6|7|
#

"""
#========================================================
# input number
n = int(input('Enter number[1-9]: '))
print()

# Reads two numbers from input and typecasts them to int using 
# list comprehension
x, y = [int(x) for x in input().split()]  

# list comprehension example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)


# Reads two numbers from input and typecasts them to int using 
# map function
x, y = map(int, input().split())

#========================================================

# range(n) from 0 to n-1, step 1
for i in range(n):
    print(i,end='')
print()

# range(n) from 0 to n-1, step 1
for i in range(n):
    print('-',end='')
print()

# range(n+1) from 1 to n, step 1 
for i in range(1,n+1):

    # range(i) from 0 to n-i-1, step 1
    for j in range(n-i):
        print(end=' ')

    # range(i) from 1 to i-1, step 1
    for j in range(i):
        print(j+1,end='')
    print()

# range(n) from 0 to n-1, step 1
for i in range(n):
    print('-',end='')
print()

# range(n,0,-1) from n to 1, step -1
for i in range(n,0,-1):
    print(i,end='')

print()
i=1
while i <= n:
    print(i,end='|')
    i+=1
"""

# =================================================================
"""
x=1
print('foramt is {0}, id = {1}, and {other}.'.format(type(x), id(x), other ='lab1'))

y=1
print('x id = {0}, y id = {1}.'.format(id(x), id(y)))

print('x id = {0}, y id = {1}.'.format(id(x), id(y)))

"""


# ==================== Code to swap 'x' and 'y' ====================
# ==================== 1 ====================
"""
x = 10
y = 5


# x now becomes 15
x = x + y

# y becomes 10
y = x - y
# x becomes 5
x = x - y
print("After Swapping: x =", x, " y =", y)
"""
# ==================== 2 ====================
"""
x = 10
y = 5
 
# code to swap
# 'x' and 'y'
 
# x now becomes 50
x = x * y
 
# y becomes 10
y = x // y
 
# x becomes 5
x = x // y
 
print("After Swapping: x =",x, " y =", y)
"""
# ==================== 3 ====================
"""
x = 10
y = 5
 
# Code to swap 'x' and 'y'
x = x ^ y; # x now becomes 15 (1111)
y = x ^ y; # y becomes 10 (1010)
x = x ^ y; # x becomes 5 (0101)
 
print ("After Swapping: x = ", x, " y =", y)
"""
# ==================== 4 ====================
"""
def swap(xp, yp):
 
    xp[0] = xp[0] ^ yp[0]
    yp[0] = xp[0] ^ yp[0]
    xp[0] = xp[0] ^ yp[0]
 
 
# Driver code
x = [10]
swap(x, x)
print("After swap(&x, &x): x = ", x[0])
"""
# ==================== 5 ====================
"""
def swap(xp, yp):
 
    # Check if the two addresses are same
    if (xp[0] == yp[0]):
        return
    xp[0] = xp[0] + yp[0]
    yp[0] = xp[0] - yp[0]
    xp[0] = xp[0] - yp[0]
 
 
# Driver Code
x = [10]
swap(x, x)
print("After swap(&x, &x): x = ", x[0])
"""

# ==================== 6 ====================
"""
def swap(a, b):
 
    # Same as a = a + b
    a = (a & b) + (a | b)
 
    # Same as b = a - b
    b = a + (~b) + 1
 
    # Same as a = a - b
    a = a + (~b) + 1
 
    print("After Swapping: a = ", a, ", b = ", b)
 
 
# Driver code
a = 5
b = 10
 
# Function call
swap(a, b)
"""
# ==================== 7 ====================
"""
def swap(x, y):
  x , y = y, x
  print("After Swapping: x = ", x, ", y = ", y)
   
# Driver code
x = 10
y = 5
  
# Function call
swap(x, y)
"""
# =============================================================
"""
a=b=c=5
print(a,b,c)

print(7 % 3, 7/3, 7//3, 2**3)

import math
print(math.pi)
from math import pi
print(pi)

print(int("10"))
"""
# format ========================================================
"""
a,b,c = 2, 3.14159265359, 'abcd!@#$'

print('a={0}, b={1}, c={2} next'.format(a,b,c),'b={0:.2f} end'.format(b))

print('{0:>5d},{1:<10.4f},{2}'.format(a,b,c))
print('{0:^5d},{1:>10.4f},{2}'.format(a,b,c))

#x=int(input('Enter int: '))

# range ==========================================================
print(tuple(range(4)))
print(range(4))
print(tuple(range(3,8)))
print(tuple(range(8,3,-2)))
"""
# loop ============================================================
"""
for x in range(1,8):
	print(x)
for x in range(1,8):
	print(x,end=' ')
for x in range(1,8):
	print(x,end='$')
for _ in range(1,8):
	print('$')

i=1
n=10
while i <= n:
    print(i,end='|')
    i+=1

print("\n ")
ACCEPTED_EXTENSIONS     = ('jpg', 'jpeg', 'tif', 'tiff', 'png') 

print(ACCEPTED_EXTENSIONS[0])
"""
# lambda ============================================================
"""
def foo(x):
    def foo2(y):
        y+=10
        return y/2
    return foo2(x)




res = lambda x: x

print(type(res))
print("lambda", res(foo(5)))

print("foo", foo(5))

print("(lambda x: foo(x))(foo(5))", (lambda x: foo(x))(foo(5)))

def foo3(foo):

    return foo(foo(5))

print("foo3", foo3(foo))
"""
# lambda/global ============================================================

print("global")
x=3
def interesting(x):

        def because(y):
                global x
                x=y
        because(5)
        return x
print(interesting(5))
print(x)
print("nonlocal")
x=3
def interesting(x):

        def because(y):
                nonlocal x
                x=y
        because(5)
        return x
print(interesting(5))
print(x)