#               lambda
from filecmp import cmp


def foo(x): return x**2
#print(foo(4))

g=lambda x: x**2
#print(g(4))

g=lambda x,y,z:(x+z)/y
#print(g(2,3,4))

#print((lambda x,y,z:(x+z)/y)(2,3,4))

#print((lambda :1)())

def make_incrementor(n):return lambda x: x+n
#f=make_incrementor(2)(3,3)
#print(f)
#f=make_incrementor(2)
#g=make_incrementor(6)
#print(f(42),g(42))
#print(make_incrementor(2)(42))

#print((lambda x,y:x or y)(7%2==1,8>0))
#print((lambda x,y:x and y)(7%2==1,8>0))
#f=lambda x,y:x%2==1 and y>0
#f(7,8)

#               list
"""
Python offers the following list functions:

sort(): Sorts the list in ascending order.
type(list): It returns the class type of an object.
append(): Adds a single element to a list.
extend(): Adds multiple elements to a list.
index(): Returns the first appearance of the specified value.
max(list): It returns an item from the list with max value.
min(list): It returns an item from the list with min value.
len(list): It gives the total length of the list.
list(seq): Converts a tuple into a list.
cmp(list1, list2): It compares elements of both lists list1 and list2
"""
temp=[1,1,1,1]
myList = [1,5,4,3,2]


#myList.sort()
#print(myList)

myList.append(22)
#print(myList)



myList.extend([6,7,8,9])
#print(myList)
#print(min(myList))

myTuple=(1,2,3,4)
#print(list(myTuple))

#for x in myList:
    #print(x,end='')
#print(len(myList))

#for x in range(len(myList)-1,-1,-1):
    #print(myList[x])

#for x in range(len(myList)):
    #print(myList[x])

myList=["dsf",3,4,5,3.4,(1,2,3,4)]
#print(myList)

myList[0]=3
#print(myList)


#               filter() map() reduce()
# filter(function, sequence)
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
#print(less_than_zero)


"""
# function that filters vowels
def fun(variable):
    
    letters = ['a', 'e', 'i', 'o', 'u', 's']
    if (variable in letters):
        return True
    
    return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for x in filtered:
    print(x)

"""
# map(function_to_apply, list_of_inputs)
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

# reduce
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
#print(product)
#from functools import reduce
#product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

#               High Order Function
# 1. accept other function as arguments
# 2. return function as values

def summation(low,high,function,next):
    total=0
    while low<=high:
        total+=function(low)
        low=next(low)
    return total
def nextTwo(k):
    return k+2
#print(summation(0,5,lambda x:x**2,lambda x:x+1))
#print(summation(0,5,lambda x:x**2,nextTwo))

#===============================
def power1(n):
    def calculate(x):
        return x**n
    return  calculate

def power2(n):
    return lambda x:x**n

f=power1(3)
g=power2(3)
#print(f(2),g(2))