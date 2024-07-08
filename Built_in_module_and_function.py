# Built in Modules and Functions
# To check built in function in python
#1
a = dir(__builtins__)
print(a)

#2
s = pow(2,3)
print(s)

#3
kj=help(max)
print(kj)

#4
#Square root number is math
import math
l = math.sqrt(16)
print(l)

#5
import math
p = dir(math)
print(p)

#6
a = math.__doc__
print(a)

#7
def sayhello():
    """This is the function docstring """
    return "hello world"
print(sayhello())

#8
d = 123
y = str(d)
print(y)