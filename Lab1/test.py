x = int(input("first number: "))
y = int(input("second number: "))
while(y!=0):
    z=x
    x=y
    y=z%y
print(x,y)