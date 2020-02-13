Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=1
>>> a=2
>>> b=3
>>> c=4
>>> if n==1
SyntaxError: invalid syntax
>>> if n=1
SyntaxError: invalid syntax
>>> if n==1:
	print(a)
	end
	;
	
SyntaxError: invalid syntax
>>> if n<1
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> n
1
>>> if n>0
SyntaxError: invalid syntax
>>> if n>0 :
	print(b)
	;
	
SyntaxError: invalid syntax
>>> 
=================== RESTART: /home/user/RTR108/konsole.py ===================
Traceback (most recent call last):
  File "/home/user/RTR108/konsole.py", line 1, in <module>
    if n>0:
NameError: name 'n' is not defined
>>> n
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> 
=================== RESTART: /home/user/RTR108/konsole.py ===================
2
>>> n
1
>>> 2
2
>>> 3
3
>>> b
2
>>> c
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> 
