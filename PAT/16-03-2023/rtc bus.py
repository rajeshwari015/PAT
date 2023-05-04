import math
l=[800,600,750,900,1400,1200,1100,1500]
l1=['th','ga','ic','ha','te','lu','ni','ca']
s=input()
d=input()
if (s in l1 and d in l1):    
    i1=l1.index(s)
    i2=l1.index(d)
    if(i1>i2):
        k=l[i1+1:len(l)+1]+l[0:i2+1]
    else:
        k=l[i1:i2]
    print(k)
    print(float(math.ceil((sum(k)*5)/1000)))
else:
    print("invalid")
