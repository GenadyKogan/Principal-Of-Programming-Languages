Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+3
5
>>> print('abcd')
abcd
>>> 
===================== RESTART: C:/Users/misha/Desktop/1.py =====================
abcd
123
>>> 
===================== RESTART: C:/Users/misha/Desktop/1.py =====================
abcd
123
>>> printa('abcd')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    printa('abcd')
NameError: name 'printa' is not defined
>>> x=1
>>> type(x)
<class 'int'>
>>> id(x)
2076567472
>>> y=1
>>> type(y)
<class 'int'>
>>> id(y)
2076567472
>>> y=2
>>> id(y)
2076567488
>>> x=3.56
>>> type(x)
<class 'float'>
>>> id(x)
61718144
>>> x='ewertwert'
>>> type(x)
<class 'str'>
>>> x=1
>>> id(x)
2076567472
>>> x,y=3,4
>>> x
3
>>> y
4
>>> x,y=y,x
>>> x
4
>>> y
3
>>> a,b,c = 2, 3.14159265359, 'abcd!@#$'
>>> a
2
>>> a+b
5.14159265359
>>> 7%3
1
>>> 7/3
2.3333333333333335
>>> 7//3
2
>>> 2**3
8
>>> n1,n2 = a+b, (b**a)/2.0+11
>>> n1
5.14159265359
>>> n2
15.93480220054533
>>> print(n1, n2, int(b//a), 15%4)
5.14159265359 15.93480220054533 1 3
>>> int(3)
3
>>> int(3.5)
3
>>> int('123')
123
>>> print('a={0}, b={1}, c={2} next'.format(a,b,c),'b={0:.2f} end'.format(b))
a=2, b=3.14159265359, c=abcd!@#$ next b=3.14 end
>>> 'a={0}, b={1}, c={2} next'.format(a,b,c)
'a=2, b=3.14159265359, c=abcd!@#$ next'
>>> 'a={2}, b={0}, c={2} next'.format(a,b,c)
'a=abcd!@#$, b=2, c=abcd!@#$ next'
>>> print('{0:>5d},{1:<10.4f},{2}'.format(a,b,c))
    2,3.1416    ,abcd!@#$
>>> print('{0:^5d},{1:<10.4f},{2}'.format(a,b,c))
  2  ,3.1416    ,abcd!@#$
>>> input()
sfgfghf
'sfgfghf'
>>> input()
234
'234'
>>> input('Enter int: ')
Enter int: 45
'45'
>>> x=input('Enter int: ')
Enter int: 45
>>> x+1
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    x+1
TypeError: can only concatenate str (not "int") to str
>>> x
'45'
>>> x=int(input('Enter int: '))
Enter int: 45
>>> x
45
>>> x+1
46
>>> x++
SyntaxError: invalid syntax
>>> x=x+1
>>> x
46
>>> tuple(range(4))
(0, 1, 2, 3)
>>> range(4)
range(0, 4)
>>> tuple(range(3,8))
(3, 4, 5, 6, 7)
>>> tuple(range(3,8,2))
(3, 5, 7)
>>> tuple(range(8,3,-1))
(8, 7, 6, 5, 4)
>>> tuple(range(8,3))
()
>>> tuple(range(8,0,-1))
(8, 7, 6, 5, 4, 3, 2, 1)
>>> for x in range(8):
	print(x)

	
0
1
2
3
4
5
6
7
>>> for x in range(1,8):
	print(x)

	
1
2
3
4
5
6
7
>>> for x in range(1,8):
	print(x,end=' ')

	
1 2 3 4 5 6 7 
>>> for x in range(1,8):
	print(x,end=',')

	
1,2,3,4,5,6,7,
>>> for x in range(1,8):
	print(x,end='$')

	
1$2$3$4$5$6$7$
>>> for x in range(1,8):
	print(x,end='')

	
1234567
>>> for x in range(1,8):
	print('$')

	
$
$
$
$
$
$
$
>>> for _ in range(1,8):
	print('$')

	
$
$
$
$
$
$
$
>>> i=1
>>> while i <= n:
    print(i,end='|')
    i+=1

    
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    while i <= n:
NameError: name 'n' is not defined
>>> n=9
>>> while i <= n:
    print(i,end='|')
    i+=1

    
1|2|3|4|5|6|7|8|9|
>>> 