# ------------------------------------------------
# class Fraction
# Attributes: numerator,denominator
# ------------------------------------------------
class Fraction(object):
# ------------- Constructor ----------------------
    def __init__(self,num=0,den=1):
        self.numerator = num
        self.denominator = den
# ------------- Print Fraction -------------------
    def printFraction(self):
        if self.denominator == 1:
            print(self.numerator)
        elif self.numerator > self.denominator:
            print('{0} {1}/{2}'.format(self.numerator//self.denominator,self.numerator%self.denominator,self.denominator))            
        else:
            print('{0}/{1}'.format(self.numerator,self.denominator))
# ------------- Real Number ----------------------
    def RealNum(self):
        if self.denominator == 1:
            return float(self.numerator)
        return self.numerator/self.denominator
# ------------- Fractions Reduction --------------
    def Reduction(self):
        den = self.denominator-1
        flag = False
        while den > 0 and flag == False:
            flag = (self.numerator%den == 0)and(self.denominator%den == 0)
            if flag == False:
                den -= 1
        if flag == True:
            self.numerator //= den
            self.denominator //= den
        return self

# ------------- Adding Fractions -----------------
    def __add__(self,other):
        self.numerator=self.numerator*other.denominator+other.numerator*self.denominator
        self.denominator*=other.denominator
        return self.Reduction()
# ------------- Return Object - srt -----------------
    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

# ------------- Driver ---------------------------
def driver():
    num1 = Fraction(6,9)
    num2 = Fraction(1,4)
    num1.printFraction()                # => 6/9
    (num1.Reduction()).printFraction()  # => 2/3
    print(num1.RealNum())               # => 0.6666666666666666 
    print('----------')
    (num1+num2).printFraction()         # => 11/12
    print('----------')
    num3 = Fraction(1,6)                
    num4 = Fraction(1,3)
    (num3+num4).printFraction()         # => 1/2
    print('----------')
    num5 = Fraction(23,7)   
    num5.printFraction()                # => 3 2/7

#driver()
num1 = Fraction(6,9)
num2 = Fraction(1,2)
#Fraction.printFraction(num1)
#print(Fraction.__dict__)
#print((str(num1)))
Fraction.x=100
num1.x=10
#print("Fraction.x = ", Fraction.x)
#print("num1 =",num1.x)
#print("num2 =",num2.x)
#num2.x=1000
#print(Fraction.x)
#print("num1 =",num1.x)
#print("num2 =",num2.x)

#print(num1.__dict__) # or print(vars(num1))
#print(Fraction.__dict__.values())


# ======================= 1 =======================
def foo():
    def foo1(q):
        return q+100
    def foo2(w):
        return  w+200
    def foo3(e):
        return e+300
    return {"foo1": foo1,"foo2": foo2,"foo3":foo3}

res=foo()
#print(res["foo1"](0))
# ======================= 2 =======================
def foo():
    def foo1(q):
        return q + 100
    def foo2(w):
        return w + 200
    def foo3(e):
        return e + 300
    def dispatch(m,num):
        if m == 'foo1':
            return foo1(num)
        elif m == 'foo2':
            return foo2(num)
        elif m == 'foo3':
            return foo3(num)
    return dispatch
res = foo()
#print(res("foo1",0))
# ======================= 3 =======================
def foo(x,y,z):
    def dispatch(m):
        if m == 1:
            return x
        elif m == 2:
            return y
        else: return z
    return dispatch
res = foo(10,20,30) # or foo(10,20,30)(1)
#print(res(1))

def foo():
    pass

# =================================================
# =================================================
# =================================================

# =================================================
# Create a Class

#Create a class named MyClass, with a property named x
class MyClass:
  x = 5

# =================================================
# Create Object

# Create an object named p1, and print the value of x:
p1 = MyClass()
#print(p1.x)

# =================================================

# The __init__() Function

"""
All classes have a function called __init__(), which is 
always executed when the class is being initiated.

Use the __init__() function to assign values to object 
properties, or other operations that are necessary to 
do when the object is being created.
"""

# Create a class named Person, use the __init__() function 
# to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

#print(p1.name)
#print(p1.age)

"""
Note: The __init__() function is called automatically 
every time the class is being used to create a new object.
"""

# =================================================

# Object Methods

"""
Objects can also contain methods. Methods in objects 
are functions that belong to the object.
"""

# Insert a function that prints a greeting, and execute it 
# on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
#p1.myfunc()

# =================================================

# The self Parameter

"""
Note: The self parameter is a reference to the current 
instance of the class, and is used to access variables 
that belong to the class.
"""
"""
The self parameter is a reference to the current instance 
of the class, and is used to access variables that belongs 
to the class. It does not have to be named self , you 
can call it whatever you like, but it has to be the first 
parameter of any function in the class:
"""

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
#p1.myfunc()

# =================================================

# Modify Object Properties

# You can modify properties on objects like this:
# Set the age of p1 to 40:

p1.age = 40

# =================================================

# Delete Object Properties

"""
You can delete properties on objects by using the del keyword.
"""

# Delete the age property from the p1 object:
#print(p1.age)
del p1.age
#print(p1.age)

# The pass Statement

"""
Class definitions cannot be empty, but if you for some 
reason have a class definition with no content, put in 
the pass statement to avoid getting an error.
"""

# =================================================

# Python Inheritance

"""
Inheritance allows us to define a class that inherits 
all the methods and properties from another class.
Parent -  class is the class being inherited from, 
also called base class.
Child - class is the class that inherits from 
another class, also called derived class.
"""
# =================================================

# Create a Parent Class

# Create a class named Person, with firstname and lastname
# properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# Use the Person class to create an object, and then 
# execute the printname method:

x = Person("John", "Doe")
#x.printname()

# =================================================

# Create a Child Class

"""
To create a class that inherits the functionality 
from another class, send the parent class as a 
parameter when creating the child class:
"""

# Create a class named Student, which will inherit
# the properties and methods from the Person class:

class Student(Person):
  pass


"""
Note: Use the pass keyword when you do not want 
to add any other properties or methods to the class.
"""

# Use the Student class to create an object, 
# and then execute the printname method:

x = Student("Mike", "Olsen")
#x.printname()

# =================================================

# Add the __init__() Function

"""
So far we have created a child class that inherits 
the properties and methods from its parent.
We want to add the __init__() function to the 
child class (instead of the pass keyword)
"""

# Add the __init__() function to the Student class:

#class Student(Person):
  #def __init__(self, fname, lname):
    #add properties etc

"""
When you add the __init__() function, the 
child class will no longer inherit the parent's 
__init__() function.
"""

# To keep the inheritance of the parent's __init__() 
# function, add a call to the parent's __init__() function:

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)


"""
Now we have successfully added the __init__() 
function, and kept the inheritance of the parent class, 
and we are ready to add functionality in 
the __init__() function.
"""

# =================================================

# Use the super() Function
"""
Python also has a super() function that will 
make the child class inherit all the methods 
and properties from its parent:
"""

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)


"""
By using the super() function, you do not have to 
use the name of the parent element, it will 
automatically inherit the methods and properties 
from its parent.
"""

# =================================================

# Add Properties

# Add a property called graduationyear to the Student class:
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

"""
In the example below, the year 2019 should be a 
variable, and passed into the Student class when 
creating student objects. To do so, add another 
parameter in the __init__() function:
"""

# Add a year parameter, and pass the correct year when creating objects:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

# =================================================

# Add Methods

# Add a method called welcome to the Student class:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

"""
If you add a method in the child class with the 
same name as a function in the parent class, 
the inheritance of the parent method will be overridden.
"""

# =================================================

# Call Parent class method
# Python code to demonstrate 
# parent call method 
class Parent:
  
    # create a parent class method
    def show(self):
        print("Inside Parent class")
  
# create a child class
class Child(Parent):
      
    # Create a child class method
    def display(self):
        print("Inside Child class")
  
# Driver's code
obj = Child()
#obj.display()
  
# Calling Parent class
#obj.show()

# Python program to demonstrate
# calling the parent's class method
# inside the overridden method
class Parent():
	
	def show(self):
		print("Inside Parent")
		
class Child(Parent):
	
	def show(self):
		
		# Calling the parent's class
		# method
		Parent.show(self)
		print("Inside Child")
		
# Driver's code
obj = Child()
#obj.show()


# Python program to demonstrate
# calling the parent's class method
# inside the overridden method using
# super() 
class Parent():
      
    def show(self):
        print("Inside Parent")
          
class Child(Parent):
      
    def show(self):
          
        # Calling the parent's class
        # method
        super().show()
        print("Inside Child")
          
# Driver's code
obj = Child()
#obj.show()


# Program to define the use of super() 
# function in multiple inheritance 
class GFG1: 
    def __init__(self): 
        print('HEY !!!!!! GfG I am initialised(Class GEG1)') 
    
    def sub_GFG(self, b): 
        print('Printing from class GFG1:', b) 
    
# class GFG2 inherits the GFG1 
class GFG2(GFG1): 
    def __init__(self): 
        print('HEY !!!!!! GfG I am initialised(Class GEG2)') 
        super().__init__() 
    
    def sub_GFG(self, b): 
        print('Printing from class GFG2:', b) 
        super().sub_GFG(b + 1) 
    
# class GFG3 inherits the GFG1 ang GFG2 both 
class GFG3(GFG2): 
    def __init__(self): 
        print('HEY !!!!!! GfG I am initialised(Class GEG3)') 
        super().__init__() 
    
    def sub_GFG(self, b): 
        print('Printing from class GFG3:', b) 
        super().sub_GFG(b + 1) 
    
    
# main function 
#if __name__ == '__main__': 
    
    # created the object gfg 
    #gfg = GFG3() 
    
    # calling the function sub_GFG3() from class GHG3 
    # which inherits both GFG1 and GFG2 classes 
    #gfg.sub_GFG(10)
    
# =================================================

# Calling a child method in a parent class in Python

class Parent:
    def makeChildrenStopCry(self):
        if self.cry():
            self.doWhateverToStopCry()

class Children(Parent):
    crying = False
    def makeCry(self):
        self.crying = True
    def doWhateverToStopCry(self):
        self.crying = False
    def cry(self):
        return self.crying

child = Children()
child.makeCry()
print(child.crying)

child.makeChildrenStopCry()
print(child.crying)

