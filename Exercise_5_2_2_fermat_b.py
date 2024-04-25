Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#write a script that uses "epoch" time in seconds and translates it into time in days, hours, minues, seconds
import time
time.time()
1714056360.1591203
def chour(t):
    hour = t/3600
    print("The number of hours that have passed since epoch began is %f" %hour)

    
def cminute(t):
    minute = t/(60)
    print("The number of minutes that have passed since epoch began is %f" %minute)

    
def cseconds(t):
    seconds = t
    print("The number of seconds that have passed since epoch began is %f" %seconds)

    
def tot_day():
    sec=time.time()
    tot_day = sec / (60*60*24)
    print("The number of days that have passed since epoch began is %f" %tot_day)

    
tot_day()
The number of days that have passed since epoch began is 19838.617983
chour(time.time())
The number of hours that have passed since epoch began is 476126.833611
cminute(time.time())
The number of minutes that have passed since epoch began is 28567610.234296
cseconds(time.time())
The number of seconds that have passed since epoch began is 1714056627.112891

================================ RESTART: Shell ================================
a=("Please test a: ")
print('a')
a
a=input("please test a: ")
please test a: 3.4
a
'3.4'
b=input(please test b: int()")
        
SyntaxError: unterminated string literal (detected at line 1)
b=input("please test b: int()")
        
please test b: int()4.5
b
        
'4.5'
c=input("please test c: %d")
        
please test c: %d5.5
c
        
'5.5'
c=input("please test c: "%d)
        
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    c=input("please test c: "%d)
NameError: name 'd' is not defined. Did you mean: 'id'?
c=input("please test c: %d"%d)
        
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    c=input("please test c: %d"%d)
NameError: name 'd' is not defined. Did you mean: 'id'?
print(int(b))
        
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(int(b))
ValueError: invalid literal for int() with base 10: '4.5'

================================ RESTART: Shell ================================
import math
#write a function to check Fermat's Last Theorum with positive integers and n values greater than 2.
def check_fermat(a,b,c,n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy Smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work")

        
#Fermat's Last Theorum states that there are no positive integers a, b, and c such that a^n + b^n = c^n for n >2.
        
check_fermat(3,4,6,3)
No, that doesn't work
check_fermat(5,2,8,4)
No, that doesn't work
check_fermat(15,9,22,6)
No, that doesn't work
def check_fermat_user():
    a=input("Please test for a: ")
    b=input("Please test for b: ")
    c=input("Please test for c: ")
    n=input("please test for n greater than 2: ")
    return check_fermat(a,b,c,n)

check_fermat_user()
Please test for a: 4
Please test for b: 3
Please test for c: 6
please test for n greater than 2: 7
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    check_fermat_user()
  File "<pyshell#55>", line 6, in check_fermat_user
    return check_fermat(a,b,c,n)
  File "<pyshell#43>", line 2, in check_fermat
    if n > 2 and a**n + b**n == c**n:
TypeError: '>' not supported between instances of 'str' and 'int'
def check_fermat_user():
    a=input("Please test for a: ")
    int([a])
    b=input("Please test for b: ")
    int([b])
    c=input("Please test for c: ")
    int([c])
    n=input("please test for n greater than 2: ")
    int([n])
    return check_fermat(a,b,c,n)

check_fermat_user()
Please test for a: 3
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    check_fermat_user()
  File "<pyshell#58>", line 3, in check_fermat_user
    int([a])
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
def check_fermat_user():
    a=input("Please test for a: ")
    int(a)
    b=input("Please test for b: ")
    int(b)
    c=input("Please test for c: ")
    int(c)
    n=input("please test for n greater than 2: ")
    int(n)
    return check_fermat(a,b,c,n)

check_fermat_user()
Please test for a: 3
Please test for b: 5
Please test for c: 4
please test for n greater than 2: 6
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    check_fermat_user()
  File "<pyshell#61>", line 10, in check_fermat_user
    return check_fermat(a,b,c,n)
  File "<pyshell#43>", line 2, in check_fermat
    if n > 2 and a**n + b**n == c**n:
TypeError: '>' not supported between instances of 'str' and 'int'
>>> def check_fermat_user():
...     a=input("Please test for a: ")
...     int("a")
...     b=input("Please test for b: ")
...     int("b")
...     c=input("Please test for c: ")
...     int("c")
...     n=input("please test for n greater than 2: ")
...     int("n")
...     return check_fermat(a,b,c,n)
... 
>>> check_fermat_user():
...     
SyntaxError: invalid syntax
>>> check_fermat_user()
Please test for a: 3
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    check_fermat_user()
  File "<pyshell#64>", line 3, in check_fermat_user
    int("a")
ValueError: invalid literal for int() with base 10: 'a'
>>> def check_fermat_user():
...     a_input=input("Please test for a: ")
...     a=int(a_input)
...     b_input=input("Please test for b: ")
...     b=int(b_input)
...     c_input=input("Please test for c: ")
...     c=int(c_input)
...     n_input=input("please test for n greater than 2: ")
...     n=int(n_input)
...     return check_fermat(a,b,c,n)
... 
>>> check_fermat_user()
Please test for a: 3
Please test for b: 4
Please test for c: 5
please test for n greater than 2: 6
No, that doesn't work
