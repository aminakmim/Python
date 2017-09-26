Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [1 ,2 , 5 , 6]
>>> b = list(enumerate(a))
>>> b
[(0, 1), (1, 2), (2, 5), (3, 6)]
>>> f = lambda x,y:x[0]+y[0],x[1]+y[1]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    f = lambda x,y:x[0]+y[0],x[1]+y[1]
NameError: name 'x' is not defined
>>> a = [i for i in range(100)]
>>> f = lambda x,y : x+y if x<10 else x
>>> from functools import reduce
>>> p = reduce(f,a)
>>> p
10
>>> q = reduce(f,enumerate(a))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    q = reduce(f,enumerate(a))
  File "<pyshell#5>", line 1, in <lambda>
    f = lambda x,y : x+y if x<10 else x
TypeError: unorderable types: tuple() < int()
>>> f = lambda x,y: x+y if x<10 else pass
SyntaxError: invalid syntax
>>> f = lambda x,y : x+y if x<34 else x
>>> p = reduce(f,a)
>>> p
36
>>> 
