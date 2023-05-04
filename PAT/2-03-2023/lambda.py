
"""def add_sub(a,b):
    if(a>b):
        return a
    else:
        return b
a=lambda x,y:x+y
b=lambda p,q:p-q
a=a(3,4)
b=b(5,6)

print(add_sub(a,b))"""

"""convert 17-base to decimal
num=str(input())
print(int(num,17))"""

""" sum of n natural numbers using lambda

def natural(y):
    return (lambda x:x+1)(y)
a=100
print(a)
b=natural(a)
print(b)"""

"""method 1
def natural(y):
    return (lambda n:n*(n+1)//2)(y)
y=natural(10)
print(y)

method 2"""

x=lambda: sum(range(1,11))
print(x())
