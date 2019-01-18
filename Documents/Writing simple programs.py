Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "copyright", "credits" or "license()" for more information.
>>> for i in range(5)
SyntaxError: invalid syntax
>>> for i in range(5):
	print (i * i)

	
0
1
4
9
16
>>> for d in [3,1,4,1,5]:
	print (d, end=" ")

	
3 1 4 1 5 
>>>  for i in range(4):
	print ("Hello")
	
SyntaxError: unexpected indent
>>> for i in range(4):
	print ("Hello")

	
Hello
Hello
Hello
Hello
>>> for i in range(5):
	print (i, 2 ** i)

	
0 1
1 2
2 4
3 8
4 16
>>> print("start")
for i in range(O):
	print("Hello")
	print("end")
	
SyntaxError: multiple statements found while compiling a single statement
>>> print ("start")
start
>>> for i in range(0):
	print("Hello")
	print("end") 
