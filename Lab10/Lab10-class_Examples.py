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
Fraction.printFraction(num1)
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
print(res("foo1",0))
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
print(res(1))

def foo():
    pass