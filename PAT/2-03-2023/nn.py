"""s=input()
k=s.find("0")
for i in range(k+1,len(s)):
    if(s[i]=="0"):
       p=i
       break
print((p-k)-1)"""
s=input()
l=[]
l1=[]
for i in range(len(s)):
    if(s[i]=="0"):
        l.append(i)
for i in range(len(l)-1):
    l1.append((l[i+1]-l[i]))
print(max(l1)-1)

method 2


    
    
    
    


