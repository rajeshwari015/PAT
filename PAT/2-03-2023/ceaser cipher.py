"""s=input()
i=0
while i<len(s):
    letter=s[i]
    print(chr(ord(letter)+1),end="")
    i+=1
"""
from itertools import permutations
l=[1,2,3,4]
k=permutations(l)
l=[]
for i in k:
    l.append(list(i))
print(l)
