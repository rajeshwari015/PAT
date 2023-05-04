"""def happynumber(s):
    i=0
    c=0
    while(i<=len(s)-1):
        c+=int(s[i])**2
        i+=1
    print(c)
    if len(str(c))>1:
        happynumber(str(c))
    else:
        if c==1:
            print("happy")
        else:
            print("sad")
        
        
s=input()
print(happynumber(s))"""
n=int(input())
s = str(n)
l = []
while s != '1':
    c = 0
    for i in s:
        c += (int(i) ** 2)
        if c in l:
            print(l)
        l.append(c)
        s = str(c)
print(1)
