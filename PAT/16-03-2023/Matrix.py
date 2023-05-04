r=int(input())
c=int(input())
l=list(map(int,input().split()))
a=[]
l1=[]
for i in range(0,len(l),r):
    x=i
    o=(l[x:x+r])
    a.append(sum(o))
print(a)
y=max(a)
print(a.index(y)+1)
    
