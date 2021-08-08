#Q1
print ("start of lambda functions")
var=lambda x: x+2
print (var(4)) #6
var = lambda x: x**2+3*x-2
print (var(3))#16
var=lambda x,y: (x+y)/(x-y)
print (var(8,4))#3
print ("end of lambda functions")
print()

#Q2
import math

def integral1(a, b, f):
    dx = (b-a)/100

    def sum_of_func():
        total = 0
        for k in range(100):
            total += f(a + k*dx)
        return total
    return sum_of_func()*dx


#print(integral1(0, 1, lambda x: x**2))  #=> 0.3283500000000004
#print(integral1(0, math.pi, math.sin))  #=> 1.9998355038874451

def integral2(a, b, f):
    dx = (b-a)/100
    def sum_of_func():
        total = 0
        for k in range(100):
            total += f(a + k*dx)
        return total
    return (lambda x, y: x * y)(sum_of_func(), dx)


#print(integral2(0, 1, lambda x: x**2))  #=> 0.3283500000000004
#print(integral2(0, math.pi, math.sin))  #=> 1.9998355038874451


#Q3
def derived1(f):
    dx = 0.0001

    def calc(x):
        return (f(x+dx)-f(x))/dx
    return calc

print(derived1(lambda x: x**2)(3))  # => 6.0001…
print(derived1(math.sin)(math.pi))  # => -0.99999…
# ------- OR --------
def derived2(f):
    dx = 0.0001
    return lambda x: (f(x+dx)-f(x))/dx

print(derived2(lambda x: x**2)(3))  # => 6.0001…
print(derived2(math.sin)(math.pi))  # => -0.99999…

#Q4
def derived_twice(f):
    return derived1(derived1(f))
print("derived",derived1 (lambda x: x**2) (3))   
print("derived",derived2 (lambda x: x**2) (3))
print("derived",derived1  (math.sin) (math.pi) )
print(derived_twice(lambda x : x**2)(13))

#Q5
def f(x,y):
    return x*y**2-2*x*y

#Q5.1
def partial_derivat_x(pf):
    dx = 0.001
    return lambda x,y: (pf(x+dx,y)-pf(x,y))/dx

#Q5.2
def partial_derivat_y(pf):
    dy = 0.001
    return lambda x,y: (pf(x,y+dy)-pf(x,y))/dy

print ("partial_derivat_x ", partial_derivat_x (f)(2,3))
print ("partial_derivat_y ", partial_derivat_y(f)(2,3))
print()

#Q6
def like_fib(f):
    return lambda n: f(n-1)+f(n-2)
def f(n):
    return 5-n
def g():
    return like_fib(f)

print("Q6",g()(3))

#Q7
def smooth(f):
    return lambda x:(f(x-1)+f(x)+f(x+1))/3
def gg():
    return smooth(f)
print("Q7",gg()(2))##smooth(2)= (f(1)+f(2)+f(3))/3 = (4+3+2)/3 = 9/3 = 3








   
