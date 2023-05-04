class abc():
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self):
        return self.var-obj.var
obj=abc("klmnop",10)
print("The returned value is",repr(obj))
print("The lenght is",len(obj))
obj1=abc("abcdef",10)
val=abc.__cmp__(obj1)
if(val==0):
    print("both values are equal")
elif(val==-1):
    print("1st value is less than 2nd")
else:
    print("2nd value isless")

"""
__call__ acts as a funtion obj(ar1,ar2)
__it__
__le__
__eq__
__ne__
__gt__
__ge__
__add__
__sub__
__mul__
__truediv__
__pow__
__rshift__
__lshift__
__lt__
__iadd__
__isub__

__
__hash__ decides the place of the obj
__iter__ iteration on a object
__getitem__ used for indexing
__setitem__

"""

"""
in-built functions

getattr()
seattr()
delattr()


"""

"""
built-in class attributes

__dict__
__doc__ used for strings
__name__ returns name of the class
__module__ returns the module where the class is defined
__bases__  Mother of inheritance
"""


    
    
                
